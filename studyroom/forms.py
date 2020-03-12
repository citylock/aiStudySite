from django import forms
from django.forms.widgets import RadioSelect, Textarea
from .models import Answer, StudentAnswer, TakenQuiz

class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        print ("===== LOG IN ::: TakeQuizForm =====")
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        print (question)
        # self.fields['answer'].queryset = question.answers.order_by('text')
        self.fields['answer'].queryset = Answer.objects.filter(question=question)
        # print (self.fields['answer'].queryset)
        
class TakenQuizForm(forms.ModelForm):
    class Meta:
        model = TakenQuiz
        fields = '__all__'