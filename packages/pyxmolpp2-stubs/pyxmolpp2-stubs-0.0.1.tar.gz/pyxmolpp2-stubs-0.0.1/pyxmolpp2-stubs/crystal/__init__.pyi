"""pyxmolpp2.crystal module"""
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
import pyxmolpp2.geometry
__all__  = [
"BestShiftFinder",
"LatticeVectors"
]
class BestShiftFinder():
    def __init__(self, lattice_vectors: LatticeVectors) -> None:
        pass
    def find_best_shift(self, ref: pyxmolpp2.geometry.XYZ, var: pyxmolpp2.geometry.XYZ) -> Tuple[float, pyxmolpp2.geometry.XYZ]:
        pass
    def scale_lattice_by(self, factor: float) -> None:
        pass
    pass
class LatticeVectors():
    def __getitem__(self, i: int) -> pyxmolpp2.geometry.XYZ:
        pass
    @overload
    def __init__(self, v1: pyxmolpp2.geometry.XYZ, v2: pyxmolpp2.geometry.XYZ, v3: pyxmolpp2.geometry.XYZ) -> None:
        pass
    @overload
    def __init__(self, a: float, b: float, c: float, alpha: pyxmolpp2.geometry.AngleValue, beta: pyxmolpp2.geometry.AngleValue, gamma: pyxmolpp2.geometry.AngleValue) -> None:
        pass
    def get_shift(self, i: int, j: int, k: int) -> pyxmolpp2.geometry.XYZ:
        pass
    def scale_by(self, factor: float) -> None:
        pass
    def translate(self, r: pyxmolpp2.geometry.XYZ, i: int, j: int, k: int) -> pyxmolpp2.geometry.XYZ:
        pass
    pass