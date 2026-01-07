from django import forms
from routine.models import Routine


class RoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ["day", "class_name", "subject", "teacher", "start_time", "end_time", "room"]
        widgets = {
            "day": forms.Select(attrs={"class": "form-select"}),
            "class_name": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "teacher": forms.TextInput(attrs={"class": "form-control"}),
            "start_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "end_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "room": forms.TextInput(attrs={"class": "form-control"}),
        }
