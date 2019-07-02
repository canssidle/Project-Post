from django import forms
from .models import Project, Review, Profile
class UploadSiteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','pub_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['average','project', 'user']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']