import os
from django.contrib.gis.utils import LayerMapping
from .models import IsleifPoints

isleif_mapping = {
    # 'x' : 'X',
    # 'y' : 'Y',
    'samtala' : 'Samtala',
    'geom' : 'POINT',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Isleif', 'Isleif.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        IsleifPoints, world_shp, isleif_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
    run2()

from .models import WorldBorder

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

world2_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),
)

def run2(verbose=True):
    lm2 = LayerMapping(
        WorldBorder, world2_shp, world_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm2.save(strict=True, verbose=verbose)
