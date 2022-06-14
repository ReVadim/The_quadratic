from django import forms
from django.utils.translation import gettext_lazy as _
from equation.models import Comments, SolvingEquation
from django.core.exceptions import ValidationError
from . import views

from services import quadratic_equation


class CommentForm(forms.ModelForm):
    """ Form for add comments """

    class Meta:
        model = Comments
        fields = ['username', 'comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'cols': 80, 'rows': 7}),
        }
        labels = {
            'username': _('Имя пользователя'),
            'comment_text': _('Текст'),
        }
        help_texts = {
            'username': _('Авторизация не требуется'),
            'comment_text': _('Не более 300 символов'),
        }


class ValuesForm(forms.Form):
    """ Form for add values for solving equation """

    a = forms.FloatField(help_text='аргумент при "х2"', initial=1)
    b = forms.FloatField(help_text='аргумент при "х"', initial=1)
    c = forms.FloatField(required=False, help_text='третий аргумент', initial=0)

