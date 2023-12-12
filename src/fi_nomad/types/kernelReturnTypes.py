"""Defines an interface for data objects returned from decomposition kernels."""
from abc import ABC
from typing import Union
from dataclasses import dataclass
from .types import FloatArrayType

# This will facilitate a future conversion from returning the full
# low-rank matrix to returning a factored version.
SolutionType = FloatArrayType


@dataclass
class KernelReturnBase(ABC):
    """Base interface for returned kernel data. Enforces that every kernel
    must return a "reconstruction" member with its solution.
    This facilitates usability and a smoother transition to returning the
    decomposed version of the low-rank estimation matrix.
    """

    reconstruction: SolutionType


@dataclass
class BaseModelFreeKernelReturnType(KernelReturnBase):
    """Base/naive method returns only the reconstruction. (Adds nothing to base.)"""


@dataclass
class SingleVarianceGaussianModelKernelReturnType(KernelReturnBase):
    """The simple Gaussian model returns a (scalar) variance in addition to
    the low-rank estimate.
    """

    variance: float


@dataclass
class RowwiseVarianceGaussianModelKernelReturnType(KernelReturnBase):
    """The rowwise-variance Gaussian model returns the estimated per-row
    variance of the model, in addition to the low-rank estimate (means).
    """

    variance: FloatArrayType


KernelReturnDataType = Union[
    BaseModelFreeKernelReturnType,
    SingleVarianceGaussianModelKernelReturnType,
    RowwiseVarianceGaussianModelKernelReturnType,
]


@dataclass
class KernelReturnType:
    """Enforces that kernels return a summary string and their actual data."""

    summary: str
    data: KernelReturnDataType
