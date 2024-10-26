from django import forms
from app.models import *

class Topicform(forms.Form):
    tn=forms.CharField()
class Webpageform(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    email=forms.EmailField()
    url=forms.URLField()
class checkboxform(forms.Form):
    topic_names=forms.MultipleChoiceField(choices=[('topic','Topic.objects.all()')],widget=forms.CheckboxSelectMultiple)
    