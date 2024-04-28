# Name

Assignment 1 , File Manager Testcases

#Setup:
For creating a file specifically for testing, we used the setup function.

#Teardown:
This function ensures that the file for testing is permanently deleted, even if a test fails or raises an exception. We use try and except blocks to ensure this condtion is covered. This is implemented in every test function! 

# File Manager Test Suite

This test suite is designed to verify the functionality of the `file_manager` , which provides functions for reading, writing, creating, and deleting files. The test cases cover various scenarios to ensure that the test file behaves as expected. The tests are structured to confirm the following functionality:

## Reading Files

### Test case: Reading a non-existent file

When trying to use the file manager's `read_file` method with a file name of a file that does not exist, we expect the file manager to return `None`. We are testing this in `test_read_file_when_nonexistent()` by calling the method and asserting that it returns `None.

### Test case: Reading file content correctly

When using the file manager's `read_file` method with an existing file, we expect the file manager to read and return its content correctly. In `test_read_file_content()`, we create a test file with some example content and then assert that `read_file` returns the same content correctly when reading it back.

### Test case: Reading an empty file

We need to ensure that the file manager can correctly read the content of an empty file. In `test_read_file_empty()`, we create an empty test file and then verify that `read_file` returns an empty string when reading it.

## Writing Files

### Test case: Writing file content

The `write_file` method should be able to write content to an existing file. In `test_write_file()`, we set up a test file and write new content to it using `write_file`. Then, we assert that the written content matches what we expected.

### Test case: Writing file returns true

When successfully writing to a file, the `write_file` method should return `True`. In `test_write_file_returns_true()`, we create a test file, write content to it, and assert that the method returns `True.

### Test case: Writing file returns false if failed

If writing to a file fails for any reason, the `write_file` method should return `False`. We test this in `test_write_file_returns_false_if_failed()` by attempting to write `None` to a file and checking that the method returns `False.

## Creating Files

### Test case: File creation

The `create_file` method should be able to create a new file with an optional initial content. In `test_file_got_created()`, we create a test file and assert that the method returns `True`, indicating that the file was successfully created. In 'test_os_path_file()' checks if the file got created, precisely the os_path, as descried in the instructions.

### Test case: File creation returns a boolean

The `create_file` method should return a boolean value to indicate whether the file creation was successful. We test this in `test_file_creation_returns_bool()` by creating a test file and verifying that the method returns a boolean value.

### Test case: Create error

We need to handle cases where file creation fails. In `test_create_error()`, we attempt to create a file with an empty name and ensure that the method returns `False.

## Deleting Files

### Test case: File deletion

The `delete_file` method should be able to delete a file. In `test_file_got_deleted()`, we create a test file, delete it, and assert that the method returns `True`, indicating successful deletion.

The function 'test_os_path_deleted()' checks if the file path has also bee successfully removed.

### Test case: File deletion returns a boolean

The `delete_file` method should return a boolean value to indicate whether the file deletion was successful. We test this in `test_file_deletion_returns_bool()` by creating a test file, attempting to delete it, and verifying that the method returns a boolean value.

## Running the Tests
'find_tests(prefix)' This function puts all global items, which are stored in a dictionary, that start with 'test_', as well as containing a prefix, which could be at any index in the test's name.

The test suite can be executed by running the `run_tests.py` script, for example:

```
python run_tests.py
```

This will automatically find and run all tests using introspection.
You can also specify a pattern to select specific tests. To do so, you can provide the `pattern` argument. Only tests that contain the specified string pattern will then be executed.



