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

    # Test tail if file is not specified. Read lines from stdin
    command_our = ["python", "homework_1/cli.py", "tail"]
    command_their = ["tail"]
    data1 = b"a\nb\nc\n" * 3
    data2 = b"a\nb\nc\n" * 3
    out1, err1, exitcode1 = capture(command_our, data1)
    out2, err2, exitcode2 = capture(command_their, data2)

    assert out1 == out2
    assert err1 == err2
    assert exitcode1 == exitcode2

    data_more_than_17_lines = b"a\nb\nc\n" * 10
    expected_data = data_more_than_17_lines.splitlines()[-17:]

    command_our = ["python", "homework_1/cli.py", "tail"]
    out1, err1, exitcode1 = capture(command_our, data_more_than_17_lines)
    result_data = out1.splitlines()

    assert expected_data == result_data
