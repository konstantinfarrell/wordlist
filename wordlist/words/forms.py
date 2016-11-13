from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse

from wordlist.words.models import Word


class WordForm(forms.ModelForm):
    """
    Form for creating and editing a word entry.
    """
    phonetic = forms.CharField(required=False)
    part_of_speech = forms.CharField(required=False)
    language = forms.CharField(required=False)
    definition = forms.CharField(required=False)
    attribution = forms.CharField(required=False)
    notes = forms.CharField(required=False)

    class Meta:
        model = Word
        fields = (
            'word',
        )

    def __init__(self, *args, **kwargs):
        super(WordForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        """
        cleaned_data = super(WordForm, self).clean()
        return cleaned_data

    def in_create_mode(self):
        """
        """
        return self.instance.pk is None

    def save(self, *args, **kwargs):
        """
        """
        in_create_mode = self.in_create_mode()
        word = super(WordForm, self).save(*args, **kwargs)
        return word
