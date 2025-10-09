from django.forms import ModelForm
from .models import Reviews, ReviewResponse
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['review', 'reviewer', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш отзыв...'}),
            'reviewer': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'rating': forms.RadioSelect(),
        }


class ReviewResponseForm(forms.ModelForm):
    class Meta:
        model = ReviewResponse
        fields = ['author', 'response_text']
        widgets = {
            'author': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'form-control'
            }),
            'response_text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Ваш ответ на отзыв...',
                'class': 'form-control'
            }),
        }
