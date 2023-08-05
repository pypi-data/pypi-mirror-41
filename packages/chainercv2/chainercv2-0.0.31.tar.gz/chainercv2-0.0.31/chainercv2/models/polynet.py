"""
    PolyNet, implemented in Chainer.
    Original paper: 'PolyNet: A Pursuit of Structural Diversity in Very Deep Networks,'
    https://arxiv.org/abs/1611.05725.
"""

__all__ = ['PolyNet', 'polynet']

import os
import chainer.functions as F
import chainer.links as L
from chainer import Chain
from functools import partial
from chainer.serializers import load_npz
from .common import SimpleSequential, Concurrent, ParametricSequential, ParametricConcurrent


class ConvBlock(Chain):
    """
    Standard convolution block with Batch normalization and ReLU activation.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    ksize : int or tuple/list of 2 int
        Convolution window size.
    stride : int or tuple/list of 2 int
        Stride of the convolution.
    pad : int or tuple/list of 2 int
        Padding value for convolution layer.
    activate : bool, default True
        Whether activate the convolution block.
    """
    def __init__(self,
                 in_channels,
                 out_channels,
                 ksize,
                 stride,
                 pad,
                 activate=True):
        super(ConvBlock, self).__init__()
        self.activate = activate

        with self.init_scope():
            self.conv = L.Convolution2D(
                in_channels=in_channels,
                out_channels=out_channels,
                ksize=ksize,
                stride=stride,
                pad=pad,
                nobias=True)
            self.bn = L.BatchNormalization(
                size=out_channels,
                eps=1e-5)
            if self.activate:
                self.activ = F.relu

    def __call__(self, x):
        x = self.conv(x)
        x = self.bn(x)
        if self.activate:
            x = self.activ(x)
        return x


def conv1x1_block(in_channels,
                  out_channels,
                  stride=1,
                  activate=True):
    """
    1x1 version of the standard convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    stride : int or tuple/list of 2 int, default 1
        Stride of the convolution.
    activate : bool, default True
        Whether activate the convolution block.
    """
    return ConvBlock(
        in_channels=in_channels,
        out_channels=out_channels,
        ksize=1,
        stride=stride,
        pad=0,
        activate=activate)


def conv3x3_block(in_channels,
                  out_channels,
                  stride,
                  pad=1,
                  activate=True):
    """
    3x3 version of the standard convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    stride : int or tuple/list of 2 int
        Stride of the convolution.
    pad : int or tuple/list of 2 int, default 0
        Padding value for convolution layer.
    activate : bool, default True
        Whether activate the convolution block.
    """
    return ConvBlock(
        in_channels=in_channels,
        out_channels=out_channels,
        ksize=3,
        stride=stride,
        pad=pad,
        activate=activate)


class PolyConv(Chain):
    """
    PolyNet specific convolution block. A block that is used inside poly-N (poly-2, poly-3, and so on) modules.
    The Convolution layer is shared between all Inception blocks inside a poly-N module. BatchNorm layers are not
    shared between Inception blocks and therefore the number of BatchNorm layers is equal to the number of Inception
    blocks inside a poly-N module.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    ksize : int or tuple/list of 2 int
        Convolution window size.
    stride : int or tuple/list of 2 int
        Stride of the convolution.
    pad : int or tuple/list of 2 int
        Padding value for convolution layer.
    num_blocks : int
        Number of blocks (BatchNorm layers).
    """
    def __init__(self,
                 in_channels,
                 out_channels,
                 ksize,
                 stride,
                 pad,
                 num_blocks):
        super(PolyConv, self).__init__()
        with self.init_scope():
            self.conv = L.Convolution2D(
                in_channels=in_channels,
                out_channels=out_channels,
                ksize=ksize,
                stride=stride,
                pad=pad,
                nobias=True)
            for i in range(num_blocks):
                setattr(self, "bn{}".format(i + 1), L.BatchNormalization(
                    size=out_channels,
                    eps=1e-5))
            self.activ = F.relu

    def __call__(self, x, index):
        x = self.conv(x)
        bn = getattr(self, "bn{}".format(index + 1))
        x = bn(x)
        x = self.activ(x)
        return x


def poly_conv1x1(in_channels,
                 out_channels,
                 num_blocks):
    """
    1x1 version of the PolyNet specific convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    num_blocks : int
        Number of blocks (BatchNorm layers).
    """
    return PolyConv(
        in_channels=in_channels,
        out_channels=out_channels,
        ksize=1,
        stride=1,
        pad=0,
        num_blocks=num_blocks)


class MaxPoolBranch(Chain):
    """
    PolyNet specific max pooling branch block.
    """
    def __init__(self):
        super(MaxPoolBranch, self).__init__()
        with self.init_scope():
            self.pool = partial(
                F.max_pooling_2d,
                ksize=3,
                stride=2,
                pad=0,
                cover_all=False)

    def __call__(self, x):
        x = self.pool(x)
        return x


class Conv1x1Branch(Chain):
    """
    PolyNet specific convolutional 1x1 branch block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    """
    def __init__(self,
                 in_channels,
                 out_channels):
        super(Conv1x1Branch, self).__init__()
        with self.init_scope():
            self.conv = conv1x1_block(
                in_channels=in_channels,
                out_channels=out_channels)

    def __call__(self, x):
        x = self.conv(x)
        return x


class Conv3x3Branch(Chain):
    """
    PolyNet specific convolutional 3x3 branch block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    """
    def __init__(self,
                 in_channels,
                 out_channels):
        super(Conv3x3Branch, self).__init__()
        with self.init_scope():
            self.conv = conv3x3_block(
                in_channels=in_channels,
                out_channels=out_channels,
                stride=2,
                pad=0)

    def __call__(self, x):
        x = self.conv(x)
        return x


class ConvSeqBranch(Chain):
    """
    PolyNet specific convolutional sequence branch block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels_list : list of tuple of int
        List of numbers of output channels.
    kernel_size_list : list of tuple of int or tuple of tuple/list of 2 int
        List of convolution window sizes.
    strides_list : list of tuple of int or tuple of tuple/list of 2 int
        List of strides of the convolution.
    padding_list : list of tuple of int or tuple of tuple/list of 2 int
        List of padding values for convolution layers.
    """
    def __init__(self,
                 in_channels,
                 out_channels_list,
                 kernel_size_list,
                 strides_list,
                 padding_list):
        super(ConvSeqBranch, self).__init__()
        assert (len(out_channels_list) == len(kernel_size_list))
        assert (len(out_channels_list) == len(strides_list))
        assert (len(out_channels_list) == len(padding_list))

        with self.init_scope():
            self.conv_list = SimpleSequential()
            with self.conv_list.init_scope():
                for i, (out_channels, kernel_size, strides, padding) in enumerate(zip(
                        out_channels_list, kernel_size_list, strides_list, padding_list)):
                    setattr(self.conv_list, "conv{}".format(i + 1), ConvBlock(
                        in_channels=in_channels,
                        out_channels=out_channels,
                        ksize=kernel_size,
                        stride=strides,
                        pad=padding))
                    in_channels = out_channels

    def __call__(self, x):
        x = self.conv_list(x)
        return x


class PolyConvSeqBranch(Chain):
    """
    PolyNet specific convolutional sequence branch block with internal PolyNet specific convolution blocks.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels_list : list of tuple of int
        List of numbers of output channels.
    kernel_size_list : list of tuple of int or tuple of tuple/list of 2 int
        List of convolution window sizes.
    strides_list : list of tuple of int or tuple of tuple/list of 2 int
        List of strides of the convolution.
    padding_list : list of tuple of int or tuple of tuple/list of 2 int
        List of padding values for convolution layers.
    num_blocks : int
        Number of blocks for PolyConv.
    """
    def __init__(self,
                 in_channels,
                 out_channels_list,
                 kernel_size_list,
                 strides_list,
                 padding_list,
                 num_blocks):
        super(PolyConvSeqBranch, self).__init__()
        assert (len(out_channels_list) == len(kernel_size_list))
        assert (len(out_channels_list) == len(strides_list))
        assert (len(out_channels_list) == len(padding_list))

        with self.init_scope():
            self.conv_list = ParametricSequential()
            with self.conv_list.init_scope():
                for i, (out_channels, kernel_size, strides, padding) in enumerate(zip(
                        out_channels_list, kernel_size_list, strides_list, padding_list)):
                    setattr(self.conv_list, "conv{}".format(i + 1), PolyConv(
                        in_channels=in_channels,
                        out_channels=out_channels,
                        ksize=kernel_size,
                        stride=strides,
                        pad=padding,
                        num_blocks=num_blocks))
                    in_channels = out_channels

    def __call__(self, x, index):
        x = self.conv_list(x, index=index)
        return x


class TwoWayABlock(Chain):
    """
    PolyNet type Inception-A block.
    """
    def __init__(self):
        super(TwoWayABlock, self).__init__()
        in_channels = 384

        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(32, 48, 64),
                    kernel_size_list=(1, 3, 3),
                    strides_list=(1, 1, 1),
                    padding_list=(0, 1, 1)))
                setattr(self.branches, "branch2", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(32, 32),
                    kernel_size_list=(1, 3),
                    strides_list=(1, 1),
                    padding_list=(0, 1)))
                setattr(self.branches, "branch3", Conv1x1Branch(
                    in_channels=in_channels,
                    out_channels=32))
                self.conv = conv1x1_block(
                    in_channels=128,
                    out_channels=in_channels,
                    activate=False)

    def __call__(self, x):
        x = self.branches(x)
        x = self.conv(x)
        return x


class TwoWayBBlock(Chain):
    """
    PolyNet type Inception-B block.
    """
    def __init__(self):
        super(TwoWayBBlock, self).__init__()
        in_channels = 1152

        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(128, 160, 192),
                    kernel_size_list=(1, (1, 7), (7, 1)),
                    strides_list=(1, 1, 1),
                    padding_list=(0, (0, 3), (3, 0))))
                setattr(self.branches, "branch2", Conv1x1Branch(
                    in_channels=in_channels,
                    out_channels=192))
                self.conv = conv1x1_block(
                    in_channels=384,
                    out_channels=in_channels,
                    activate=False)

    def __call__(self, x):
        x = self.branches(x)
        x = self.conv(x)
        return x


class TwoWayCBlock(Chain):
    """
    PolyNet type Inception-C block.
    """
    def __init__(self):
        super(TwoWayCBlock, self).__init__()
        in_channels = 2048

        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(192, 224, 256),
                    kernel_size_list=(1, (1, 3), (3, 1)),
                    strides_list=(1, 1, 1),
                    padding_list=(0, (0, 1), (1, 0))))
                setattr(self.branches, "branch2", Conv1x1Branch(
                    in_channels=in_channels,
                    out_channels=192))
                self.conv = conv1x1_block(
                    in_channels=448,
                    out_channels=in_channels,
                    activate=False)

    def __call__(self, x):
        x = self.branches(x)
        x = self.conv(x)
        return x


class PolyPreBBlock(Chain):
    """
    PolyNet type PolyResidual-Pre-B block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    num_blocks : int
        Number of blocks (BatchNorm layers).
    """
    def __init__(self,
                 num_blocks):
        super(PolyPreBBlock, self).__init__()
        in_channels = 1152

        with self.init_scope():
            self.branches = ParametricConcurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", PolyConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(128, 160, 192),
                    kernel_size_list=(1, (1, 7), (7, 1)),
                    strides_list=(1, 1, 1),
                    padding_list=(0, (0, 3), (3, 0)),
                    num_blocks=num_blocks))
                setattr(self.branches, "branch2", poly_conv1x1(
                    in_channels=in_channels,
                    out_channels=192,
                    num_blocks=num_blocks))

    def __call__(self, x, index):
        x = self.branches(x, index=index)
        return x


class PolyPreCBlock(Chain):
    """
    PolyNet type PolyResidual-Pre-C block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    num_blocks : int
        Number of blocks (BatchNorm layers).
    """
    def __init__(self,
                 num_blocks):
        super(PolyPreCBlock, self).__init__()
        in_channels = 2048

        with self.init_scope():
            self.branches = ParametricConcurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", PolyConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(192, 224, 256),
                    kernel_size_list=(1, (1, 3), (3, 1)),
                    strides_list=(1, 1, 1),
                    padding_list=(0, (0, 1), (1, 0)),
                    num_blocks=num_blocks))
                setattr(self.branches, "branch2", poly_conv1x1(
                    in_channels=in_channels,
                    out_channels=192,
                    num_blocks=num_blocks))

    def __call__(self, x, index):
        x = self.branches(x, index=index)
        return x


def poly_res_b_block():
    """
    PolyNet type PolyResidual-Res-B block.
    """
    return conv1x1_block(
        in_channels=384,
        out_channels=1152,
        stride=1,
        activate=False)


def poly_res_c_block():
    """
    PolyNet type PolyResidual-Res-C block.
    """
    return conv1x1_block(
        in_channels=448,
        out_channels=2048,
        stride=1,
        activate=False)


class MultiResidual(Chain):
    """
    Base class for constructing N-way modules (2-way, 3-way, and so on). Actually it is for 2-way modules.

    Parameters:
    ----------
    scale : float, default 1.0
        Scale value for each residual branch.
    res_block : Chain class
        Residual branch block.
    num_blocks : int
        Number of residual branches.
    """
    def __init__(self,
                 scale,
                 res_block,
                 num_blocks):
        super(MultiResidual, self).__init__()
        assert (num_blocks >= 1)
        self.scale = scale
        self.num_blocks = num_blocks

        with self.init_scope():
            for i in range(num_blocks):
                setattr(self, "res_block{}".format(i + 1), res_block())
            self.activ = F.relu

    def __call__(self, x):
        out = x
        for i in range(self.num_blocks):
            res_block = getattr(self, "res_block{}".format(i + 1))
            out = out + self.scale * res_block(x)
        out = self.activ(out)
        return out


class PolyResidual(Chain):
    """
    The other base class for constructing N-way poly-modules. Actually it is for 3-way poly-modules.

    Parameters:
    ----------
    scale : float, default 1.0
        Scale value for each residual branch.
    res_block : Chain class
        Residual branch block.
    num_blocks : int
        Number of residual branches.
    pre_block : Chain class
        Preliminary block.
    """
    def __init__(self,
                 scale,
                 res_block,
                 num_blocks,
                 pre_block):
        super(PolyResidual, self).__init__()
        assert (num_blocks >= 1)
        self.scale = scale
        self.num_blocks = num_blocks

        with self.init_scope():
            self.pre_block = pre_block(num_blocks=num_blocks)
            for i in range(num_blocks):
                setattr(self, "res_block{}".format(i + 1), res_block())
            self.activ = F.relu

    def __call__(self, x):
        out = x
        for index in range(self.num_blocks):
            x = self.pre_block(x, index)
            res_block = getattr(self, "res_block{}".format(index + 1))
            x = res_block(x)
            out = out + self.scale * x
            x = self.activ(x)
        out = self.activ(out)
        return out


class PolyBaseUnit(Chain):
    """
    PolyNet unit base class.

    Parameters:
    ----------
    two_way_scale : float
        Scale value for 2-way stage.
    two_way_block : Chain class
        Residual branch block for 2-way-stage.
    poly_scale : float, default 0.0
        Scale value for 2-way stage.
    poly_res_block : Chain class, default None
        Residual branch block for poly-stage.
    poly_pre_block : Chain class, default None
        Preliminary branch block for poly-stage.
    """
    def __init__(self,
                 two_way_scale,
                 two_way_block,
                 poly_scale=0.0,
                 poly_res_block=None,
                 poly_pre_block=None):
        super(PolyBaseUnit, self).__init__()
        with self.init_scope():
            if poly_res_block is not None:
                assert (poly_scale != 0.0)
                assert (poly_pre_block is not None)
                self.poly = PolyResidual(
                    scale=poly_scale,
                    res_block=poly_res_block,
                    num_blocks=3,
                    pre_block=poly_pre_block)
            else:
                assert (poly_scale == 0.0)
                assert (poly_pre_block is None)
                self.poly = None
            self.twoway = MultiResidual(
                scale=two_way_scale,
                res_block=two_way_block,
                num_blocks=2)

    def __call__(self, x):
        if self.poly is not None:
            x = self.poly(x)
        x = self.twoway(x)
        return x


class PolyAUnit(PolyBaseUnit):
    """
    PolyNet type A unit.

    Parameters:
    ----------
    two_way_scale : float
        Scale value for 2-way stage.
    poly_scale : float
        Scale value for 2-way stage.
    """
    def __init__(self,
                 two_way_scale,
                 poly_scale=0.0):
        super(PolyAUnit, self).__init__(
            two_way_scale=two_way_scale,
            two_way_block=TwoWayABlock)
        assert (poly_scale == 0.0)


class PolyBUnit(PolyBaseUnit):
    """
    PolyNet type B unit.

    Parameters:
    ----------
    two_way_scale : float
        Scale value for 2-way stage.
    poly_scale : float
        Scale value for 2-way stage.
    """
    def __init__(self,
                 two_way_scale,
                 poly_scale):
        super(PolyBUnit, self).__init__(
            two_way_scale=two_way_scale,
            two_way_block=TwoWayBBlock,
            poly_scale=poly_scale,
            poly_res_block=poly_res_b_block,
            poly_pre_block=PolyPreBBlock)


class PolyCUnit(PolyBaseUnit):
    """
    PolyNet type C unit.

    Parameters:
    ----------
    two_way_scale : float
        Scale value for 2-way stage.
    poly_scale : float
        Scale value for 2-way stage.
    """
    def __init__(self,
                 two_way_scale,
                 poly_scale):
        super(PolyCUnit, self).__init__(
            two_way_scale=two_way_scale,
            two_way_block=TwoWayCBlock,
            poly_scale=poly_scale,
            poly_res_block=poly_res_c_block,
            poly_pre_block=PolyPreCBlock)


class ReductionAUnit(Chain):
    """
    PolyNet type Reduction-A unit.
    """
    def __init__(self):
        super(ReductionAUnit, self).__init__()
        in_channels = 384

        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(256, 256, 384),
                    kernel_size_list=(1, 3, 3),
                    strides_list=(1, 1, 2),
                    padding_list=(0, 1, 0)))
                setattr(self.branches, "branch2", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(384,),
                    kernel_size_list=(3,),
                    strides_list=(2,),
                    padding_list=(0,)))
                setattr(self.branches, "branch3", MaxPoolBranch())

    def __call__(self, x):
        x = self.branches(x)
        return x


class ReductionBUnit(Chain):
    """
    PolyNet type Reduction-B unit.
    """
    def __init__(self):
        super(ReductionBUnit, self).__init__()
        in_channels = 1152

        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(256, 256, 256),
                    kernel_size_list=(1, 3, 3),
                    strides_list=(1, 1, 2),
                    padding_list=(0, 1, 0)))
                setattr(self.branches, "branch2", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(256, 256),
                    kernel_size_list=(1, 3),
                    strides_list=(1, 2),
                    padding_list=(0, 0)))
                setattr(self.branches, "branch3", ConvSeqBranch(
                    in_channels=in_channels,
                    out_channels_list=(256, 384),
                    kernel_size_list=(1, 3),
                    strides_list=(1, 2),
                    padding_list=(0, 0)))
                setattr(self.branches, "branch4", MaxPoolBranch())

    def __call__(self, x):
        x = self.branches(x)
        return x


class PolyBlock3a(Chain):
    """
    PolyNet type Mixed-3a block.
    """
    def __init__(self):
        super(PolyBlock3a, self).__init__()
        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", MaxPoolBranch())
                setattr(self.branches, "branch2", Conv3x3Branch(
                    in_channels=64,
                    out_channels=96))

    def __call__(self, x):
        x = self.branches(x)
        return x


class PolyBlock4a(Chain):
    """
    PolyNet type Mixed-4a block.
    """
    def __init__(self):
        super(PolyBlock4a, self).__init__()
        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", ConvSeqBranch(
                    in_channels=160,
                    out_channels_list=(64, 96),
                    kernel_size_list=(1, 3),
                    strides_list=(1, 1),
                    padding_list=(0, 0)))
                setattr(self.branches, "branch2", ConvSeqBranch(
                    in_channels=160,
                    out_channels_list=(64, 64, 64, 96),
                    kernel_size_list=(1, (7, 1), (1, 7), 3),
                    strides_list=(1, 1, 1, 1),
                    padding_list=(0, (3, 0), (0, 3), 0)))

    def __call__(self, x):
        x = self.branches(x)
        return x


class PolyBlock5a(Chain):
    """
    PolyNet type Mixed-5a block.
    """
    def __init__(self):
        super(PolyBlock5a, self).__init__()
        with self.init_scope():
            self.branches = Concurrent()
            with self.branches.init_scope():
                setattr(self.branches, "branch1", MaxPoolBranch())
                setattr(self.branches, "branch2", Conv3x3Branch(
                    in_channels=192,
                    out_channels=192))

    def __call__(self, x):
        x = self.branches(x)
        return x


class PolyInitBlock(Chain):
    """
    PolyNet specific initial block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    """
    def __init__(self,
                 in_channels):
        super(PolyInitBlock, self).__init__()
        with self.init_scope():
            self.conv1 = ConvBlock(
                in_channels=in_channels,
                out_channels=32,
                ksize=3,
                stride=2,
                pad=0)
            self.conv2 = ConvBlock(
                in_channels=32,
                out_channels=32,
                ksize=3,
                stride=1,
                pad=0)
            self.conv3 = ConvBlock(
                in_channels=32,
                out_channels=64,
                ksize=3,
                stride=1,
                pad=1)
            self.block1 = PolyBlock3a()
            self.block2 = PolyBlock4a()
            self.block3 = PolyBlock5a()

    def __call__(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return x


class PolyNet(Chain):
    """
    PolyNet model from 'PolyNet: A Pursuit of Structural Diversity in Very Deep Networks,'
    https://arxiv.org/abs/1611.05725.

    Parameters:
    ----------
    two_way_scales : list of list of floats
        Two way scale values for each normal unit.
    poly_scales : list of list of floats
        Three way scale values for each normal unit.
    dropout_rate : float, default 0.2
        Fraction of the input units to drop. Must be a number between 0 and 1.
    in_channels : int, default 3
        Number of input channels.
    in_size : tuple of two ints, default (331, 331)
        Spatial size of the expected input image.
    classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 two_way_scales,
                 poly_scales,
                 dropout_rate=0.2,
                 in_channels=3,
                 in_size=(331, 331),
                 classes=1000):
        super(PolyNet, self).__init__()
        self.in_size = in_size
        self.classes = classes
        normal_units = [PolyAUnit, PolyBUnit, PolyCUnit]
        reduction_units = [ReductionAUnit, ReductionBUnit]

        with self.init_scope():
            self.features = SimpleSequential()
            with self.features.init_scope():
                setattr(self.features, "init_block", PolyInitBlock(
                    in_channels=in_channels))

                for i, (two_way_scales_per_stage, poly_scales_per_stage) in enumerate(zip(two_way_scales, poly_scales)):
                    stage = SimpleSequential()
                    with stage.init_scope():
                        for j, (two_way_scale, poly_scale) in enumerate(zip(
                                two_way_scales_per_stage, poly_scales_per_stage)):
                            if (j == 0) and (i != 0):
                                unit = reduction_units[i - 1]
                                setattr(stage, "unit{}".format(j + 1), unit())
                            else:
                                unit = normal_units[i]
                                setattr(stage, "unit{}".format(j + 1), unit(
                                    two_way_scale=two_way_scale,
                                    poly_scale=poly_scale))
                    setattr(self.features, "stage{}".format(i + 1), stage)

                setattr(self.features, 'final_pool', partial(
                    F.average_pooling_2d,
                    ksize=9,
                    stride=1))

            in_channels = 2048
            self.output = SimpleSequential()
            with self.output.init_scope():
                setattr(self.output, 'flatten', partial(
                    F.reshape,
                    shape=(-1, in_channels)))
                setattr(self.output, 'dropout', partial(
                    F.dropout,
                    ratio=dropout_rate))
                setattr(self.output, 'fc', L.Linear(
                    in_size=in_channels,
                    out_size=classes))

    def __call__(self, x):
        x = self.features(x)
        x = self.output(x)
        return x


def get_polynet(model_name=None,
                pretrained=False,
                root=os.path.join('~', '.chainer', 'models'),
                **kwargs):
    """
    Create PolyNet model with specific parameters.

    Parameters:
    ----------
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    two_way_scales = [
        [1.000000, 0.992308, 0.984615, 0.976923, 0.969231, 0.961538, 0.953846, 0.946154, 0.938462, 0.930769],
        [0.000000, 0.915385, 0.900000, 0.884615, 0.869231, 0.853846, 0.838462, 0.823077, 0.807692, 0.792308, 0.776923],
        [0.000000, 0.761538, 0.746154, 0.730769, 0.715385, 0.700000]]
    poly_scales = [
        [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.923077, 0.907692, 0.892308, 0.876923, 0.861538, 0.846154, 0.830769, 0.815385, 0.800000, 0.784615],
        [0.000000, 0.769231, 0.753846, 0.738462, 0.723077, 0.707692]]

    net = PolyNet(
        two_way_scales=two_way_scales,
        poly_scales=poly_scales,
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


def polynet(**kwargs):
    """
    PolyNet model from 'PolyNet: A Pursuit of Structural Diversity in Very Deep Networks,'
    https://arxiv.org/abs/1611.05725.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    return get_polynet(model_name="polynet", **kwargs)


def _test():
    import numpy as np
    import chainer

    chainer.global_config.train = False

    pretrained = False

    models = [
        polynet,
    ]

    for model in models:

        net = model(pretrained=pretrained)
        weight_count = net.count_params()
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != polynet or weight_count == 95366600)

        x = np.zeros((1, 3, 331, 331), np.float32)
        y = net(x)
        assert (y.shape == (1, 1000))


if __name__ == "__main__":
    _test()
