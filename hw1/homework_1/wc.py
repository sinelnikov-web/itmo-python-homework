import sys

__all__ = ["wc"]


def wc(filename: str | None = None):
    counts = {"lines": 0, "words": 0, "bytes": 0}

    with open(filename, "r") if filename else sys.stdin as f:
        for line in f.readlines():
            counts["lines"] += 1
            counts["words"] += len(line.split())
            counts["bytes"] += len(line.encode("utf-8"))

    return counts
