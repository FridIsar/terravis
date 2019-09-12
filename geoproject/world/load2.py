import os
from django.contrib.gis.utils import LayerMapping
from .models import IsleifPoints

world_mapping = {
    'name' : 'Hlutverk',
    'lon' : 'X (A)',
    'lat' : 'Y (N)',
    'point' : 'POINT',
}

world_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Isleif', 'Isleif.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        IsleifPoints, world_shp, world_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
