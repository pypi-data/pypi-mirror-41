"""
    DarkNet-53, implemented in Chainer.
    Original source: 'YOLOv3: An Incremental Improvement,' https://arxiv.org/abs/1804.02767.
"""

__all__ = ['DarkNet53', 'darknet53']

import os
import chainer.functions as F
import chainer.links as L
from chainer import Chain
from functools import partial
from chainer.serializers import load_npz
from .common import conv1x1_block, conv3x3_block, SimpleSequential


class DarkUnit(Chain):
    """
    DarkNet unit.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    alpha : float
        Slope coefficient for Leaky ReLU activation.
    """
    def __init__(self,
                 in_channels,
                 out_channels,
                 alpha):
        super(DarkUnit, self).__init__()
        assert (out_channels % 2 == 0)
        mid_channels = out_channels // 2

        with self.init_scope():
            self.conv1 = conv1x1_block(
                in_channels=in_channels,
                out_channels=mid_channels,
                activation=partial(
                    F.leaky_relu,
                    slope=alpha))
            self.conv2 = conv3x3_block(
                in_channels=mid_channels,
                out_channels=out_channels,
                activation=partial(
                    F.leaky_relu,
                    slope=alpha))

    def __call__(self, x):
        identity = x
        x = self.conv1(x)
        x = self.conv2(x)
        return x + identity


class DarkNet53(Chain):
    """
    DarkNet-53 model from 'YOLOv3: An Incremental Improvement,' https://arxiv.org/abs/1804.02767.

    Parameters:
    ----------
    channels : list of list of int
        Number of output channels for each unit.
    init_block_channels : int
        Number of output channels for the initial unit.
    alpha : float, default 0.1
        Slope coefficient for Leaky ReLU activation.
    in_channels : int, default 3
        Number of input channels.
    in_size : tuple of two ints, default (224, 224)
        Spatial size of the expected input image.
    classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 channels,
                 init_block_channels,
                 alpha=0.1,
                 in_channels=3,
                 in_size=(224, 224),
                 classes=1000):
        super(DarkNet53, self).__init__()
        self.in_size = in_size
        self.classes = classes

        with self.init_scope():
            self.features = SimpleSequential()
            with self.features.init_scope():
                setattr(self.features, "init_block", conv3x3_block(
                    in_channels=in_channels,
                    out_channels=init_block_channels,
                    activation=partial(
                        F.leaky_relu,
                        slope=alpha)))
                in_channels = init_block_channels
                for i, channels_per_stage in enumerate(channels):
                    stage = SimpleSequential()
                    with stage.init_scope():
                        for j, out_channels in enumerate(channels_per_stage):
                            if j == 0:
                                setattr(stage, "unit{}".format(j + 1), conv3x3_block(
                                    in_channels=in_channels,
                                    out_channels=out_channels,
                                    stride=2,
                                    activation=partial(
                                        F.leaky_relu,
                                        slope=alpha)))
                            else:
                                setattr(stage, "unit{}".format(j + 1), DarkUnit(
                                    in_channels=in_channels,
                                    out_channels=out_channels,
                                    alpha=alpha))
                            in_channels = out_channels
                    setattr(self.features, "stage{}".format(i + 1), stage)
                setattr(self.features, "final_pool", partial(
                    F.average_pooling_2d,
                    ksize=7,
                    stride=1))

            self.output = SimpleSequential()
            with self.output.init_scope():
                setattr(self.output, "flatten", partial(
                    F.reshape,
                    shape=(-1, in_channels)))
                setattr(self.output, "fc", L.Linear(
                    in_size=in_channels,
                    out_size=classes))

    def __call__(self, x):
        x = self.features(x)
        x = self.output(x)
        return x


def get_darknet53(model_name=None,
                  pretrained=False,
                  root=os.path.join('~', '.chainer', 'models'),
                  **kwargs):
    """
    Create DarkNet model with specific parameters.

    Parameters:
    ----------
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    init_block_channels = 32
    layers = [2, 3, 9, 9, 5]
    channels_per_layers = [64, 128, 256, 512, 1024]
    channels = [[ci] * li for (ci, li) in zip(channels_per_layers, layers)]

    net = DarkNet53(
        channels=channels,
        init_block_channels=init_block_channels,
        **kwargs)

    if pretrained:
        if (model_name is None) or (not model_name):
            raise ValueError("Parameter `model_name` should be properly initialized for loading pretrained model.")
        from .model_store import get_model_file
        load_npz(
            file=get_model_file(
                model_name=model_name,
                local_model_store_dir_path=root),
            obj=net)

    return net


def darknet53(**kwargs):
    """
    DarkNet-53 'Reference' model from 'YOLOv3: An Incremental Improvement,' https://arxiv.org/abs/1804.02767.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    return get_darknet53(model_name="darknet53", **kwargs)


def _test():
    import numpy as np
    import chainer

    chainer.global_config.train = False

    pretrained = False

    models = [
        darknet53,
    ]

    for model in models:

        net = model(pretrained=pretrained)
        weight_count = net.count_params()
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != darknet53 or weight_count == 41609928)

        x = np.zeros((1, 3, 224, 224), np.float32)
        y = net(x)
        assert (y.shape == (1, 1000))


if __name__ == "__main__":
    _test()
