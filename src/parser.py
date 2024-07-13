from src.common import Instruction, Operation, Program
from pathlib import Path


def parse_file(path: Path) -> Program:
    return parser_source_lines(open(path, 'r', encoding='utf-8').readlines())


def parser_source_lines(source_lines: list[str]) -> Program:
    instructions: list[Instruction] = []

    for line in source_lines:
        line = line.strip()
        if line == '':
            continue
        parts = line.split()
        instr = Instruction(Operation(parts[0]))
        for part in parts[1:]:
            try:
                instr.operands.append(int(part))
            except ValueError:
                pass

        instructions.append(instr)

    return instructions
