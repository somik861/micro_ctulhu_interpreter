from src.common import Operation, Program, ProgramState


def interpret(program: Program, init_state: ProgramState | None = None) -> ProgramState:
    if init_state is None:
        init_state = ProgramState()
    state = init_state  # just rename for more readability

    for instruction in program:
        ops = instruction.operands
        match instruction.operation:
            case Operation.Move:
                state.stacks[ops[1]].append(state.stacks[ops[0]].pop())
            case Operation.Create:
                state.stacks[ops[1]].append(ops[0])
            case Operation.Add:
                state.stacks[ops[2]].append(
                    state.stacks[ops[0]].pop() + state.stacks[ops[1]].pop()
                )
            case Operation.Drop:
                state.stacks[ops[0]].pop()
            case _:
                assert False

    return state