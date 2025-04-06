from django import forms
  

class ShowEdit(forms.Form):
    show_name = forms.CharField(max_length=200)
    show_type = forms.CharField(max_length=30)
    show_duration = forms.IntegerField(help_text='In minutes')
    show_description = forms.CharField(widget=forms.Textarea, help_text='Preferably only one sentence')
    show_agerating = forms.CharField(max_length=20)
    show_release_date = forms.DateField()
    show_language = forms.CharField(max_length=20)
    show_banner = forms.ImageField()
    public = forms.BooleanField(required=False)