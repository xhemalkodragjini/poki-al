from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')

        if username and password1:
            user = authenticate(username=username, password=password1)
            if not user or not user.is_active:
                raise forms.ValidationError("GABIM")
            return self.cleaned_data
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Adresa email', widget=forms.EmailInput(attrs={'placeholder': 'Emri i perdoruesit'}))
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Fjalekalimi')
    password2= forms.CharField(widget=forms.PasswordInput(), label='Konfirmo fjalekalimin')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        email_qs = User.objects.filter(email=email)

        if email and password1 and password2:
            if email_qs.exists():
                raise forms.ValidationError('Nje llogari tjeter me kete adrese emaili ekziston.')
            if password1 != password2:
                raise forms.ValidationError("GABIM")
            return self.cleaned_data
        return super(UserRegisterForm, self).clean(*args, **kwargs)
