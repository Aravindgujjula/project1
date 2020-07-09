from django import forms

from app1.models import course

class courseform(forms.ModelForm):
    name = forms.CharField()
    fee = forms.FloatField(min_value=3000)
    class Meta:
        model = course
        fields = "__all__"