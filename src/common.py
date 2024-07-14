from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin
from enum import Enum


class Operation(Enum):
    Move = 'move'
    Create = 'create'
    Add = 'add'
    Drop = 'drop'
    Dup = 'dup'


@dataclass
class Instruction(DataClassJsonMixin):
    operation: Operation
    operands: list[int] = field(default_factory=list)


Program = list[Instruction]


@dataclass
class ProgramState(DataClassJsonMixin):
    stacks: dict[int, list[int]] = field(default_factory=dict)

    def __post_init__(self):
        for i in range(6):
            self.stacks[i] = []
