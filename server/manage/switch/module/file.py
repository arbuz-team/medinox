from server.manage.switch.module.enum import *
from server.manage.switch.module.base import *

from PIL import Image
from io import BytesIO
from urllib.request import urlopen
import base64, imghdr, os, random


class File_Manager:

    @staticmethod
    def Generate_Details(file_format):

        name = str(random.randrange(1000, 9999))
        if file_format: name += '.' + file_format

        path_root = '{0}/{1}'.format(MEDIA_ROOT, name)
        path_url = '{0}{1}'.format(MEDIA_URL, name)

        return [name, path_root, path_url]

    @staticmethod
    def Check_If_Image(path):

        if imghdr.what(path) in ['jpeg', 'png']:
            return True

        return False

    def Save_From_Base64_File(self):

        # get details
        name, path_root, path_url = self. \
            Generate_Details(self.format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_Base64_File()

        # save file
        file = open(path_root, 'wb')
        file.write(base64.b64decode(self.base64_file))
        file.close()

        return name

    def Save_From_Base64_Image(self):

        name, path_root, path_url = self. \
            Generate_Details(self.format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_Base64_Image()

        with open(path_root, 'wb') as file:
            file.write(base64.b64decode(self.base64_file))

        # if file is not image
        if not self.Check_If_Image(path_root):
            os.remove(path_root)
            name = ''

        return name

    def Save_From_Base64(self, _base64, file_name, file_type):

        self.base64_file = _base64.split(',', 1)[1]
        self.format = file_name.split('.', 1)[1] \
            if len(file_name.split('.', 1)) == 2 else ''

        if file_type == File.FILE:
            return self.Save_From_Base64_File()

        if file_type == File.IMAGE:
            return self.Save_From_Base64_Image()

    def Save_From_URL_Image(self):

        image = Image.open(self.binary_file)
        name, path_root, path_url = self. \
            Generate_Details(image.format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_URL_Image()

        image.save(path_root)

        # if file is not image
        if not self.Check_If_Image(path_root):
            os.remove(path_root)
            name = ''

        return name

    def Save_From_URL_File(self):

        # get format file
        file_name = self.url.rsplit('/', 1)[-1]
        file_format = file_name.rsplit('.', 1)[-1] \
            if len(file_name.rsplit('.', 1)) > 1 else ''

        # get details
        name, path_root, path_url = self. \
            Generate_Details(file_format.lower())

        # file with the name exists
        if os.path.exists(path_root):
            self.Save_From_URL_File()

        # save file
        file = open(path_root, 'wb')
        file.write(self.binary_file.getvalue())
        file.close()

        return name

    def Save_From_URL(self, url, file_type):
        self.binary_file = BytesIO(urlopen(url).read())
        self.url = url

        if file_type == File.FILE:
            return self.Save_From_URL_File()

        if file_type == File.IMAGE:
            return self.Save_From_URL_Image()

    def __init__(self):
        self.format = None
        self.base64_file = None
        self.binary_file = None
        self.url = None