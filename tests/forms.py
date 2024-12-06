from django import forms
from .models import Question, Test


CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4')
]


class AddTest(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['possible_points']
        exclude = ['lecture']

        widgets = {
            'possible_points': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите максимальное количество баллов за тест'
            })
        }



class OneAnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ответ на вопрос'
    }))



class ManyResponsesForm(forms.Form):
    answer = forms.ChoiceField(label=Question.question_str,
                               choices=CHOICES,
                               widget=forms.Select(attrs={
                                'class': 'form-check form-check-inline'
                               }))



class AddOneAnswerForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_str', 'correct_answer']
        exclude = ['test', 'answer1', 'answer2', 'answer3', 'answer4']

        widgets = {
            'question_str': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вопрос'
            }),
            'correct_answer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите правильный вариант ответа'
            })
        }



class AddManyResponsesForm(forms.ModelForm):
    answer1 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вариант ответа'
    }))
    answer2 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вариант ответа'
    }))
    answer3 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вариант ответа'
    }))
    answer4 = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вариант ответа'
    }))

    class Meta:
        model = Question
        fields = ['question_str', 'correct_answer', 'answer1', 'answer2', 'answer3', 'answer4']
        exclude = ['test']

        widgets = {
            'question_str': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вопрос'
            }),
            'correct_answer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите правильный вариант ответа'
            })
        }
