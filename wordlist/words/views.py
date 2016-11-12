from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from wordlist.words.models import Word
from wordlist.words.forms import WordForm


def home(request):
    """
    """
    words = Word.objects.all()
    return render(request, 'words/home.html', {
        "words": words
    })


def create(request):
    """
    """
    return _edit(request, word_id=None)


def edit(request, word_id):
    """
    """
    return _edit(request, word_id)


def _edit(request, word_id):
    """
    """
    if word_id is None:
        word = None
    else:
        word = get_object_or_404(Word, pk=word_id)

    if request.POST:
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save()
            if word_id:
                messages.success(request, "Updated")
            else:
                messages.success(request, "New Word Created")
            return HttpResponseRedirect(reverse('home'))
    else:
        form = WordForm(instance=word)

    return render(request, "words/edit.html", {
        "form": form,
        "word_id": word_id,
    })
