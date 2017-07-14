from server.manage.switch.models.base import *
from server.service.file.views import *


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

