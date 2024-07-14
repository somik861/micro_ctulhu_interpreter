from argparse import ArgumentParser
import sys
from pathlib import Path
from src.parser import parse_file
from src.engine import interpret
from src.common import ProgramState


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument('source', type=Path,
                        help='path to micro-ctulhu source code')
    parser.add_argument('--save_result', type=Path,
                        required=False, help='Save result state to json file')
    parser.add_argument('--init_state', type=Path, required=False,
                        help='Load initial state from json file')

    args = parser.parse_args()

    state: ProgramState | None = None
    if args.init_state is not None:
        state = ProgramState.from_json(
            open(args.init_state, 'r', encoding='utf-8'))

    program = parse_file(args.source)
    result = interpret(program, state)

    if args.save_result is not None:
        open(args.save_result, 'w', encoding='utf-8').write(result.to_json(indent=4))

    for k, v in result.stacks.items():
        print(f'{k}: |{' '.join(map(lambda x: str(x), v))}>')

    return 0


if __name__ == '__main__':
    sys.exit(main())
