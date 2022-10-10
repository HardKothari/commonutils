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

Example Usage:
```
from commonutils import commonutils
util = commonutils.CommonUtils()
```

##### append_new_line: 
This is used to append a new line in a text file without overwriting the content of the file which is already present.

Example Usage:
```
text = 'Example text to append in existing file'
util.append_new_line('file_name.txt', 'text')
```

##### log:
This is used to:
    - log text into a file
    - print on the console 
    - send a Telegram message if we want to for notification. (optional)

Example Usage:
```
# Log the text
text = 'Example text to log'
util.log('text', filename = 'logger.txt')

# Log the text and send message via telegram
text = 'Example text to log'
util.log('text',message='sample text message' ,filename = 'logger.txt', send_message = True, chat_id = 0000, token = 'telegram_API_token')
```    

##### exception_handle:
This is used alongwith try/except block to catch the exception message and print it in a way we want along with the actual line number on which error occured for easy debugging.
This also has optional functionality to send telegram message in case instant notification of error is required outside of program.

Example Usage:
```
# Exception Handle
try:
    i = i / 0
except Exception as e:
    util.exception_handle(e, "function/definition_name")
```

##### send_telegram_message:
This is used to send message via Telegram during any time in the python code where its used.

Example Usage:
```
# Sending Telegram Message
message = 'A sample text message to be sent'
util.send_telegram_message(message, chat_id=0000, token = 'telegram_API_token')
```

##### connect_mariadb:
This is used to connect with MariaDB database and use it for any database related operations inside our code.

Example Usage:
```
# Connecting to MariaDB
cur = util.connect_mariadb(mariadb_username, mariadb_password, host="192.168.0.22", database="database_name")

# Retrieving Data
cur.execute(
    "SELECT first_name,last_name FROM employees WHERE first_name=?", 
    (some_name,))
```
You can find more examples on below website:
https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/


##### rename_all_files_remove_specialchars:
This is used to remove all the special characters from a file name and jush have numeric/alphabets and "." as is. All special characters are removed and file is renamed.

Example Usage:
```
# Renaming a specific file
path = "D:/file_name.txt"
util.rename_all_files_remove_specialchars(path)
```

##### direct_download_links:
This is used to download the files directly from the link provided using requests module.

Example Usage:
```
# Renaming a specific file
path = "D:/"
url = "https://example_url.com/sample_filename.mkv"
util.direct_download_links(url,path)
```

##### streams_download: (Work in Progress):
This is used to download any streaming video which has .m3u8 format or .ts file name.