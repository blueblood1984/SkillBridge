from django import forms
from django.shortcuts import get_object_or_404

from users.models import User
from .models import Quiz, Questions, Choices


class QuizForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={

        'type': 'datetime-local'
    }))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local'
    }))

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'start_time', 'end_time', 'course']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        user_object = User.objects.filter(username=user.username)
        new_user_object = get_object_or_404(user_object)
        self.fields['course'].queryset = self.fields['course'].queryset.filter(teacher=new_user_object.id)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['description']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choices
        fields = ['text', 'is_correct']


ChoicesFormSet = forms.inlineformset_factory(
    Questions, Choices, form=ChoiceForm, extra=4, can_delete=False  # 默认3个问题
)
