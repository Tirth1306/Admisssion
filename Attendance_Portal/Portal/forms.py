from django import forms


def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise forms.ValidationError("Only CSV file is accepted")

class uploadfile(forms.Form):
    file = forms.FileField(label = "Input File", validators=[validate_file_extension])