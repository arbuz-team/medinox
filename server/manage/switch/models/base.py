from django.db import models
from django_countries.fields import CountryField
from server.manage.switch.website.base import *
import os


class Base_Model:

    def Set_Variables(self):
        pass

    def __init__(self):
        self.image_dir = None
        self.file_dir = None
        self.direction = Direction.NONE
        self.Set_Variables()
