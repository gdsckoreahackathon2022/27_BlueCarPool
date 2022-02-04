from django import forms
from recruitment.models import Recruit

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['departure', 'destination', 'car_num', 'time', 'max_num', 'present_num']
        widgets = {
            'departure': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'car_num': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'max_num': forms.NumberInput(),
            'present_num': forms.NumberInput(),
        }
        labels = {
            'departure': '출발지',
            'destination': '도착지',
            'car_num': '차량 번호',
            'time': '출발 시각',
            'max_num': '최대 인원',
            'present_num': '현재 인원',
        }