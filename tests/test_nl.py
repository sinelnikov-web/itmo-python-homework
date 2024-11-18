from tests.utils import FILENAMES, capture


def test_cli():
    for i in range(len(FILENAMES)):
        command_our = ["python", "homework_1/cli.py", "nl"] + [FILENAMES[i]]
        command_their = ["nl", "-b", "a"] + [FILENAMES[i]]
        out1, err1, exitcode1 = capture(command_our)
        out2, err2, exitcode2 = capture(command_their)

        assert out1 == out2
        assert err1 == err2
        assert exitcode1 == exitcode2

    command_our = ["python", "homework_1/cli.py", "nl"]
    command_their = ["nl", "-b", "a"]
    data1 = b"a\nb\nc\n" * 3
    data2 = b"a\nb\nc\n" * 3
    out1, err1, exitcode1 = capture(command_our, data1)
    out2, err2, exitcode2 = capture(command_their, data2)

    assert out1 == out2
    assert err1 == err2
    assert exitcode1 == exitcode2
