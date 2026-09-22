#! /usr/bin/env python3
import sys
from typing import IO


def main() -> None:

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    archive_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{archive_name}'")
    try:
        archive: IO[str] = open(archive_name, 'r', encoding='utf-8')
        print("---")
        print("")
        content: str = archive.read()
        print(content, end="")
        print("")
        print("---")
        archive.close()
        print(f"File '{archive_name}' closed.")
        print("")
    except Exception as e:
        print(f"[STDERR] Error opening file '{archive_name}'"
              f": {e}", file=sys.stderr)
        sys.exit(1)
    print("Transform data:")
    print("---")
    try:
        archive = open(archive_name, 'r', encoding='utf-8')
        transform_content: str = ""
        for line in archive:
            line_clean = line.rstrip('\n')
            line_modified = f"{line_clean}#\n"
            transform_content += line_modified
            print(line_modified, end="")
        archive.close()
    except Exception as e:
        print(f"[STDERR] Error transforming file '{archive_name}'"
              f": {e}", file=sys.stderr)
        sys.exit(1)
    print("---")
    # capture the name of the archive.
    print("Enter new file name (or empty): ", end="")
    # flush, ensure the promp is displayed before reading input.
    sys.stdout.flush()
    new_name: str = sys.stdin.readline().rstrip('\n')
    if new_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_name}'.")
        try:
            new_archive: IO[str] = open(new_name, 'w', encoding='utf-8')
            new_archive.write(transform_content)
            new_archive.close()
            print(f"Data saved in file '{new_name}'.")
        except Exception as e:
            print(f"[STDERR] Error opening file '{new_name}'"
                  f": {e}", file=sys.stderr)
            print("Data not saved.")
            sys.exit(1)


if __name__ == "__main__":
    main()
