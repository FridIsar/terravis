# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView

from django.core import serializers

from .models import WorldBorder, IsleifPoints

import time

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
        # allpoints = []
        # t0 = time.time()
        # for point in IsleifPoints.objects.all():
        #     allpoints.append(point.geom.geojson)
        # context['isleifpoints'] = allpoints
        # obj = context['object']
        # print("area :"+str(obj.lat));
        # context['country_mpoly'] = obj.mpoly.geojson
        # t1 = time.time()
        # print allpoints
        # print("Converting to geojson took "+str(t1-t0)+" ms.")
        t0 = time.time()
        allfastpoints = serializers.serialize("geojson", IsleifPoints.objects.all(), fields=('samtala', 'geom'))
        t1 = time.time()
        # allfastpoints = {"IsleifPoints_json": IsleifPoints_json}
        print("Converting to geojson took "+str(t1-t0)+" ms.")
        context['isleifall'] = allfastpoints
        return context
