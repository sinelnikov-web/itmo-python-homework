__all__ = ["tail"]


def tail(filename: str, n: int = 10):
    with open(filename, "rb") as f:
        f.seek(0, 2)
        filesize = f.tell()

        lines: list[str] = []
        end_position = filesize
        while len(lines) <= n and end_position > 0:
            buffer_size = min(1024, end_position)
            f.seek(end_position - buffer_size, 0)
            buffer = f.read(buffer_size)
            lines.extend(buffer.decode("utf-8", errors="ignore").splitlines()[::-1])
            end_position -= buffer_size

        return lines[:n][::-1]
