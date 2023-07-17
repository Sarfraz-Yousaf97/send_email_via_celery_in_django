from django import forms
from .tasks import send_email_review_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label="Firstname", min_length=4, max_length=500, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'plcaeholder':'Firstname','id':'form-firstname'}
        )
    )
    email = forms.EmailField(
        label="Email",max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'plcaeholder':'email','id':'form-email'}
        )
    )
    review = forms.CharField(
        label="Email",max_length=200, widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'rows':5}
        )
    )


    def send_email(self):
        send_email_review_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'],self.cleaned_data['review']
        )