from django import forms

from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'content', 'car_num']

        labels = {
            'subject': '제목',
            'car_num': '차량 번호',
            'content': '내용',
        }