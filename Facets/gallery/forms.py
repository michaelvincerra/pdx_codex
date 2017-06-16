"""
Forms for Update and Delete of Media Records. 

"""
from django import forms
from .models import Media

#Write your forms here.
# This is a DJANGO model form.

class MediaModelForm(forms.ModelForm):

    """
    A model forms for manipulating Media records. 
    """

    class Meta:
        model = Media
        fields = ('name', 'type', 'file', 'is_published', 'tags')  # Fields that are shown to the user.

# CUSTOM VALIDATOR
    # def validate_name(self):
    #     if self.name == 'Michael':
    #         raise ValidationError()
