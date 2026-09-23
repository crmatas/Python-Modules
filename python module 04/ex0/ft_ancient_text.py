#! /usr/bin/env python3
import sys
from typing import IO


def archive_process(archive_name: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file {archive_name}")

    try:
        archive: IO[str] = open(archive_name, 'r', encoding='utf-8')
        print("---")
        content: str = archive.read()
        print(content)
        print("---")
        archive.close()
        print(f"File '{archive_name}' closed.")
    except Exception as e:
        print(f"Error opening file '{archive_name}': {e}")


def main() -> None:

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    archive_name = sys.argv[1]
    archive_process(archive_name)


if __name__ == "__main__":
    main()
