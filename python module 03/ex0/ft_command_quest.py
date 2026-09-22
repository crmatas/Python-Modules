#! /usr/bin/env python3
import sys
program_mame = sys.argv[0]
received_argv = len(sys.argv) - 1
total_argument = len(sys.argv)


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {program_mame}")
    print(f"Argument received: {received_argv}")
    position = 1
    for argument in sys.argv[1:]:
        print(f"Argument {position}: {argument}")
        position = position + 1
    print(f"Total arguments: {total_argument}")


if __name__ == "__main__":
    main()
