import os
from django.contrib.gis.utils import LayerMapping
from .models import IsleifPoints

isleif_mapping = {
    'x' : 'X',
    'y' : 'Y',
    'samtala' : 'Samtala',
    'geom' : 'MULTIPOINT',
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
