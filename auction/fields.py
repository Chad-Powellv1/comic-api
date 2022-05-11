from rest_framework import serializers


class CustomForeignKeyField(serializers.RelatedField):

    def __init__(self, **kwargs):
        self.model = kwargs.pop('model', None)
        self.field_name = kwargs.pop('field_name', None)

        if self.model is None:
            raise TypeError('"model" is not a valid model class')

        if self.field_name is None:
            raise TypeError('"field_name" is not a valid field_name on model')

        super().__init__(**kwargs)

        return getattr(self.model, str(self.field_name))

    def to_internal_value(self, id):
        if isinstance(id, int):
            instance = self.model.objects.filter(id=id).first()
            if instance:
                return instance

        raise serializers.ValidationError(
            "No instance exists with id \"%s\"." % str(id),
        )
