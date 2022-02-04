from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

class UserForm(UserCreationForm):
    username = forms.Field(label = "사용자 이름")
    password1 = forms.Field(label="비밀번호")
    password2 = forms.Field(label="비밀번호 확인")
    phone_num = forms.Field(label = "휴대폰 번호")
    car_num = forms.Field(label="차량 번호")


    class Meta:
        model = User
        fields = ("username", "phone_num", "car_num")

