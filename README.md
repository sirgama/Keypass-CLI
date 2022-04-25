# KEYPASS-CLI

Simple Python App that creates new credentials with properties. Touches on Test Driven Development using unittest (Python test framework).

## Technologies Used

- Python3.9
- unittest (Python test framework)


##### Setup Instructions and Installation

- Clone this repository to a location in your file system. `git clone https://github.com/sirgama/Keypass-CLI.git`
- Open terminal command line then navigate to the root folder of the application. `cd Keypass-CLI`
- Run `./run.py` 


## Behaviour Driven Development

1. Displays Intro Message to user
    - OUTPUT: "Use these commands to proceed to your keypass account?"
   - OUTPUT: " To create account use: CA "
   - OUTPUT: "To login with an existing account use: LO ?"
2. Enter Short Code
   - INPUT: "ca"
   - INPUT: "username", "password"
   - OUTPUT: "Account created Successfully" - Create new user account by providing required account details
3. Enter Short Code
   - INPUT: "sc" 
   - OUTPUT: "Kindly enter the Software/application name you want to search for:" - Prompts user to enter applicatin name to search for
   - OUTPUT: "Application: github username: Sirgama....." - Displays existing credentials stored in the system
4. Enter Short Code
   - INPUT: "dc"
   - OUTPUT: "Here's a list of all Credentials" - list of all available credentials
   - OUTPUT: "Account:  github    Username: Sirg    Password:  2323" - Returns list of all saved credentials

## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


## Known Bugs

If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

### License

*MIT*
Copyright (c) 2022 **Gamaliel Sirengo**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
