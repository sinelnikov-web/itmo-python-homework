import subprocess

FILENAMES = [
    "./tests/data/a.txt",
    "./tests/data/b.txt",
    "./tests/data/c.txt",
]


def capture(command: list[str]):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode
