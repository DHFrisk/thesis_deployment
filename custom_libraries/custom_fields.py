from django.forms import ModelChoiceField

class CustomModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class CustomUserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()