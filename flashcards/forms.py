
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Flashcard, Pack

class MyCustomLoginForm(AuthenticationForm):
    # Будь-які ваші налаштування форми
    pass

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['ukrainian_word', 'english_word', 'pack']

    def __init__(self, *args, **kwargs):
        super(FlashcardForm, self).__init__(*args, **kwargs)
        self.fields['pack'].queryset = Pack.objects.all()

class MyCustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')  # Ви можете додати будь-які додаткові поля, які вам потрібні для форми реєстрації


class PackChoiceForm(forms.Form):
    pack = forms.ModelChoiceField(queryset=Pack.objects.all(), empty_label=None)