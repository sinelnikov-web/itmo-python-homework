from tests.utils import FILENAMES, capture


def test_cli():
    for i in range(len(FILENAMES)):
        command_our = ["python", "homework_1/cli.py", "tail"] + FILENAMES[: i + 1]
        command_their = ["tail"] + FILENAMES[: i + 1]
        out1, err1, exitcode1 = capture(command_our)
        out2, err2, exitcode2 = capture(command_their)

        assert out1 == out2
        assert err1 == err2
        assert exitcode1 == exitcode2
