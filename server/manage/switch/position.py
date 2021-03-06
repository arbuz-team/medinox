from server.manage.switch.website.base import *
from server.manage.switch.enum import *
from server.service.sql.views import *


class Position_Manager(Base_Website):

    @staticmethod
    def Change_Position(model, position, move=Direction.NONE):

        # get current object
        object_index = SQL.Get(model, position=position)

        # change with up element
        if move == Direction.UP:
            # swap - object up position 0
            object_up = SQL.Get(model, position=position - 1)
            object_up_position = object_up.position + 1
            object_up.position = 0
            SQL.Save(data=object_up)

            # save position
            object_up.position = object_up_position
            object_index.position -= 1

            SQL.Save(data=object_index)
            SQL.Save(data=object_up)

        # change with down element
        if move == Direction.DOWN:
            # swap - object down position 0
            object_down = SQL.Get(model, position=position + 1)
            object_down_position = object_down.position - 1
            object_down.position = 0
            SQL.Save(data=object_down)

            # save position
            object_down.position = object_down_position
            object_index.position += 1

            SQL.Save(data=object_index)
            SQL.Save(data=object_down)

    @staticmethod
    def Insert_Element(model, new_object):

        position = new_object.position
        direction = new_object.direction

        if direction == Direction.UP:

            # change greater elements positions
            greater_objects = SQL.Filter(model,
                position__gte=position).order_by('-position')

            for greater_object in greater_objects:
                greater_object.position += 1
                SQL.Save(data=greater_object)

        if direction == Direction.DOWN:

            # change greater elements positions
            greater_objects = SQL.Filter(model,
                position__gt=position).order_by('-position')

            for greater_object in greater_objects:
                greater_object.position += 1
                SQL.Save(data=greater_object)

            # set position for new object
            new_object.position = position + 1

    def Get_Direction(self):
        direction = self.Get_Post_Other('direction')

        switch = {
            'up':   Direction.UP,
            'down': Direction.DOWN,
            '':     None
        }

        return switch[direction]

    def Button_Service_Delete(self, model):

        # get position
        position = SQL.Get(model,
           pk=self.request.POST['value']).position

        # delete
        SQL.Delete(model, pk=self.request.POST['value'])

        # change greater elements positions
        greater_objects = SQL.Filter(model,
            position__gte=position).order_by('position')

        for greater_object in greater_objects:
            greater_object.position -= 1
            SQL.Save(data=greater_object)


    def Button_Service(self, model):

        if self.request.POST['_name_'] == 'delete':
            self.Button_Service_Delete(model)

        if self.request.POST['_name_'] == 'move_up':
            desc = SQL.Get(model, pk=self.request.POST['value'])
            self.Change_Position(model, desc.position, Direction.UP)

        if self.request.POST['_name_'] == 'move_down':
            desc = SQL.Get(model, pk=self.request.POST['value'])
            self.Change_Position(model, desc.position, Direction.DOWN)
