#!/usr/bin/env python3

import file_manager
import os
import time
import sys


def test_read_file_when_nonexistent():
    file_name = "file_does_not_exist.txt"

    actual_value = file_manager.read_file(file_name)
    expected_value = None

    assert actual_value == expected_value


def test_read_file_content():
    file_name = "file_content_example.txt"
    expected_content = "This is a file"
    setup(file_name, "This is a file")
    actual_content = file_manager.read_file(file_name)
    teardown(file_name)
    assert actual_content == expected_content




def test_read_file_empty():
    file_name = "empty.txt"
    setup(file_name, "")

    actual = file_manager.read_file(file_name)
    expected = ""
    teardown(file_name)
    assert actual == expected



def test_write_file():
    file_name = "file_write_example.txt"
    content_to_write = "A new file"

    setup(file_name, "")
    file_manager.write_file(file_name, content_to_write)

    with open(file_name, "r") as f:
        content_inside = f.read()


    teardown(file_name)
    assert content_inside == content_to_write

# def test_write_file():
#     file_name = "file_write_example.txt"
#     content_to_write = "A new file"
#
#     setup(file_name, "")
#     file_manager.write_file(file_name, content_to_write)
#
#     written_content = file_manager.read_file(file_name)
#     teardown(file_name)
#     assert written_content == content_to_write



def test_write_file_returns_true():
    file_name = "file_write_example.txt"
    setup(file_name, "Example")
    expectation = file_manager.write_file(file_name, "New text to write")
    teardown(file_name)
    assert expectation == True



def test_write_file_returns_false_if_failed():
    file_name = "file_write_example.txt"
    expect = file_manager.write_file(file_name, None)
    teardown(file_name)
    assert expect == False


def test_file_got_created():
    file_name = "file_create_example.txt"
    expect1 = file_manager.create_file(file_name)
    teardown(file_name)
    assert expect1 == True

def test_os_path_file():
    file_name = "file_create_example.txt"
    file_manager.create_file(file_name)
    expect2 = os.path.exists(file_name)
    teardown(file_name)
    assert expect2 == True



def test_file_creation_returns_bool():
    expect = isinstance(file_manager.create_file("newerfile.txt", "correcto"), bool)
    teardown("newerfile.txt")
    assert expect == True



def test_create_error():
    assert file_manager.create_file("", 0) == False


def test_file_got_deleted():
    file_name = "file_delete_example.txt"
    setup(file_name, "An example")
    expect = file_manager.delete_file(file_name)
    teardown(file_name)
    assert expect == True

def test_os_path_deleted():
    file_name = "file_delete_example.txt"
    setup(file_name, "An example")
    file_manager.delete_file(file_name)
    expect = os.path.exists(file_name)
    teardown(file_name)
    assert expect == False


def test_file_deletion_returns_bool():
    setup("newfile.txt", "another one")
    expect = isinstance(file_manager.delete_file("newfile.txt"), bool)
    teardown("newfile.txt")
    assert expect==True


def setup(file_name, content):
    # It says in the file manager description that the name of the file should be the entire path
    # full_file_path = os.path.join(os.path.dirname(__file__) , file_name)
    try:
        with open(file_name, "w") as file:
            file.write(content)

        return True
    except Exception as e:
        print(f"Error creating/writing to the file: {e}")
        return False


def teardown(file):
    try:
        os.remove(file)
        return True
    except FileNotFoundError:
        print(f"File not found: {file}")
        return False
    except Exception as e:
        print(f"Error deleting the file: {e}")
        return False


def run_tests(pattern=""):
    results = {"pass": 0, "fail": 0, "error": 0}
    all_tests = find_tests("test_", f"{pattern}")

    if len(all_tests) == 0:
        return results

    for (name, func) in all_tests:
        try:
            start = time.time()
            func()
            end = time.time()

            time_needed_ms = (end - start) * 1000
            time_needed_formatted = "{:.2f}".format(time_needed_ms)

            print(f"✔ {name} has passed: with a duration of {time_needed_formatted}ms")
            results["pass"] += 1
        except AssertionError:
            print(f"! {name} has failed: with a duration of {time.process_time_ns()}")
            results["fail"] = results["fail"] + 1
        except Exception:
            print(f"! {name} contains an exception: with a time of {time.process_time_ns()}")
            results["error"] += 1

    return results


def find_tests(prefix, pattern=""):
    tests = []
    for (name, func) in globals().items():
        if name.startswith(prefix) and pattern in name:
            tests.append((name, func))
    return tests


if __name__ == "__main__":
    if len(sys.argv) > 3:
        raise Exception
    elif len(sys.argv) == 2 and sys.argv[1] == "--select":
        raise SyntaxError("invalid syntax")
    elif (len(sys.argv) > 1 and sys.argv[1] == "--select"):
        pattern = sys.argv[2]
        print(run_tests(f"{pattern}")) #run_tests("{pattern}")
    else:
        print(run_tests())
