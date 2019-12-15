import os
import sys
import stat
import platform


def is_windows():
    return platform.system() == "Windows"


def get_interpreter():
    interpreter_path = sys.executable
    interpreter_dir = os.path.dirname(interpreter_path)
    return interpreter_path, interpreter_dir


def read_lines(fn):
    with open(fn, "r") as foo:
        lines = foo.readlines()
    return lines


def write_lines(fn, lines):
    with open(fn, "w") as foo:
        foo.writelines(lines)


def parse_mode(mode="6"):
    mode = int(mode)
    assert 0 <= mode < 8
    _readable, _writable, _executable = map(lambda x: x=='1', bin(mode)[-3:])
    return _readable, _writable, _executable


def chmod(fpath, mode="644"):
    """
        A wrapper for os.chmod.

        You can specify mode as in shell!
    """
    assert os.path.isfile(fpath)

    stat_mode = {
        "user":   [stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR],
        "groups": [stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP],
        "others": [stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH],
    }

    for _mode, _stat in zip(mode, stat_mode.values()):
        for _i, _j in zip(parse_mode(_mode), _stat):
            if _i:
                os.chmod(fpath, os.stat(fpath).st_mode | _j)


def copy_scripts_to_bin(script_file):
    """
        Copy scripts in "./build_server.py" to bin folder of current interpreter.
    """
    _path, _dir = get_interpreter()
    script_lines = read_lines(script_file)

    first_line = "#!%s\n"%_path
    if script_lines[0].startswith("#!"):
        script_lines[0] = first_line
    else:
        script_lines.insert(0, first_line)

    if not is_windows():
        bin_file = os.path.join(_dir, os.path.splitext(os.path.basename(script_file))[0])
    else:
        bin_file = os.path.join(_dir, "Scripts", os.path.basename(script_file))

    try:
        write_lines(bin_file, script_lines)
        chmod(bin_file, "775")
        print("Scripts have been writen to {}".format(bin_file))
    except Exception as e:
        UserWarning("Failed to write scripts to {}, permission denied, please use sudo!".format(bin_file))



if __name__ == "__main__":
    print(sys.argv)
    print(sys.executable)