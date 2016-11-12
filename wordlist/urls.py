from django.conf.urls import url
from django.contrib import admin
from wordlist.words import views as words


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', words.home, name='home'),
    url(r'^new/', words.create, name='words-create'),
    url(r'^edit/(?P<word_id>\d+)/?$', words.edit, name='words-edit'),
]
