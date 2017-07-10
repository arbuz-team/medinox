from server.manage.switch.forms.standard import *


class Abstract_Image_Form(Abstract_Form):

    def clean_image_name(self):
        image_base64 = self.data['image_base64']
        image_name = self.data['image_name']

        if image_base64:
            if not image_name:
                raise forms.ValidationError(Text(self, 166))

        return image_name

    def clean_image_base64(self):
        image_base64 = self.data['image_base64']
        image_name = self.data['image_name']

        if image_base64:

            # save temp image
            manager = File_Manager()
            image_base64 = manager.Save_From_Base64(
                image_base64, image_name, File.IMAGE)

            if not image_base64:
                raise forms.ValidationError(Text(self, 66))

        return image_base64

    def clean_image_url(self):
        image_url = self.data['image_url']

        if image_url:

            # save temp image
            manager = File_Manager()
            image_url = manager.Save_From_URL(
                image_url, File.IMAGE)

            if not image_url:
                raise forms.ValidationError(Text(self, 67))

        return image_url

    def clean_image(self):

        if self.data['image_url']:
            return 'image_url'

        if self.data['image_base64']:
            return 'image_base64'

        return ''

    def clean(self):

        if self.cleaned_data['image']:
            image = self.cleaned_data['image']
            self.cleaned_data['image'] = self.cleaned_data[image]

        return self.cleaned_data

    def Create_Fields(self):
        self.fields['image'] = forms.ImageField(required=False)
        self.fields['image_base64'] = forms.CharField(required=False)
        self.fields['image_url'] = forms.URLField(required=False)
        self.fields['image_name'] = forms.CharField(required=False)

    def Set_Widgets(self):

        image_attr = self.Attr()
        image_base64_attr = self.Attr(hidden=True)
        image_url_attrs = self.Attr(Text(self, 97))
        name_attrs = self.Attr(hidden=True)

        self.fields['image'].widget = forms.FileInput(attrs=image_attr)
        self.fields['image_base64'].widget = forms.TextInput(attrs=image_base64_attr)
        self.fields['image_url'].widget = forms.TextInput(attrs=image_url_attrs)
        self.fields['image_name'].widget = forms.TextInput(attrs=name_attrs)



class Abstract_File_Form(Abstract_Form):

    def clean_file_name(self):
        file_base64 = self.data['file_base64']
        file_name = self.data['file_name']

        if file_base64:
            if not file_name:
                raise forms.ValidationError(Text(self, 165))

        return file_name

    def clean_file_base64(self):
        file_base64 = self.data['file_base64']
        file_name = self.data['file_name']

        if file_base64:

            # save temp file
            manager = File_Manager()
            file_base64 = manager.Save_From_Base64(
                file_base64, file_name, File.FILE)

            if not file_base64:
                raise forms.ValidationError(Text(self, 163))

        return file_base64

    def clean_file_url(self):
        file_url = self.data['file_url']

        if file_url:

            # save temp file
            manager = File_Manager()
            file_url = manager.Save_From_URL(
                file_url, File.FILE)

            if not file_url:
                raise forms.ValidationError(Text(self, 162))

        return file_url

    def clean_file(self):

        if self.data['file_url']:
            return 'file_url'

        if self.data['file_base64']:
            return 'file_base64'

        return ''

    def clean(self):

        if self.cleaned_data['file']:
            file = self.cleaned_data['file']
            self.cleaned_data['file'] = self.cleaned_data[file]

        return self.cleaned_data

    def Create_Fields(self):
        self.fields['file'] = forms.FileField(required=False)
        self.fields['file_base64'] = forms.CharField(required=False)
        self.fields['file_url'] = forms.URLField(required=False)
        self.fields['file_name'] = forms.CharField(required=False)

    def Set_Widgets(self):

        file_attr = self.Attr()
        file_base64_attr = self.Attr(hidden=True)
        file_url_attrs = self.Attr(Text(self, 97))
        name_attrs = self.Attr(hidden=True)

        self.fields['file'].widget = forms.FileInput(attrs=file_attr)
        self.fields['file_base64'].widget = forms.TextInput(attrs=file_base64_attr)
        self.fields['file_url'].widget = forms.TextInput(attrs=file_url_attrs)
        self.fields['file_name'].widget = forms.TextInput(attrs=name_attrs)

