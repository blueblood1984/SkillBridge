from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from lectures.models import Lecture
from users.models import User


class CreateLectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user_object = User.objects.filter(username=user.username)
        new_user_object = get_object_or_404(user_object)
        self.fields['course'].queryset = self.fields['course'].queryset.filter(teacher=new_user_object.id)

