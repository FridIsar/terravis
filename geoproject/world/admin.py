# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.gis import admin
from .models import WorldBorder, IsleifPoints

admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(IsleifPoints, admin.OSMGeoAdmin)
# Register your models here.
