"""pyxmolpp2.geometry module"""
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
import numpy
__all__  = [
"GeometryException",
"AngleValue",
"BadRotationMatrix",
"AlignmentError",
"Rotation3d",
"Transformation3d",
"Translation3d",
"UniformScale3d",
"VectorXYZ",
"XYZ",
"Degrees",
"Radians",
"angle",
"calc_alignment",
"calc_autocorr_order_2",
"calc_geom_center",
"calc_rmsd",
"cos",
"degrees_to_radians",
"dihedral_angle",
"distance",
"distance2",
"fabs",
"radians_to_degrees",
"sin",
"tan"
]
class GeometryException(Exception, BaseException):
    pass
class AngleValue():
    def __add__(self, arg0: AngleValue) -> AngleValue:
        pass
    def __ge__(self, arg0: AngleValue) -> bool:
        pass
    def __gt__(self, arg0: AngleValue) -> bool:
        pass
    def __le__(self, arg0: AngleValue) -> bool:
        pass
    def __lt__(self, arg0: AngleValue) -> bool:
        pass
    def __mul__(self, arg0: float) -> AngleValue:
        pass
    def __neg__(self) -> AngleValue:
        pass
    def __rmul__(self, arg0: float) -> AngleValue:
        pass
    def __sub__(self, arg0: AngleValue) -> AngleValue:
        pass
    def __truediv__(self, arg0: float) -> AngleValue:
        pass
    def to_standard_range(self) -> AngleValue:
        """
Turns angle to range [-Pi..Pi)
"""
    @property
    def degrees(self) -> float:
        pass
    @property
    def radians(self) -> float:
        pass
    pass
class BadRotationMatrix(GeometryException, Exception, BaseException):
    pass
class AlignmentError(GeometryException, Exception, BaseException):
    pass
class Rotation3d():
    @overload
    def __init__(self, rotation_axis: XYZ, rotation_angle: AngleValue) -> None:
        pass
    @overload
    def __init__(self) -> None:
        pass
    @overload
    def __mul__(self, arg0: Rotation3d) -> Rotation3d:
        pass
    @overload
    def __mul__(self, arg0: Translation3d) -> Transformation3d:
        pass
    @overload
    def __mul__(self, arg0: UniformScale3d) -> Transformation3d:
        pass
    @overload
    def __rmul__(self, arg0: Translation3d) -> Transformation3d:
        pass
    @overload
    def __rmul__(self, arg0: UniformScale3d) -> Transformation3d:
        pass
    def axis(self) -> XYZ:
        """
Returns axis of rotation
"""
    def inverted(self) -> Rotation3d:
        """
Returns inverted rotation
"""
    def matrix3d(self) -> numpy.ndarray:
        pass
    def theta(self) -> AngleValue:
        """
Returns angle of rotation
"""
    def transform(self, r: XYZ) -> XYZ:
        """
Returns rotated point
"""
    pass
class Transformation3d():
    @overload
    def __init__(self) -> None:
        pass
    @overload
    def __init__(self, rotation_followed_by: Rotation3d, translation: Translation3d) -> None:
        pass
    @overload
    def __mul__(self, arg0: Rotation3d) -> Transformation3d:
        pass
    @overload
    def __mul__(self, arg0: Transformation3d) -> Transformation3d:
        pass
    @overload
    def __mul__(self, arg0: UniformScale3d) -> Transformation3d:
        pass
    @overload
    def __mul__(self, arg0: Translation3d) -> Transformation3d:
        pass
    @overload
    def __rmul__(self, arg0: Rotation3d) -> Transformation3d:
        pass
    @overload
    def __rmul__(self, arg0: UniformScale3d) -> Transformation3d:
        pass
    @overload
    def __rmul__(self, arg0: Translation3d) -> Transformation3d:
        pass
    def inverted(self) -> Transformation3d:
        """
Returns inverted transformation
"""
    def matrix3d(self) -> numpy.ndarray:
        pass
    def transform(self, r: XYZ) -> XYZ:
        """
Returns transformed point
"""
    def vector3d(self) -> XYZ:
        pass
    pass
class Translation3d():
    @overload
    def __init__(self, dr: XYZ) -> None:
        pass
    @overload
    def __init__(self) -> None:
        pass
    def __mul__(self, arg0: Translation3d) -> Translation3d:
        pass
    def dr(self) -> XYZ:
        pass
    def inverted(self) -> Translation3d:
        pass
    def transform(self, r: XYZ) -> XYZ:
        """
Returns translated point
"""
    pass
class UniformScale3d():
    @overload
    def __init__(self) -> None:
        pass
    @overload
    def __init__(self, scale_factor: float) -> None:
        pass
    @overload
    def __mul__(self, arg0: UniformScale3d) -> UniformScale3d:
        pass
    @overload
    def __mul__(self, arg0: Translation3d) -> Transformation3d:
        pass
    def __rmul__(self, arg0: Translation3d) -> Transformation3d:
        pass
    def inverted(self) -> UniformScale3d:
        """
Returns inverted scale transformation
"""
    def transform(self, r: XYZ) -> XYZ:
        """
Returns scaled point
"""
    @property
    def scale(self) -> float:
        """Scale factor"""
    pass
class VectorXYZ():
    def __bool__(self) -> bool:
        """
Check whether the list is nonempty
"""
    @overload
    def __delitem__(self, arg0: int) -> None:
        pass
    @overload
    def __delitem__(self, arg0: slice) -> None:
        pass
    @overload
    def __getitem__(self, arg0: int) -> XYZ:
        pass
    @overload
    def __getitem__(self, s: slice) -> VectorXYZ:
        pass
    @overload
    def __init__(self, arg0: iterable) -> None:
        pass
    @overload
    def __init__(self, arg0: VectorXYZ) -> None:
        pass
    @overload
    def __init__(self) -> None:
        pass
    def __iter__(self) -> iterator:
        pass
    def __len__(self) -> int:
        pass
    @overload
    def __setitem__(self, arg0: slice, arg1: VectorXYZ) -> None:
        pass
    @overload
    def __setitem__(self, arg0: int, arg1: XYZ) -> None:
        pass
    def append(self, x: XYZ) -> None:
        """
Add an item to the end of the list
"""
    def extend(self, L: VectorXYZ) -> None:
        """
Extend the list by appending all the items in the given list
"""
    def insert(self, i: int, x: XYZ) -> None:
        """
Insert an item at a given position.
"""
    @overload
    def pop(self) -> XYZ:
        pass
    @overload
    def pop(self, i: int) -> XYZ:
        pass
    pass
class XYZ():
    def __add__(self, arg0: XYZ) -> XYZ:
        pass
    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        pass
    @overload
    def __init__(self) -> None:
        pass
    def __mul__(self, arg0: float) -> XYZ:
        pass
    def __neg__(self) -> XYZ:
        pass
    def __repr__(self) -> str:
        pass
    def __rmul__(self, arg0: float) -> XYZ:
        pass
    def __str__(self) -> str:
        pass
    def __sub__(self, arg0: XYZ) -> XYZ:
        pass
    def __truediv__(self, arg0: float) -> XYZ:
        pass
    def cross(self, rhs: XYZ) -> XYZ:
        """
Returns cross product
"""
    def dot(self, rhs: XYZ) -> float:
        """
Returns dot product
"""
    def len(self) -> float:
        """
Returns vector length
"""
    def len2(self) -> float:
        """
Returns vector length squared
"""
    @property
    def to_np(self) -> numpy.ndarray:
        pass
    @property
    def x(self) -> float:
        """x coordinate"""
    @x.setter
    def x(self, arg1: float) -> None:
        """x coordinate"""
    @property
    def y(self) -> float:
        """y coordinate"""
    @y.setter
    def y(self, arg1: float) -> None:
        """y coordinate"""
    @property
    def z(self) -> float:
        """z coordinate"""
    @z.setter
    def z(self, arg1: float) -> None:
        """z coordinate"""
    pass
def Degrees(degrees: float) -> AngleValue:
    pass
def Radians(radians: float) -> AngleValue:
    pass
def angle(a: XYZ, b: XYZ, c: XYZ) -> AngleValue:
    """
Calculate angle a-b-c
"""
def calc_alignment(ref: VectorXYZ, var: VectorXYZ) -> Transformation3d:
    pass
def calc_autocorr_order_2(vectors: VectorXYZ, limit: int = -1) -> List[float]:
    """
Calculates vector auto correlation function :math:`C(t)` of second order

.. math::

      C(t) = \frac{4 \pi}{5} \sum_{m=-2}^{m=2} \left\langle Y^{2,m}(\theta(\tau),\phi(\tau)) \overline{Y^{2,m}(\theta(\tau+t),\phi(\tau+t))} \right\rangle_\tau \\
           = \left\langle P_2\left(\cos(\gamma_{\tau,\tau+t})\right) \right\rangle_\tau\\
           = \left\langle \frac{1}{2}\left(3 \cos^2(\gamma_{\tau,\tau+t}) - 1\right) \right\rangle_\tau

:param vectors: list of not normalized vectors
:param limit: strip output to first ``limit`` points. If negative return list size match size of ``vectors``

"""
def calc_geom_center(coords: VectorXYZ) -> XYZ:
    """
Returns mean coordinates
"""
@overload
def calc_rmsd(ref: VectorXYZ, var: VectorXYZ, T: Transformation3d) -> float:
    pass
@overload
def calc_rmsd(ref: VectorXYZ, var: VectorXYZ) -> float:
    pass
def cos(angle: AngleValue) -> float:
    pass
def degrees_to_radians(degrees: float) -> float:
    pass
def dihedral_angle(a: XYZ, b: XYZ, c: XYZ, d: XYZ) -> AngleValue:
    """
Calculate dihedral angle between planes (a,b,c) and (b,c,d)
"""
def distance(a: XYZ, b: XYZ) -> float:
    """
Calculate distance between two points

:param a: first point
:param b: second point

"""
def distance2(a: XYZ, b: XYZ) -> float:
    """
Calculate distance square between two points
"""
def fabs(angle: AngleValue) -> AngleValue:
    pass
def radians_to_degrees(radians: float) -> float:
    pass
def sin(angle: AngleValue) -> float:
    pass
def tan(angle: AngleValue) -> float:
    pass