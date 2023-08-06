import torch
from torch.nn import Module

from neural_pipeline.utils.file_structure_manager import FileStructManager, CheckpointsManager

__all__ = ['Model']


class Model:
    """
    Wrapper for :class:`torch.nn.Module`. This class provide initialization, call and serialization for it

    :param base_model: :class:`torch.nn.Module` object
    """

    class ModelException(Exception):
        def __init__(self, msg):
            self._msg = msg

        def __str__(self):
            return self._msg

    def __init__(self, base_model: Module):
        self._base_model = base_model
        self._checkpoints_manager = None

    def set_checkpoints_manager(self, manager: CheckpointsManager) -> 'Model':
        self._checkpoints_manager = manager
        return self

    def model(self) -> Module:
        """
        Get internal :class:`torch.nn.Module` object

        :return: internal :class:`torch.nn.Module` object
        """
        return self._base_model

    def load_weights(self, weights_file: str = None) -> None:
        """
        Load weight from checkpoint
        """
        if weights_file is not None:
            file = weights_file
        else:
            if self._checkpoints_manager is None:
                raise self.ModelException('No weights file or CheckpointsManagement specified')
            file = self._checkpoints_manager.weights_file()
        print("Model inited by file:", file, end='; ')
        pretrained_weights = torch.load(file)
        print("dict len before:", len(pretrained_weights), end='; ')
        pretrained_weights = {k: v for k, v in pretrained_weights.items() if k in self._base_model.state_dict()}
        self._base_model.load_state_dict(pretrained_weights)
        print("dict len after:", len(pretrained_weights))

    def save_weights(self) -> None:
        """
        Serialize weights to file
        """
        if self._checkpoints_manager is None:
            raise self.ModelException("Checkpoints manager doesn't specified. Use 'set_checkpoints_manager()'")
        torch.save(self._base_model.state_dict(), self._checkpoints_manager.weights_file())

    def __call__(self, x):
        """
        Call torch.nn.Module __call__ method

        :param x: model input data
        """
        return self._base_model(x)

    def to_device(self, device: torch.device) -> None:
        """
        Pass model to specified device
        """
        self._base_model.to(device)
