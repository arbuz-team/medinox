
class SQL:

    @staticmethod
    def Get(model, deleted=False, *args, **kwargs):
        return model.objects.get(*args, **kwargs) if deleted is None \
            else model.objects.filter(deleted=deleted).get(*args, **kwargs)

    @staticmethod
    def Filter(model, deleted=False, *args, **kwargs):
        return model.objects.filter(*args, **kwargs) if deleted is None \
            else model.objects.filter(deleted=deleted, *args, **kwargs)

    @staticmethod
    def All(model, deleted=False):
        return model.objects.all() if deleted is None \
            else model.objects.filter(deleted=deleted)

    @staticmethod
    def First(model, deleted=False, *args, **kwargs):
        return model.objects.filter(*args, **kwargs).first() if deleted is None \
            else model.objects.filter(deleted=deleted, *args, **kwargs).first()

    @staticmethod
    def Delete(model=None, data=None,
               force=True, *args, **kwargs):

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
    def Trash(model, *args, **kwargs):
        return model.objects.filter(deleted=True)\
            .filter(*args, **kwargs)

