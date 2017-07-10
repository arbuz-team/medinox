
class SQL:

    @staticmethod
    def Get(model, *args, **kwargs):
        return model.objects.filter(deleted=False)\
            .get(*args, **kwargs)

    @staticmethod
    def Filter(model, *args, **kwargs):
        return model.objects.filter(deleted=False, *args, **kwargs)

    @staticmethod
    def All(model):
        return model.objects.filter(deleted=False)

    @staticmethod
    def First(model, *args, **kwargs):
        return model.objects.filter(deleted=False, *args, **kwargs).first()

    @staticmethod
    def Delete(model=None, data=None,
               force=False, *args, **kwargs):

        # force delete
        if force:
            if data: data.delete()
            else: model.objects.filter(*args, **kwargs).delete()
            return

        # only one object
        if data:

            try: iter(data)
            except TypeError: # not iterable

                # not force delete
                data.deleted = True
                data.save()
                return

        # a lot of objects
        if not data:
            data = model.objects.filter(*args, **kwargs)

        # not force delete
        for obj in data:
            obj.deleted = True
            obj.save()

    @staticmethod
    def Save(model=None, data=None,
             *args, **kwargs):

        if data:
            data.save()

        if not data:
            model(*args, **kwargs).save()

    @staticmethod
    def Trash(model):
        return model.objects.filter(deleted=True)

