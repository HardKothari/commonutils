import datetime
import mariadb
import requests
import sys
import re
import os

# Global Variables
download_extensions = [".mkv", ".mp4", ".avi", ".zip", ".tar", ".rar", ".pdf", ".jpg", ".png", ".gif", ".m4v"]


class CommonUtils():
    def __init__(self):
        pass

    # Adding new line in the text file for logging
    def append_new_line(self, file_name, text_to_append):
        """Append given text as a new line at the end of file"""
        # Open the file in append & read mode ('a+')
        with open(file_name, "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(text_to_append)

    # Logging in a specified file
    def log(self, text, console_logging=True, message='', filename='logger.txt',
            send_message=False, chat_id=0, token=''):

        # Console Printing
        time_text = f'{datetime.datetime.now()} - {text}'
        if console_logging:
            print(text)

        # Logging in the file
        self.append_new_line(filename, time_text)

        # # Telegram Update
        if message == '' and send_message:
            self.send_telegram_message(time_text, chat_id, token)
        elif send_message:
            self.send_telegram_message(message, chat_id, token)

    def exception_handle(self, e, definition, message='', send_message=False, chat_id=0, token=''):
        # Console Message
        log_text = f"""
Inside {definition} Exception!!
Error: {e}
Error: {e.args}
Error on line {sys.exc_info()[-1].tb_lineno} 
"""
        self.log(log_text)

        # # Telegram Update
        if message == '' and send_message:
            self.send_telegram_message(log_text, chat_id, token)
        elif send_message:
            self.send_telegram_message(message, chat_id, token)

    def send_telegram_message(self, message, chat_id, token):
        tele_url = f"https://api.telegram.org/bot{token}"
        params = {"chat_id": chat_id, "text": message}
        requests.get(tele_url + "/sendMessage", params=params)

    def connect_mariadb(self, mariadb_username, mariadb_password, host, database, port=3306):
        # Connect to MariaDB Platform
        try:
            self.log("Connecting to MariaDB")
            conn = mariadb.connect(
                user=mariadb_username,
                password=mariadb_password,
                host=host,
                port=port,
                database=database
            )
            self.log("MariaDB Connection Successful!!")

            # Get Cursor for adding data in MariaDB
            cur = conn.cursor()

            return cur

        except mariadb.Error as e:
            self.exception_handle(e, "connect_mariadb")
            cur = False
            return cur

    # Removing all special characters from file name except 0-9,A-Z,a-z and .
    """Example value of path = "D:/Telegram/Normal/video/"""""
    def rename_all_files_remove_specialchars(self, path=''):
        try:
            if path != '':
                with os.scandir(path) as it:
                    for entry in it:
                        new_name = re.sub('[^0-9a-zA-Z.]+', '', entry.name)
                        os.rename(f'{path}\{entry.name}', f'{path}\{new_name}')
        except Exception as e:
            self.exception_handle(e, definition='rename_all_files_remove_specialchars')

    # Downloading direct links ending in certain file format
    """Example value of path = "D:/Telegram/Normal/video/"""""
    def direct_download_links(self, url, path):
        try:
            if any(ext in url for ext in download_extensions):

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                         'Chrome/90.0.4430.93 Safari/537.36'}
                local_filename = url.split('/')[-1]

                log_text = f"Starting to download {local_filename}...!!"
                self.log(log_text)

                with requests.get(url, headers=headers, stream=True) as r:
                    r.raise_for_status()
                    with open(f'{path}{local_filename}', 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            # if chunk:
                            f.write(chunk)

                log_text = f"Download {local_filename} complete... File Download Location: {path}{local_filename}!!"
                self.log(log_text)

        except Exception as e:
            self.exception_handle(e, 'direct_download_links')

    # def streams_download(self, path, url_array, m3u8, file_save_path):
    #     for no in range(0, len(url_array)):
    #
    #         if '.m3u8' not in url_array[no]:
    #             url_cmp = 'index.m3u8'
    #             url_1 = url_array[no] + url_cmp
    #             r_1 = requests.get(url_1)
    #             m3u8_master = m3u8.loads(r_1.text)
    #
    #         elif '.m3u8' in url_array[no]:
    #             playlist = m3u8.load(uri=url_m3u8, headers=headers, verify_ssl=False)
    #             real_url = playlist.playlists[0].absolute_uri
    #             # print(real_url)
    #             m3u8_master = m3u8.load(uri=real_url, headers=headers, verify_ssl=False)
    #
    #
    #         # Here you can investigate the m3u8_master segments
    #         print(m3u8_master.data['segments'][0])
    #
    #         file_number = 0
    #         i = 0
    #         percentage = 0.0
    #         print(f'Downloading Movie {url_names[no]} at time: {datetime.datetime.now()}')
    #         print('')
    #         for segment in m3u8_master.data['segments']:
    #             file_number += 1
    #
    #         with open(file_path + url_names[no] + '.ts', 'wb') as f:
    #
    #             for segment in m3u8_master.data['segments']:
    #                 print(f"Inside FOR loop!! {i} of {file_number}")
    #                 print('')
    #                 url = url_array[no] + segment['uri']
    #                 while (True):
    #                     try:
    #                         r = requests.get(url, timeout=15)
    #                     except:
    #                         continue
    #                         print("TIMEOUT")
    #                         print('')
    #                     break
    #                 f.write(r.content)
    #                 i += 1
    #                 percentage = round((i / file_number * 100), 2)
    #                 # print(f"\033[F{url}")
    #                 print(f"{percentage}% of Download Complete")
    #
    #             print(f"Download of Movie {url_names[no]} completed at time: {datetime.datetime.now()}!!")
    #
    #         cmd = 'ffmpeg -i "' + file_path + url_names[no] + '.ts" -c copy "' + file_save_path + url_names[
    #             no] + '.mp4"'
    #         os.system(cmd)
    #         os.remove(file_path + url_names[no] + '.ts')
    #         print(f"File {url_names[no]}.ts removed!!")
