from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from wordlist.words.models import Word


def home(request):
    """
    """
    words = Word.objects.all()
    return render(request, 'words/home.html', {
        "words": words
    })
