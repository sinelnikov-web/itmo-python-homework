__all__ = ["wc"]


def wc(filename: str):
    counts = {"lines": 0, "words": 0, "bytes": 0}

    with open(filename, "rb") as f:
        for line in f:
            counts["lines"] += 1
            line = line.decode("utf-8", errors="ignore")
            counts["words"] += len(line.split())
            counts["bytes"] += len(line.encode("utf-8"))

    return counts
