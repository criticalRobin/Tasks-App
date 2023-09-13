from django import forms
from core.user.models import MyUser


class UserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "off",
                "placeholder": "Confirm Password",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs["class"] = "form-control"
            form.field.widget.attrs["autocomplete"] = "off"
            form.field.widget.attrs["placeholder"] = (
                form.label[0].capitalize() + form.label[1:].lower()
            )
        self.fields["username"].widget.attrs["autofocus"] = True
        self.fields["password"].widget = forms.PasswordInput()

    class Meta:
        model = MyUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirm",
            "image",
        ]
        labels = {
            "username": "Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "password": "Password",
            "password_confirm": "Confirm Password",
            "image": "Image",
        }
