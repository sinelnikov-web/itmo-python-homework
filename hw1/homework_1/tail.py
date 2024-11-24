import sys

__all__ = ["tail"]


def tail(filename: str | None, n: int = 10):
    if filename is None:
        n = 17

    with open(filename, "rb") if filename else sys.stdin as f:
        f.seek(0, 2)
        filesize = f.tell()
        lines: list[str] = []
        end_position = filesize
        while len(lines) <= n and (not filename or end_position > 0):
            buffer_size = min(1024, end_position)
            f.seek(end_position - buffer_size, 0)
            buffer = f.read(buffer_size)
            lines.extend(buffer.decode("utf-8", errors="ignore").splitlines()[::-1])
            end_position -= buffer_size

        return lines[:n][::-1]

def tail(filename: str | None = None):
    num_lines_file = 10
    num_lines_stdin = 17

    if not filename:
        lines = sys.stdin.readlines()
        return lines[-num_lines_stdin:]
    else:
        try:
            with open(filename, 'rb') as f:
                f.seek(0, 2)
                filesize = f.tell()
                lines: list[str] = []
                end_position = filesize
                while len(lines) <= num_lines_file and (not filename or end_position > 0):
                    buffer_size = min(1024, end_position)
                    f.seek(end_position - buffer_size, 0)
                    buffer = f.read(buffer_size)
                    lines.extend(buffer.decode("utf-8", errors="ignore").splitlines()[::-1])
                    end_position -= buffer_size

                return lines[:num_lines_file][::-1]
        except FileNotFoundError:
            print(f"tail: cannot open '{filename}' for reading: No such file or directory")
        except IOError as e:
            print(f"tail: error reading '{filename}': {e}")

