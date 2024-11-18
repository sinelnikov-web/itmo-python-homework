import sys

__all__ = ["nl"]


def nl(filename: str):
    with open(filename, "r") if filename else sys.stdin as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            yield index + 1, line
