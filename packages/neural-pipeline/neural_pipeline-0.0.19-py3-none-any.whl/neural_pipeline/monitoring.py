import json
import os
from abc import ABCMeta
import numpy as np

from neural_pipeline.train_config import MetricsGroup
from neural_pipeline.utils import dict_recursive_bypass
from neural_pipeline.utils.file_structure_manager import FileStructManager, FolderRegistrable

__all__ = ['MonitorHub', 'AbstractMonitor', 'ConsoleMonitor', 'LogMonitor']


class AbstractMonitor(metaclass=ABCMeta):
    def __init__(self):
        self.epoch_num = 0

    def set_epoch_num(self, epoch_num: int) -> None:
        """
        Set current epoch num

        :param epoch_num: num of current epoch
        """
        self.epoch_num = epoch_num

    def update_metrics(self, metrics: {}) -> None:
        """
        Update metrics on   monitor

        :param metrics: metrics dict with keys 'metrics' and 'groups'
        """
        pass

    def update_losses(self, losses: {}) -> None:
        """
        Update losses on monitor

        :param losses: losses values dict with keys is names of stages in train pipeline (e.g. [train, validation])
        """
        pass

    @staticmethod
    def _iterate_by_losses(losses: {}, callback: callable) -> None:
        """
        Internal method for unify iteration by losses dict

        :param losses: dic of losses
        :param callback: callable, that call for every loss value and get params loss_name and loss_values: ``callback(name: str, values: np.ndarray)``
        """
        for m, v in losses.items():
            callback(m, v)

    def register_event(self, text: str) -> None:
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ConsoleMonitor(AbstractMonitor):
    class ResStr:
        def __init__(self, start: str):
            self.res = start

        def append(self, string: str):
            self.res += string

        def __str__(self):
            return self.res[:len(self.res) - 1]

    def update_losses(self, losses: {}) -> None:
        def on_loss(name: str, values: np.ndarray, string) -> None:
            string.append(" {}: [{:4f}, {:4f}, {:4f}];".format(name, np.min(values), np.mean(values), np.max(values)))

        res_string = self.ResStr("Epoch: [{}];".format(self.epoch_num))
        self._iterate_by_losses(losses, lambda m, v: on_loss(m, v, res_string))
        print(res_string)


class LogMonitor(AbstractMonitor, FolderRegistrable):
    def __init__(self, fsm: FileStructManager):
        super().__init__()

        self._fsm = fsm
        self._fsm.register_dir(self)
        self._storage = {}
        self._file = self._get_file_name(False)
        self._final_metrics_file = None

    def write_final_metrics(self) -> 'LogMonitor':
        self._final_metrics_file = self._get_final_file_name(False)
        return self

    def get_final_metrics_file(self) -> str or None:
        return self._final_metrics_file

    def update_metrics(self, metrics: {}) -> None:
        for metric in metrics['metrics']:
            self._process_metric(metric)

        for metrics_group in metrics['groups']:
            for metric in metrics_group.metrics():
                self._process_metric(metric, metrics_group.name())
            for group in metrics_group.groups():
                self._process_metric(group, metrics_group.name())

    def update_losses(self, losses: {}) -> None:
        def on_loss(name: str, values: np.ndarray):
            store = self._cur_storage([name, 'loss'])
            store.append(float(np.mean(values)))

        self._iterate_by_losses(losses, on_loss)

    def _process_metric(self, cur_metric, parent_tag: str = None):
        if isinstance(cur_metric, MetricsGroup):
            for m in cur_metric.metrics():
                if m.get_values().size > 0:
                    store = self._cur_storage([parent_tag, cur_metric.name(), m.name()])
                    store.append(float(np.mean(m.get_values())))
        else:
            values = cur_metric.get_values().astype(np.float32)
            if values.size > 0:
                store = self._cur_storage([parent_tag, cur_metric.name()])
                store.append(float(np.mean(values)))

    def _flush_metrics(self) -> None:
        with open(self._get_file_name(True), 'w') as out:
            json.dump(self._storage, out)

        if self._final_metrics_file is not None:
            res = dict_recursive_bypass(self._storage, lambda v: v[-1])
            with open(self._get_final_file_name(True), 'w') as out:
                json.dump(res, out)

    def _cur_storage(self, names: [str]):
        res = self._storage
        for i, n in enumerate(names):
            if n is None:
                continue
            if n not in res:
                res[n] = {} if i < (len(names) - 1) else []
            res = res[n]
        return res

    def close(self):
        self._flush_metrics()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def _get_file_name(self, create: bool) -> str:
        return os.path.join(self._fsm.get_path(self, create), 'metrics_log.json')

    def _get_final_file_name(self, create: bool) -> str:
        return os.path.join(self._fsm.get_path(self, create), 'metrics.json')

    def get_gir(self) -> str:
        return os.path.join('monitors', 'metrics_log')

    def get_name(self) -> str:
        return 'LogMonitor'


class MonitorHub:
    def __init__(self):
        self.monitors = []

    def set_epoch_num(self, epoch_num: int) -> None:
        """
        Set current epoch num

        :param epoch_num: num of current epoch
        """
        for m in self.monitors:
            m.set_epoch_num(epoch_num)

    def add_monitor(self, monitor: AbstractMonitor) -> 'MonitorHub':
        self.monitors.append(monitor)
        return self

    def update_metrics(self, metrics: {}) -> None:
        """
        Update metrics in all monitors

        :param metrics: metrics dict with keys 'metrics' and 'groups'
        """
        for m in self.monitors:
            m.update_metrics(metrics)

    def update_losses(self, losses: {}) -> None:
        """
        Update monitor

        :param losses: losses values with keys 'train' and 'validation'
        """
        for m in self.monitors:
            m.update_losses(losses)

    def register_event(self, text: str) -> None:
        for m in self.monitors:
            m.register_event(text)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for m in self.monitors:
            m.__exit__(exc_type, exc_val, exc_tb)
