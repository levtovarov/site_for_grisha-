from django import forms
from .models import *


class GroupSearch(forms.Form):
    group_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'style': "position: relative; left: 55px; top: 30px; width: 400px", 'class': "form-control"}), label='',
                                 error_messages={'required': ''})


class CoverSearch(forms.Form):
    cover_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'style': "position: relative; top: 94px; left: 323px; width: 400px", 'class': "form-control"}), error_messages={'required': ''}, label='')


class CoverUpload(forms.ModelForm):
    # forms.BaseForm.use_required_attribute = False
    title = forms.CharField(label='Название',
                            widget=forms.TextInput(attrs={'style': "width: 300px", 'class': "form-control"}),
                            error_messages={'required': ''}, help_text='', required=False)
    creator = forms.CharField(label='Автор',
                              widget=forms.TextInput(attrs={'style': "width: 300px", 'class': "form-control"}),
                              error_messages={'required': ''}, required=False)
    file = forms.FileField(label='Кавер', widget=forms.FileInput(
        attrs={'style': "width: 300px", 'class': "form-control"}), error_messages={'required': ''}, required=False)

    class Meta:
        model = Cover
        fields = {'title': 'title', 'creator': 'creator', 'file': 'file'}
        error_messages = {'title': {'required': ''}}

        # , 'file': forms.FileField()


