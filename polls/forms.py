from django import forms

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question', max_length=250)