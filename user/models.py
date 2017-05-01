from arbuz.models import *
import string, random


class User(Abstract_Model):

    unique = models.CharField(max_length=8, primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=75)
    approved = models.BooleanField(default=False)

    @staticmethod
    def Generate_User_Unique():

        unique = ''
        permitted_chars = string.ascii_letters + \
                          string.digits

        for char_number in range(0, 8):
            unique += random.choice(permitted_chars)

        if {'unique': unique} in User.objects.values('unique'):
            return User.Generate_User_Unique()

        return unique

    def __str__(self):
        return self.username



class User_Address(Abstract_Address):
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class No_Approved_User(Abstract_Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_key = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username



class Forgot_Password_User(Abstract_Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_key = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username