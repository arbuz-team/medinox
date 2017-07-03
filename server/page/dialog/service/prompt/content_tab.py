from server.page.dialog.service.base import *


class Service_Content_Tab(Base_Service):

    def Manage(self):

        pk = self.request.POST['dialog_value']
        content = Content_Tab.objects.get(pk=pk)
        initial = {
            'header':       content.header,
            'paragraph':    content.paragraph,
        }

        self.request.session['main_content_tab'] = content
        self.content['title'] = Text(self.request, 93)
        self.content['image'] = content.image
        self.content['form'] = self.Prepare_Form(
            Form_Content_Tab, initial=initial)

        return self.Render_Dialog(
            'prompt.html', 'content_tab', only_root=True)
