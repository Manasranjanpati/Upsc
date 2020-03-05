from django import forms
from django.forms import ModelForm
from .models import FeedBackData, ServicesData, Comment, Post


class FeedbackForm(ModelForm):
    email = forms.CharField(max_length=50, error_messages={
                            'required': 'Email can not be blank', 'invalid': 'Please enter a valid email'})
    mobile = forms.CharField(error_messages={
        'required': 'Phone Number can not be blank', 'invalid': 'Please enter a valid phone number'})

    class Meta:
        model = FeedBackData
        fields = ['first_name', 'last_name',
                  'adress', 'email', 'subject', 'feedback']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'object_id']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','published_date']
