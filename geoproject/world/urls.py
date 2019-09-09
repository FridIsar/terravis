from django.conf.urls import url
from . import views


app_name = 'world'

urlpatterns = [
    # city detail view
    url(r'^country/(?P<pk>[0-9]+)$',
        views.CountriesDetailView.as_view(), name='country-detail'),
]
