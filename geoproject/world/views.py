# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView

from .models import WorldBorder

# Create your views here.


class CountriesDetailView(DetailView):
    """
        Countries detail view.
    """
    template_name = 'country-detail.html'
    model = WorldBorder
    def get_context_data(self, **kwargs): #recupere le contexte de la vue generique
        context = super(DetailView, self).get_context_data(**kwargs)
        context['mapbox_token'] = 'pk.eyJ1IjoibmlkbHkiLCJhIjoiY2swY2tyaGx5MDBscDNucG1ycm9pZG1tMSJ9.Npj4mCdM7VhNQmYcfMxcpA'
        obj = context['object']
        context['country_mpoly'] = obj.mpoly.geojson;
        print("area :"+str(obj.lat));
        return context
