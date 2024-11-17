import os
import sys
import click

from nl import nl
from wc import wc
from tail import tail


@click.group("cli")
def cli():
    pass


@click.command("nl")
@click.argument("filename")
def nl_command(filename: str):
    for line_number, line in nl(filename):
        line_number = f"{line_number}".rjust(6, " ")
        sys.stdout.write(f"{line_number}\t{line}")


@click.command("wc")
@click.argument("filenames", nargs=-1)
def wc_command(filenames: str):
    total = {"lines": 0, "words": 0, "bytes": 0}
    for file in filenames:
        counts = wc(file)
        total["lines"] += counts["lines"]
        total["words"] += counts["words"]
        total["bytes"] += counts["bytes"]
        lines = str(counts["lines"]).rjust(7, " ")
        words = str(counts["words"]).rjust(7, " ")
        bytes = str(counts["bytes"]).rjust(7, " ")
        sys.stdout.write(f" {lines} {words} {bytes} {file}\n")
    else:
        lines = str(total["lines"]).rjust(7, " ")
        words = str(total["words"]).rjust(7, " ")
        bytes = str(total["bytes"]).rjust(7, " ")
        if len(filenames) > 1:
            sys.stdout.write(f" {lines} {words} {bytes} total\n")


@click.command("tail")
@click.argument("filenames", nargs=-1)
def tail_command(filenames: list[str]):
    for idx, file in enumerate(filenames):
        if len(filenames) > 1:
            sys.stdout.write(f"==> {file} <==\n")

        sys.stdout.write("\n".join(tail(file)))

        sys.stdout.write("\n")

        if idx < len(filenames) - 1:
            sys.stdout.write("\n")



cli.add_command(nl_command)
cli.add_command(wc_command)
cli.add_command(tail_command)

if __name__ == "__main__":
    cli()
