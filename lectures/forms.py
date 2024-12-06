from django import forms

from .models import Lecture


TRUE_FALSE_CHOICES = (
        (True, 'Да'),
        (False, 'Нет')
    )


class AddLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['theme', 'show_theme', 'text', 'image', 'video_url']
        exclude = ['creator']   # Исключить создателя из полей для ввода

        widgets = {
            'theme': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите тему лекции'
            }),
            'show_theme': forms.Select(choices= TRUE_FALSE_CHOICES,
                                 attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст лекции'
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 
                                                'placeholder': 'Введите ссылку на видеоматериал'})
        }
