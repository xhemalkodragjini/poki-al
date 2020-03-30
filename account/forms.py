from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Ky perdorues nuk ekziston')
            if not user.check_password(password):
                raise forms.ValidationError('Passwordi eshte i gabuar')
            if not user.is_active:
                raise forms.ValidationError('Perdoruesi nuk eshte aktiv')
        return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Adresa email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email2 = forms.EmailField(label='Konfirmo adresen email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Adresat duhet te jene identike")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "Ky email eshte regjistruar me pare. Tento te logohesh!")
        return super(UserRegisterForm, self).clean()
