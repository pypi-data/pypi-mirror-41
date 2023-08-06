"""pyxmolpp2.polymer module"""
from typing import *
from typing import Iterable as iterable
from typing import Iterator as iterator
import pyxmolpp2.geometry
import pyxmolpp2.pdb
__all__  = [
"Atom",
"AtomIdPredicateGenerator",
"AtomName",
"AtomNamePredicateGenerator",
"AtomPredicate",
"AtomSelection",
"AtomSelectionRange",
"Chain",
"ChainIndexPredicateGenerator",
"ChainName",
"ChainNamePredicateGenerator",
"ChainPredicate",
"ChainSelection",
"ChainSelectionRange",
"DeadAtomSelectionAccess",
"DeadChainSelectionAccess",
"DeadResidueSelectionAccess",
"DeletedAtomAccess",
"DeletedChainAccess",
"DeletedResidueAccess",
"Frame",
"OutOfRangeAtomSelection",
"OutOfRangeChain",
"OutOfRangeChainSelection",
"OutOfRangeFrame",
"OutOfRangeResidue",
"OutOfRangeResidueSelection",
"Residue",
"ResidueId",
"ResidueIdPredicateGenerator",
"ResidueInsertionCode",
"ResidueName",
"ResidueNamePredicateGenerator",
"ResiduePredicate",
"ResidueSelection",
"ResidueSelectionRange",
"TorsionAngle",
"TorsionAngleFactory",
"TorsionAngleName",
"aId",
"aName",
"cIndex",
"cName",
"rId",
"rName"
]
class Atom():
    def __eq__(self, arg0: Atom) -> bool:
        pass
    def __repr__(self) -> str:
        pass
    def delete(self) -> None:
        """
Mark atom as deleted. Further access to deleted atom is illegal.
"""
    @property
    def aId(self) -> int:
        """Atom id"""
    @property
    def aName(self) -> AtomName:
        """Atom name"""
    @property
    def cIndex(self) -> int:
        """Chain index"""
    @property
    def cName(self) -> ChainName:
        """Chain name (chainID in PDB nomenclature)"""
    @property
    def chain(self) -> Chain:
        """Parent chain"""
    @property
    def fIndex(self) -> int:
        """Frame index"""
    @property
    def frame(self) -> Frame:
        """Parent frame"""
    @property
    def id(self) -> int:
        """Atom id"""
    @property
    def name(self) -> AtomName:
        """Atom name"""
    @name.setter
    def name(self, arg1: AtomName) -> None:
        """Atom name"""
    @property
    def r(self) -> pyxmolpp2.geometry.XYZ:
        """Atom coordinates"""
    @r.setter
    def r(self, arg1: pyxmolpp2.geometry.XYZ) -> None:
        """Atom coordinates"""
    @property
    def rId(self) -> ResidueId:
        """Residue id"""
    @property
    def rName(self) -> ResidueName:
        """Residue name"""
    @property
    def residue(self) -> Residue:
        """Parent residue, guarantied to be not None"""
    pass
class AtomIdPredicateGenerator():
    def __eq__(self, arg0: int) -> AtomPredicate:
        pass
    def __ge__(self, arg0: int) -> AtomPredicate:
        pass
    def __gt__(self, arg0: int) -> AtomPredicate:
        pass
    def __le__(self, arg0: int) -> AtomPredicate:
        pass
    def __lt__(self, arg0: int) -> AtomPredicate:
        pass
    def __ne__(self, arg0: int) -> AtomPredicate:
        pass
    def is_in(self, arg0: Set[int]) -> AtomPredicate:
        pass
    pass
class AtomName():
    def __eq__(self, arg0: AtomName) -> bool:
        pass
    def __hash__(self) -> int:
        pass
    def __init__(self, name: str) -> None:
        pass
    def __ne__(self, arg0: AtomName) -> bool:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def str(self) -> str:
        pass
    pass
class AtomNamePredicateGenerator():
    @overload
    def __eq__(self, arg0: AtomName) -> AtomPredicate:
        pass
    @overload
    def __eq__(self, arg0: str) -> AtomPredicate:
        pass
    @overload
    def __ne__(self, arg0: AtomName) -> AtomPredicate:
        pass
    @overload
    def __ne__(self, arg0: str) -> AtomPredicate:
        pass
    @overload
    def is_in(self, arg0: Set[AtomName]) -> AtomPredicate:
        pass
    @overload
    def is_in(self, arg0: Set[str]) -> AtomPredicate:
        pass
    pass
class AtomPredicate():
    @overload
    def __and__(self, arg0: ChainPredicate) -> AtomPredicate:
        pass
    @overload
    def __and__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __and__(self, arg0: ResiduePredicate) -> AtomPredicate:
        pass
    def __call__(self, arg0: Atom) -> bool:
        pass
    def __init__(self, arg0: Callable[[Atom], bool]) -> None:
        pass
    def __invert__(self) -> AtomPredicate:
        pass
    @overload
    def __or__(self, arg0: ChainPredicate) -> AtomPredicate:
        pass
    @overload
    def __or__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __or__(self, arg0: ResiduePredicate) -> AtomPredicate:
        pass
    def __ror__(self, arg0: ChainPredicate) -> AtomPredicate:
        pass
    @overload
    def __xor__(self, arg0: ResiduePredicate) -> AtomPredicate:
        pass
    @overload
    def __xor__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    pass
class AtomSelection():
    def __add__(self, arg0: AtomSelection) -> AtomSelection:
        pass
    @overload
    def __getitem__(self, n: int) -> Atom:
        pass
    @overload
    def __getitem__(self, slice: slice) -> AtomSelection:
        pass
    def __iadd__(self, arg0: AtomSelection) -> AtomSelection:
        pass
    def __imul__(self, arg0: AtomSelection) -> AtomSelection:
        pass
    def __isub__(self, arg0: AtomSelection) -> AtomSelection:
        pass
    def __iter__(self) -> AtomSelectionRange:
        pass
    def __len__(self) -> int:
        """
Returns number of elements
"""
    def __mul__(self, arg0: AtomSelection) -> AtomSelection:
        pass
    def __repr__(self) -> str:
        pass
    def __sub__(self, arg0: AtomSelection) -> AtomSelection:
        pass
    def filter(self, predicate: Callable[[Atom], bool]) -> AtomSelection:
        """
Keeps in selection only elements that match predicate
"""
    def for_each(self, transformation: Callable[[Atom], None]) -> AtomSelection:
        pass
    @overload
    def transform(self, transformation: pyxmolpp2.geometry.UniformScale3d) -> AtomSelection:
        pass
    @overload
    def transform(self, transformation: pyxmolpp2.geometry.Translation3d) -> AtomSelection:
        pass
    @overload
    def transform(self, transformation: pyxmolpp2.geometry.Transformation3d) -> AtomSelection:
        pass
    @overload
    def transform(self, transformation: pyxmolpp2.geometry.Rotation3d) -> AtomSelection:
        pass
    @property
    def asChains(self) -> ChainSelection:
        """Returns selection of parent chains"""
    @property
    def asResidues(self) -> ResidueSelection:
        """Returns selection of parent residues"""
    @property
    def size(self) -> int:
        """Returns number of elements"""
    @property
    def toCoords(self) -> pyxmolpp2.geometry.VectorXYZ:
        """Returns copy of atom coordinates"""
    pass
class AtomSelectionRange():
    def __next__(self) -> Atom:
        pass
    pass
class Chain():
    def __eq__(self, arg0: Chain) -> bool:
        pass
    @overload
    def __getitem__(self, arg0: ResidueId) -> Residue:
        pass
    @overload
    def __getitem__(self, arg0: int) -> Residue:
        pass
    def __len__(self) -> int:
        """
Returns number of residues in chain
"""
    def __repr__(self) -> str:
        pass
    def delete(self) -> None:
        """
Marks chain as deleted. Further access to deleted chain is illegal
"""
    @overload
    def emplace(self, residue: Residue) -> Residue:
        pass
    @overload
    def emplace(self, name: ResidueName, id: ResidueId, reserve: int = 0) -> Residue:
        pass
    @property
    def asAtoms(self) -> AtomSelection:
        """Returns selection of child atoms"""
    @property
    def asResidues(self) -> ResidueSelection:
        """Returns selection of child residues"""
    @property
    def cIndex(self) -> int:
        """Chain index, starts from 0"""
    @property
    def cName(self) -> ChainName:
        """Chain name (chainID in PDB nomenclature)"""
    @property
    def fIndex(self) -> int:
        """Frame index"""
    @property
    def frame(self) -> Frame:
        """Parent frame"""
    @property
    def index(self) -> int:
        """Chain index, starts from 0"""
    @property
    def name(self) -> ChainName:
        """Chain name (chainID in PDB nomenclature)"""
    @name.setter
    def name(self, arg1: ChainName) -> None:
        """Chain name (chainID in PDB nomenclature)"""
    @property
    def size(self) -> int:
        """Returns number of residues in chain"""
    pass
class ChainIndexPredicateGenerator():
    def __eq__(self, arg0: int) -> ChainPredicate:
        pass
    def __ge__(self, arg0: int) -> ChainPredicate:
        pass
    def __gt__(self, arg0: int) -> ChainPredicate:
        pass
    def __le__(self, arg0: int) -> ChainPredicate:
        pass
    def __lt__(self, arg0: int) -> ChainPredicate:
        pass
    def __ne__(self, arg0: int) -> ChainPredicate:
        pass
    def is_in(self, arg0: Set[int]) -> ChainPredicate:
        pass
    pass
class ChainName():
    def __eq__(self, arg0: ChainName) -> bool:
        pass
    def __hash__(self) -> int:
        pass
    def __init__(self, name: str) -> None:
        pass
    def __ne__(self, arg0: ChainName) -> bool:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def str(self) -> str:
        pass
    pass
class ChainNamePredicateGenerator():
    @overload
    def __eq__(self, arg0: ChainName) -> ChainPredicate:
        pass
    @overload
    def __eq__(self, arg0: str) -> ChainPredicate:
        pass
    @overload
    def __ne__(self, arg0: str) -> ChainPredicate:
        pass
    @overload
    def __ne__(self, arg0: ChainName) -> ChainPredicate:
        pass
    @overload
    def is_in(self, arg0: Set[ChainName]) -> ChainPredicate:
        pass
    @overload
    def is_in(self, arg0: Set[str]) -> ChainPredicate:
        pass
    pass
class ChainPredicate():
    @overload
    def __and__(self, arg0: ResiduePredicate) -> ResiduePredicate:
        pass
    @overload
    def __and__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __and__(self, arg0: ChainPredicate) -> ChainPredicate:
        pass
    @overload
    def __call__(self, arg0: Residue) -> bool:
        pass
    @overload
    def __call__(self, arg0: Chain) -> bool:
        pass
    @overload
    def __call__(self, arg0: Atom) -> bool:
        pass
    def __init__(self, arg0: Callable[[Chain], bool]) -> None:
        pass
    def __invert__(self) -> ChainPredicate:
        pass
    @overload
    def __or__(self, arg0: ResiduePredicate) -> ResiduePredicate:
        pass
    @overload
    def __or__(self, arg0: ChainPredicate) -> ChainPredicate:
        pass
    @overload
    def __or__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __xor__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __xor__(self, arg0: ChainPredicate) -> ChainPredicate:
        pass
    @overload
    def __xor__(self, arg0: ResiduePredicate) -> ResiduePredicate:
        pass
    pass
class ChainSelection():
    def __add__(self, arg0: ChainSelection) -> ChainSelection:
        pass
    @overload
    def __getitem__(self, n: int) -> Chain:
        pass
    @overload
    def __getitem__(self, slice: slice) -> ChainSelection:
        pass
    def __iadd__(self, arg0: ChainSelection) -> ChainSelection:
        pass
    def __imul__(self, arg0: ChainSelection) -> ChainSelection:
        pass
    def __isub__(self, arg0: ChainSelection) -> ChainSelection:
        pass
    def __iter__(self) -> ChainSelectionRange:
        pass
    def __len__(self) -> int:
        pass
    def __mul__(self, arg0: ChainSelection) -> ChainSelection:
        pass
    def __repr__(self) -> str:
        pass
    def __sub__(self, arg0: ChainSelection) -> ChainSelection:
        pass
    def filter(self, predicate: Callable[[Chain], bool]) -> ChainSelection:
        """
Keeps in selection only elements that match predicate
"""
    def for_each(self, transformation: Callable[[Chain], None]) -> ChainSelection:
        pass
    @property
    def asAtoms(self) -> AtomSelection:
        """Returns selection of child chains"""
    @property
    def asResidues(self) -> ResidueSelection:
        """Returns selection of child residues"""
    @property
    def size(self) -> int:
        pass
    pass
class ChainSelectionRange():
    def __next__(self) -> Chain:
        pass
    pass
class DeadAtomSelectionAccess(Exception, BaseException):
    pass
class DeadChainSelectionAccess(Exception, BaseException):
    pass
class DeadResidueSelectionAccess(Exception, BaseException):
    pass
class DeletedAtomAccess(Exception, BaseException):
    pass
class DeletedChainAccess(Exception, BaseException):
    pass
class DeletedResidueAccess(Exception, BaseException):
    pass
class Frame():
    def __getitem__(self, arg0: ChainName) -> Chain:
        pass
    def __init__(self, frame_index: int) -> None:
        pass
    def __len__(self) -> int:
        """
Returns number of chains
"""
    def __repr__(self) -> str:
        pass
    def copy(self) -> Frame:
        pass
    @overload
    def emplace(self, index: ChainName, reserve: int = 0) -> Chain:
        pass
    @overload
    def emplace(self, chain: Chain) -> Chain:
        pass
    @overload
    def to_pdb(self, output_filename: str) -> None:
        pass
    @overload
    def to_pdb(self, output_filename: str, db: pyxmolpp2.pdb.basic_PdbRecords) -> None:
        pass
    @property
    def asAtoms(self) -> AtomSelection:
        """Returns selection of child atoms"""
    @property
    def asChains(self) -> ChainSelection:
        """Returns selection of child chains"""
    @property
    def asResidues(self) -> ResidueSelection:
        """Returns selection of child residues"""
    @property
    def index(self) -> int:
        """Frame index"""
    @property
    def size(self) -> int:
        """Number of chains"""
    pass
class OutOfRangeAtomSelection(Exception, BaseException):
    pass
class OutOfRangeChain(Exception, BaseException):
    pass
class OutOfRangeChainSelection(Exception, BaseException):
    pass
class OutOfRangeFrame(Exception, BaseException):
    pass
class OutOfRangeResidue(Exception, BaseException):
    pass
class OutOfRangeResidueSelection(Exception, BaseException):
    pass
class Residue():
    def __eq__(self, arg0: Residue) -> bool:
        pass
    def __getitem__(self, arg0: AtomName) -> Atom:
        """
Returns first atom in residue with given name. If no atoms with such name exception raised.
"""
    def __len__(self) -> int:
        """
Returns number of atoms in residues
"""
    def __repr__(self) -> str:
        pass
    def delete(self) -> None:
        """
Marks residue as deleted. Further access to deleted residue is illegal
"""
    @overload
    def emplace(self, atom: Atom) -> Atom:
        pass
    @overload
    def emplace(self, name: AtomName, id: int, r: pyxmolpp2.geometry.XYZ) -> Atom:
        pass
    @property
    def asAtoms(self) -> AtomSelection:
        """Returns selection of child atoms"""
    @property
    def cIndex(self) -> int:
        """Chain index"""
    @property
    def cName(self) -> ChainName:
        """Chain name (chainID in PDB nomenclature)"""
    @property
    def chain(self) -> Chain:
        pass
    @property
    def fIndex(self) -> int:
        """Frame index"""
    @property
    def frame(self) -> Frame:
        """Parent frame"""
    @property
    def id(self) -> ResidueId:
        """Residue id"""
    @id.setter
    def id(self, arg1: ResidueId) -> None:
        """Residue id"""
    @property
    def name(self) -> ResidueName:
        """Residue name"""
    @name.setter
    def name(self, arg1: ResidueName) -> None:
        """Residue name"""
    @property
    def rId(self) -> ResidueId:
        """Residue id"""
    @property
    def rName(self) -> ResidueName:
        """Residue name"""
    @property
    def size(self) -> int:
        """Returns number of atoms in residues"""
    pass
class ResidueId():
    @overload
    def __eq__(self, arg0: ResidueId) -> bool:
        pass
    @overload
    def __eq__(self, arg0: int) -> bool:
        pass
    @overload
    def __ge__(self, arg0: int) -> bool:
        pass
    @overload
    def __ge__(self, arg0: ResidueId) -> bool:
        pass
    @overload
    def __gt__(self, arg0: ResidueId) -> bool:
        pass
    @overload
    def __gt__(self, arg0: int) -> bool:
        pass
    def __hash__(self) -> int:
        pass
    @overload
    def __init__(self, arg0: int, arg1: ResidueInsertionCode) -> None:
        pass
    @overload
    def __init__(self, arg0: int) -> None:
        pass
    @overload
    def __init__(self) -> None:
        pass
    @overload
    def __le__(self, arg0: ResidueId) -> bool:
        pass
    @overload
    def __le__(self, arg0: int) -> bool:
        pass
    @overload
    def __lt__(self, arg0: int) -> bool:
        pass
    @overload
    def __lt__(self, arg0: ResidueId) -> bool:
        pass
    @overload
    def __ne__(self, arg0: int) -> bool:
        pass
    @overload
    def __ne__(self, arg0: ResidueId) -> bool:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def iCode(self) -> ResidueInsertionCode:
        pass
    @iCode.setter
    def iCode(self, arg0: ResidueInsertionCode) -> None:
        pass
    @property
    def serial(self) -> int:
        pass
    @serial.setter
    def serial(self, arg0: int) -> None:
        pass
    pass
class ResidueIdPredicateGenerator():
    @overload
    def __eq__(self, arg0: ResidueId) -> ResiduePredicate:
        pass
    @overload
    def __eq__(self, arg0: int) -> ResiduePredicate:
        pass
    @overload
    def __ge__(self, arg0: int) -> ResiduePredicate:
        pass
    @overload
    def __ge__(self, arg0: ResidueId) -> ResiduePredicate:
        pass
    @overload
    def __gt__(self, arg0: int) -> ResiduePredicate:
        pass
    @overload
    def __gt__(self, arg0: ResidueId) -> ResiduePredicate:
        pass
    @overload
    def __le__(self, arg0: int) -> ResiduePredicate:
        pass
    @overload
    def __le__(self, arg0: ResidueId) -> ResiduePredicate:
        pass
    @overload
    def __lt__(self, arg0: ResidueId) -> ResiduePredicate:
        pass
    @overload
    def __lt__(self, arg0: int) -> ResiduePredicate:
        pass
    @overload
    def __ne__(self, arg0: ResidueId) -> ResiduePredicate:
        pass
    @overload
    def __ne__(self, arg0: int) -> ResiduePredicate:
        pass
    @overload
    def is_in(self, arg0: Set[ResidueId]) -> ResiduePredicate:
        pass
    @overload
    def is_in(self, arg0: Set[int]) -> ResiduePredicate:
        pass
    pass
class ResidueInsertionCode():
    def __hash__(self) -> int:
        pass
    def __init__(self, arg0: str) -> None:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def str(self) -> str:
        pass
    pass
class ResidueName():
    def __eq__(self, arg0: ResidueName) -> bool:
        pass
    def __hash__(self) -> int:
        pass
    def __init__(self, name: str) -> None:
        pass
    def __ne__(self, arg0: ResidueName) -> bool:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def str(self) -> str:
        pass
    pass
class ResidueNamePredicateGenerator():
    @overload
    def __eq__(self, arg0: ResidueName) -> ResiduePredicate:
        pass
    @overload
    def __eq__(self, arg0: str) -> ResiduePredicate:
        pass
    @overload
    def __ne__(self, arg0: ResidueName) -> ResiduePredicate:
        pass
    @overload
    def __ne__(self, arg0: str) -> ResiduePredicate:
        pass
    @overload
    def is_in(self, arg0: Set[str]) -> ResiduePredicate:
        pass
    @overload
    def is_in(self, arg0: Set[ResidueName]) -> ResiduePredicate:
        pass
    pass
class ResiduePredicate():
    @overload
    def __and__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __and__(self, arg0: ChainPredicate) -> ResiduePredicate:
        pass
    @overload
    def __and__(self, arg0: ResiduePredicate) -> ResiduePredicate:
        pass
    @overload
    def __call__(self, arg0: Residue) -> bool:
        pass
    @overload
    def __call__(self, arg0: Atom) -> bool:
        pass
    def __init__(self, arg0: Callable[[Residue], bool]) -> None:
        pass
    def __invert__(self) -> ResiduePredicate:
        pass
    @overload
    def __or__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    @overload
    def __or__(self, arg0: ChainPredicate) -> ResiduePredicate:
        pass
    @overload
    def __or__(self, arg0: ResiduePredicate) -> ResiduePredicate:
        pass
    @overload
    def __xor__(self, arg0: ChainPredicate) -> ResiduePredicate:
        pass
    @overload
    def __xor__(self, arg0: ResiduePredicate) -> ResiduePredicate:
        pass
    @overload
    def __xor__(self, arg0: AtomPredicate) -> AtomPredicate:
        pass
    pass
class ResidueSelection():
    def __add__(self, arg0: ResidueSelection) -> ResidueSelection:
        pass
    @overload
    def __getitem__(self, n: int) -> Residue:
        pass
    @overload
    def __getitem__(self, slice: slice) -> ResidueSelection:
        pass
    def __iadd__(self, arg0: ResidueSelection) -> ResidueSelection:
        pass
    def __imul__(self, arg0: ResidueSelection) -> ResidueSelection:
        pass
    def __isub__(self, arg0: ResidueSelection) -> ResidueSelection:
        pass
    def __iter__(self) -> ResidueSelectionRange:
        pass
    def __len__(self) -> int:
        """
Returns number of elements
"""
    def __mul__(self, arg0: ResidueSelection) -> ResidueSelection:
        pass
    def __repr__(self) -> str:
        pass
    def __sub__(self, arg0: ResidueSelection) -> ResidueSelection:
        pass
    def filter(self, predicate: Callable[[Residue], bool]) -> ResidueSelection:
        """
Keeps in selection only elements that match predicate
"""
    def for_each(self, transformation: Callable[[Residue], None]) -> ResidueSelection:
        pass
    @property
    def asAtoms(self) -> AtomSelection:
        """Returns selection of child atoms"""
    @property
    def asChains(self) -> ChainSelection:
        """Returns selection of parent chains"""
    @property
    def size(self) -> int:
        """Returns number of elements"""
    pass
class ResidueSelectionRange():
    def __next__(self) -> Residue:
        pass
    pass
class TorsionAngle():
    @overload
    def __init__(self, a: Atom, b: Atom, c: Atom, d: Atom, affected_atoms_selector: Callable[[Atom, Atom, Atom, Atom], AtomSelection]) -> None:
        pass
    @overload
    def __init__(self) -> None:
        pass
    @overload
    def __init__(self, a: Atom, b: Atom, c: Atom, d: Atom) -> None:
        pass
    def set(self, value: pyxmolpp2.geometry.AngleValue, noop_tolerance: pyxmolpp2.geometry.AngleValue) -> None:
        """
Perform rotation around torsion angle, all dependent atoms are also rotated.

Precondition:
   Must be constructed with `affected_atoms_selector` argument

:param value: target value of torsion angle
:param noop_tolerance: if current angle is close enough to target `value` rotation is not performed, default=`Degrees(0.01)`

"""
    def value(self) -> pyxmolpp2.geometry.AngleValue:
        """
Get current value
"""
    pass
class TorsionAngleFactory():
    @staticmethod
    def chi1(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def chi2(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def chi3(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def chi4(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def chi5(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def get(residue: Residue, torsion_name: TorsionAngleName) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def omega(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def phi(residue: Residue) -> Optional[TorsionAngle]:
        pass
    @staticmethod
    def psi(residue: Residue) -> Optional[TorsionAngle]:
        pass
    pass
class TorsionAngleName():
    def __hash__(self) -> int:
        pass
    def __init__(self, name: str) -> None:
        pass
    def __repr__(self) -> str:
        pass
    def __str__(self) -> str:
        pass
    @property
    def str(self) -> str:
        pass
    pass
aId = None # type: pyxmolpp2.polymer.AtomIdPredicateGenerator # value = <pyxmolpp2.polymer.AtomIdPredicateGenerator object at 0x7f2f0eacac70>
aName = None # type: pyxmolpp2.polymer.AtomNamePredicateGenerator # value = <pyxmolpp2.polymer.AtomNamePredicateGenerator object at 0x7f2f0eacabc8>
cIndex = None # type: pyxmolpp2.polymer.ChainIndexPredicateGenerator # value = <pyxmolpp2.polymer.ChainIndexPredicateGenerator object at 0x7f2f0eacace0>
cName = None # type: pyxmolpp2.polymer.ChainNamePredicateGenerator # value = <pyxmolpp2.polymer.ChainNamePredicateGenerator object at 0x7f2f0eacac38>
rId = None # type: pyxmolpp2.polymer.ResidueIdPredicateGenerator # value = <pyxmolpp2.polymer.ResidueIdPredicateGenerator object at 0x7f2f0eacaca8>
rName = None # type: pyxmolpp2.polymer.ResidueNamePredicateGenerator # value = <pyxmolpp2.polymer.ResidueNamePredicateGenerator object at 0x7f2f0eacac00>