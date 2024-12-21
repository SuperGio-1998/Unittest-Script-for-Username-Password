Unittest Script for Username-Password Validation

This repository contains a Python script that uses unittest to validate a simple login system. The script checks whether a provided username and password match the predefined correct values.

FEATURES

Tests the login function for a successful login with correct credentials.

Tests for invalid usernames and passwords, ensuring proper failure handling.


SCRIPT OVERVIEW

The main components of the script are:

1. login(username, password) function:

This function checks if the provided username and password match the correct credentials.



2. Test cases:

test_login_success: Verifies the login returns True with the correct username and password.

test_invalid_username: Verifies the login returns False if the username is incorrect.

test_invalid_password: Verifies the login returns False if the password is incorrect.




HOW TO RUN THE SCRIPT

1. Clone the repository:

git clone https://github.com/SuperGio-1998/Unittest-Script-for-Username-Password.git


2. Navigate to the directory where the script is located:

cd Unittest-Script-for-Username-Password


3. Run the script using Python:

python script_name.py

The script will run the test cases, and you'll see the results in the terminal.

EXPECTED OUTPUT

Running the script should give the following output:

...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
