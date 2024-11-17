from enum import Enum
from typing import Any
from typing import Dict
from typing import List
from typing import Union
import uuid

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_serializer


# Data objects.

class BioMoleculeType(str, Enum):
    PROTEIN: str = "PROTEIN"
    DNA: str = "DNA"
    RNA: str = "RNA"


class BioMoleculeSequenceModification(BaseModel):
    modification_type: str = Field(..., frozen=True)
    position: int = Field(..., frozen=True)


class BioMolecule(BaseModel):
    molecule_type: BioMoleculeType = Field(..., frozen=True)
    sequence: str = Field(..., frozen=True)
    modifications: List[BioMoleculeSequenceModification] = []

    def add_modification(self, modification_type: str, position: int) -> None:
        self.modifications.append(
            BioMoleculeSequenceModification(
                modification_type=modification_type,
                position=position
            )
        )


class Ligand(BaseModel):
    smiles: str = Field(..., frozen=True)


class CovalentBond(BaseModel):
    left_entity: int = Field(..., frozen=True)
    left_position: int = Field(..., frozen=True)
    left_atom: str = Field(..., frozen=True)
    right_entity: int = Field(..., frozen=True)
    right_position: int = Field(..., frozen=True)
    right_atom: str = Field(..., frozen=True)


class Assembly(BaseModel):
    sequences: List[Union[BioMolecule, Ligand]] = Field(..., frozen=True)
    covalent_bonds: List[CovalentBond] = Field(..., frozen=True)


class AF3PredictionRequest(BaseModel):
    assembly: Assembly = Field(..., frozen=True)
    use_msa: bool = Field(default=False, frozen=True)
    atom_confidence: bool = Field(default=False, frozen=True)
    n_samples: int = Field(default=5, frozen=True)
    n_diffusion_steps: int = Field(default=200, frozen=True)
    n_cycles: int = Field(default=10, frozen=True)



# Adapters.



