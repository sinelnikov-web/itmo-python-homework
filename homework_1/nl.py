__all__ = ["nl"]


def nl(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            yield index + 1, line
