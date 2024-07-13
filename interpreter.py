from argparse import ArgumentParser
import sys
from pathlib import Path
from src.parser import parse_file
from src.engine import interpret

def main() -> int:
    parser = ArgumentParser()
    parser.add_argument('source', type=Path, help='path to micro-ctulhu source code')

    args = parser.parse_args()
    
    program = parse_file(args.source)
    result = interpret(program)

    for k, v in result.stacks:
        print(f'{k}: |{' '.join(v)}>')

    return 0


if __name__ == '__main__':
    sys.exit(main())
