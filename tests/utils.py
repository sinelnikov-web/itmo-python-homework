import subprocess

FILENAMES = [
    "./tests/data/a.txt",
    "./tests/data/b.txt",
    "./tests/data/c.txt",
]


def capture(command: list[str], data: bytes | None = None):
    proc = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
    )
    out, err = proc.communicate(data)
    return out, err, proc.returncode
