# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis import admin
from .models import WorldBorder

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
# Register your models here.
