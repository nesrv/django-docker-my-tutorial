from django import forms
from django.core.exceptions import ValidationError

from selfedu.models import *


class AddUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['door'].empty_label = "Door not selected ..."

    class Meta:
        model = Employees
        fields = ['name', 'login', 'photo', 'is_active', 'door']

        # fields = '__all__'

        def clean_title(self):
            name = self.cleaned_data['name']
            if len(name) > 32:
                raise ValidationError('Длина превышает 32')
            return name

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(AddUserForm, self).save(*args, **kwargs)

    # self.slug = slugify(self.name)
    # super(AddUserForm, self).save(*args, **kwargs)

#
#
#
#
#
#

# class AddUserForm(forms.Form):
#     name = forms.CharField(max_length=32, label="Name", widget=forms.TextInput(attrs={'class': 'form-input'}))
#     slug = forms.SlugField(max_length=32, label="URL")
#     login = forms.CharField(max_length=100, label="Login")
#     is_active = forms.BooleanField(label="Activity", required=False, initial=True)
#     door = forms.ModelChoiceField(queryset=Doors.objects.all(), label="Doors", empty_label="Дверь не выбрана")
#
#
#     # auto creation slag
#
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.hiring)
#         super(AddUserForm, self).save(*args, **kwargs)
