from server.manage.switch.models.base import *
from server.service.file.views import *
from shutil import copyfile


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

    def Copy_Image(self, record):

        if not record:
            return

        if self.image_dir not in record.image.name:
            return

        # get file details
        name = record.image.name.rsplit('/', 1)[1]
        file_old_name = '{0}{1}'.format(
            self.image_dir, name)

        file_format = name.rsplit('.', 1)[1]
        file_new_name = '{0}{1}.{2}'.format(
            self.image_dir, self.pk, file_format)

        # create paths and urls
        old_path = Path_Manager.Static_Root(file_old_name)
        new_path = Path_Manager.Static_Root(file_new_name)
        url = Path_Manager.Static_URL(file_new_name)

        # copy image and save
        copyfile(old_path, new_path)
        self.image.name = url
        self.save()

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        Base_Model.__init__(self)

