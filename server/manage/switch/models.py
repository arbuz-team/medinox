from django.db import models
from django_countries.fields import CountryField
from server.manage.switch.base import *
import os


class Base_Model:

    def Set_Variables(self):
        pass

    def __init__(self):
        self.image_dir = None
        self.file_dir = None
        self.direction = Direction.NONE
        self.Set_Variables()



class Abstract_Model(Base_Model, models.Model):

    position = models.IntegerField(unique=True, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def Get_File_Data(self, name, file_dir):

        # validate variables
        if not name:
            return

        if file_dir in str(name):
            return

        # get file details
        file_format = name.rsplit('.')[1]
        file_name = '{0}{1}.{2}'.format(
            file_dir, self.pk, file_format)

        # create paths and urls
        old_path = Path_Manager.Media_Root(name)
        new_path = Path_Manager.Static_Root(file_name)
        url = Path_Manager.Static_URL(file_name)

        return [old_path, new_path, url]

    def Save_Image(self, name):

        old_path, new_path, url = \
            self.Get_File_Data(name, self.image_dir)

        # save
        os.rename(old_path, new_path)
        self.image.name = url
        self.save()

    def Save_File(self, name):

        old_path, new_path, url = \
            self.Get_File_Data(name, self.file_dir)

        # save
        os.rename(old_path, new_path)
        self.file.name = url
        self.save()

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        Base_Model.__init__(self)



class Abstract_Address(Abstract_Model):

    full_name = models.CharField(max_length=50)
    doctor_number = models.CharField(max_length=7) # for polish users
    address_line = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)  # state/province/region
    postcode = models.CharField(max_length=10)  # zip/postal code
    country = CountryField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name
