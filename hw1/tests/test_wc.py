from homework_1.wc import wc
from tests.utils import FILENAMES, capture


def test_one_file():
    counts1 = wc("./tests/data/a.txt")

    assert counts1["lines"] == 9
    assert counts1["words"] == 16
    assert counts1["bytes"] == 122

    counts2 = wc("./tests/data/b.txt")

    assert counts2["lines"] == 99
    assert counts2["words"] == 293
    assert counts2["bytes"] == 1991

    counts3 = wc("./tests/data/c.txt")

    assert counts3["lines"] == 999
    assert counts3["words"] == 2976
    assert counts3["bytes"] == 20418


def test_cli():
    for i in range(len(FILENAMES)):
        command_our = ["python", "homework_1/cli.py", "wc"] + FILENAMES[: i + 1]
        command_their = ["wc"] + FILENAMES[: i + 1]
        out1, err1, exitcode1 = capture(command_our)
        out2, err2, exitcode2 = capture(command_their)

        assert out1 == out2
        assert err1 == err2
        assert exitcode1 == exitcode2

    command_our = ["python", "homework_1/cli.py", "wc"]
    command_their = ["wc"]
    data1 = b"a\nb\nc\n"
    data2 = b"a\nb\nc\n"
    out1, err1, exitcode1 = capture(command_our, data1)
    out2, err2, exitcode2 = capture(command_their, data2)

    assert out1 == out2
    assert err1 == err2
    assert exitcode1 == exitcode2
