#! /usr/bin/env python3

def secure_archive(
        filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                content = file.read()
                return (True, content)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
    except FileNotFoundError as error:
        return (False, str(error))
    except PermissionError as error:
        return (False, str(error))
    return (False, "Error happened")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print("")
    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file")
    print(result)
    print("")
    print("Using 'secure_archive' to read from a inaccessible file:")
    result = secure_archive("/etc/master.passwd")
    print(result)
    print("")
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print("")
    print("Using 'secure_archive' to write previous content:")
    result = secure_archive("archive_copy.txt", "write", result[1])
    print(result)
