from cProfile import label
from dataclasses import field
from tkinter.ttk import Widget
from django import forms
from report.models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model=Report
        fields=['subject','car_num','content']
        widgets={
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'car_num':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','rows':10}),
        }
        labels={
            'subject':'제목',
            'car_num':'차번호',
            'content':'내용',

        }
        