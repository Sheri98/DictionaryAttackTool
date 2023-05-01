# Password Brute-Forcing Script for CVE-2019-17240

This Python script is an example of a password brute-forcing tool that targets the CVE-2019-17240 vulnerability in a web application. It tries to log in to an admin page using a list of passwords from a file, until it finds the correct password for the given username.

## Usage

To use this script, you will need to modify the following variables in the code to match your target web application:

- `host`: The IP address or domain name of the target web application.
- `login_page_url`: The URL of the login page for the target web application.
- `passlist`: The path to the file containing the list of passwords to try.
- `username`: The username to use for the login attempt.

Once you have modified the variables, you can run the script by executing the following command in a terminal:


The script will then attempt to log in to the target web application using each password in the `passlist` file, until it finds the correct password for the given username.

## Requirements for python3 brute_force.py

- Python 3.x
- Requests library

To install the Requests library, you can use pip by executing the following command in a terminal:


## Contributing

Contributions to this project are welcome! If you find a bug or have an idea for a feature, please submit an issue or pull request.

## Credits

This script was created by [Your Name] and is released under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer

This script is provided for educational purposes only. The author and contributors are not responsible for any illegal or unauthorized use of this tool. Use at your own risk.

