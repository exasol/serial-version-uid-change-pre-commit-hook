import subprocess
import mmap
import os.path


def main():
    result = subprocess.run(['git', 'diff', '--cached', '--name-only'], stdout=subprocess.PIPE);
    changed_files = result.stdout.decode('utf_8').split("\n")
    if not all(list(map(check_file, filter(is_java_file, changed_files)))):
        print()
        print("The files listed above were changed but the serialVersionUID was not.")
        print("Please check if this is intended. In that case, add an empty comment after the serialVersionUID.")
        exit(1)
    else:
        exit(0)


def check_file(file_name):
    """
    Checks if a file was changed and in that case if also the serialVersionUID was changed.
    :param file_name: name of the file to check
    :type file_name: str
    :return: True if check passed
    :rtype bool
    """
    if not os.path.isfile(file_name):
        return True  # file was deleted --> no problem

    if contains_file_serial_id(file_name) and not was_serial_id_changed(file_name):
        print(file_name)
        return False
    else:
        return True


def was_serial_id_changed(file_name):
    """
    Check if the diff for a given file name contains a change of the serialVersionUID.
    :param file_name: name of the file to check
    :type file_name: str
    :return: True if a change of the serialVersionUID was found
    :rtype bool
    """
    result = subprocess.run(['git', 'diff', '--cached', '--unified=0', file_name], stdout=subprocess.PIPE);
    lines = result.stdout.decode('utf_8').split("\n")
    for line in lines:
        if 'serialVersionUID' in line:
            print("found")
            return True
    return False


def contains_file_serial_id(file_name):
    """
    Check if the given file contains a serialVersionUID.
    :param file_name: name of the file to check
    :type file_name: str
    :return: True if the file contains a serialVersionUID
    :rtype bool
    """
    with open(file_name, 'rb', 0) as file, \
            mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as file_contents:
        return file_contents.find(b'serialVersionUID') != -1


def is_java_file(file_name):
    """
    Check if a file name has a .java ending
    :param file_name: file name to check
    :type file_name: str
    :return: True if file has .java ending
    :rtype bool
    """
    return file_name.endswith(".java")


if __name__ == "__main__":
    main()
