from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML, Field, Reset

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','groups','password1','password2']
        widgets ={
            'first_name': forms.TextInput(attrs={'placeholder': 'Prense...'})
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterFrom, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['username'].required=True
        self.fields['email'].required=True
        self.fields['password1'].required=True
        self.fields['password2'].required=True
        self.helper.layout= Layout(
           Row(
               Column(Field('first_name',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               Column(Field('last_name',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               css_class='row'
           ),
           Row(
               Column(Field('email',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               Column(Field('username',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               css_class='row'
           ),
           Row(
               Column(Field('password1',placeholder='Prense...',css_class='rounded-1'), css_class='col-md-6 mb-0'),
               Column(Field('password2',placeholder='Prense...',css_class='rounded-1'), css_class='col-md-6 mb-0'),
               css_class='row'
           ),
           Row(
               Column(Field('groups'), css_class='col-md-12 mb-0'),
               css_class='row'
           ),

           HTML(""" 
                    <div class="my-3">
                        <button type="submit" class="btn btn-sm btn-primary">Save</button>
                        <button type="reset" onclick="self.history.back()" class="btn btn-sm btn-danger">Cansela</button>
                    </div>
           """),
        )


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','groups']
        widgets ={
            'first_name': forms.TextInput(attrs={'placeholder': 'Prense...'})
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['first_name'].required=True
        self.fields['last_name'].required=True
        self.fields['username'].required=True
        self.fields['email'].required=True
        self.helper.layout= Layout(
           Row(
               Column(Field('first_name',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               Column(Field('last_name',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               css_class='row'
           ),
           Row(
               Column(Field('email',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               Column(Field('username',placeholder='Prense...',css_class='rounded-1'), css_class='form-group col-md-6 mb-0'),
               css_class='row'
           ),
          
           Row(
               Column(Field('groups'), css_class='col-md-12 mb-0'),
               css_class='row'
           ),

           HTML(""" 
                    <div class="my-3">
                        <button type="submit" class="btn btn-sm btn-primary">Update</button>
                        <button type="reset" onclick="self.history.back()" class="btn btn-sm btn-danger">Cansela</button>
                    </div>
           """),
        )


# class UpdatePassword(models.Forms):
#     old_password = forms.CharField(
#         label="Old Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm','placeholder':'Prense...'}),
#     )
#     new_password1 = forms.CharField(
#         label="New Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm','placeholder':'Prense...'}),
#     )
#     new_password2 = forms.CharField(
#         label="Confirm New Password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm','placeholder':'Prense...'}),
#     )

   
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         # self.helper.form_class = 'orm-horizontalf'
#         self.helper.add_input(Submit('submit', 'Change Password', css_class='btn btn-sm btn-primary'))
#         self.helper.add_input(Reset('reset', 'Cansel', css_class='btn btn-danger btn-sm'))

