from django.conf.urls import url
from django.contrib import admin
from wordlist.home import views as home


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.home, name='home'),
]
