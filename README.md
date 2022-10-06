# commonutils

## Introduction:

Commonutils is a package with various simple tools which we need to use in our day to day coding with python and we keep on repeating them in every code we use. Its an effort to reduce the repeating block of code which can be generalized amongst all python projects which we have.

Example: We use try/except block in various method to catch the error and present it in a format we need along with the line number in which error occured. We can use this package instead and method "exception_handle" to do the same without repeating the block of code everytime.

## Prerequisites: 
> They will be installed automatically with package installation
- mariadb
- requests
- colorama

## Installing Instructions:

```
pip install git+https://github.com/HardKothari/commonutils
```

## Following methods are there to start with this package:

##### - append_new_line: 
This is used to append a new line in a text file without overwriting the content of the file which is already present.

##### - log:
This is used to:
    - log text into a file
    - print on the console 
    - send a Telegram message if we want to for notification. (optional)

##### - exception_handle:
This is used alongwith try/except block to catch the exception message and print it in a way we want along with the actual line number on which error occured for easy debugging.
This also has optional functionality to send telegram message in case instant notification of error is required outside of program.

##### - send_telegram_message:
This is used to send message via Telegram during any time in the python code where its used.

##### - connect_mariadb:
This is used to connect with MariaDB database and use it for any database related operations inside our code.

##### - rename_all_files_remove_specialchars:
This is used to remove all the special characters from a file name and jush have numeric/alphabets and "." as is. All special characters are removed and file is renamed.

##### - direct_download_links:
This is used to download the files directly from the link provided using requests module.

##### - streams_download: (Work in Progress):
This is used to download any streaming video which has .m3u8 format or .ts file name.