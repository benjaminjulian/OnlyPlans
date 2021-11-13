from django.forms import ModelForm
from onlyplans.models import OnlyPlan
from django.core.exceptions import ValidationError
from django import forms

class storeEventForm(ModelForm):
    title = forms.CharField(max_length=140, label="Titill")
    location_latitude = forms.FloatField(max_value=90, min_value=-90, label="")
    location_longitude = forms.FloatField(max_value=180, min_value=-180, label="")
    reach = forms.IntegerField(max_value=30, min_value=0, label="")
    when = forms.DateTimeField(label="Tímasetning", input_formats=['%Y/%m/%d %H:%M'])
    duration = forms.ChoiceField(choices=(('1', 'eitt augnablik'), ('10', 'smá stund'), ('30', 'hálftíma'), ('60', 'klukkutíma'), ('240', 'nokkra klukkutíma'), ('360', 'hálfan dag'), ('1440', 'sólarhring'), ('2880', 'tvo daga'), ('10000', 'viku')), label="Lengd")
    friendsonly = forms.BooleanField(label="Bara fyrir vini")

    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    def clean_location_latitude(self):
        data = self.cleaned_data['location_latitude']
        return data
        
    def clean_location_longitude(self):
        data = self.cleaned_data['location_longitude']
        return data

    def clean_when(self):
        data = self.cleaned_data['when']
        return data

    def clean_duration(self):
        data = self.cleaned_data['duration']
        return data

    def clean_reach(self):
        data = self.cleaned_data['reach']
        return data

    def clean_friendsonly(self):
        data = self.cleaned_data['friendsonly']
        return data

    class Meta:
        model = OnlyPlan
        fields = ['title', 'location_latitude', 'location_longitude', 'when', 'duration', 'reach', 'friendsonly']