import pandas as pd

import pytest
import geopandas as gpd
import rioxarray as rxr


@pytest.fixture
def dummy_raster():
    return rxr.open_rasterio("test/_files/raster.tif").squeeze(drop=True)


@pytest.fixture
def square_segmentation_2x2():
    return gpd.read_file("test/_files/segmentation_2x2.geojson").set_index("id")


@pytest.fixture
def square_segmentation_3x3():
    return gpd.read_file("test/_files/segmentation_3x3.geojson").set_index("id")


@pytest.fixture
def polygon_segmentation():
    return gpd.read_file("test/_files/segmentation_polygon.geojson").set_index("id")


@pytest.fixture
def points():
    return gpd.read_file("test/_files/points.geojson")


@pytest.fixture
def points_NL():
    return gpd.read_file("docs/examples/data/cities.geojson")


@pytest.fixture
def raster_NL():
    return rxr.open_rasterio("docs/examples/data/population_small.tif").squeeze(drop=True)


@pytest.fixture
def polygons_NUTS3_NL():
    return gpd.read_file("docs/examples/data/boundaries_NUTS3.geojson")


@pytest.fixture
def demand_NUTS0_NL():
    demand = pd.read_csv("docs/examples/data/demand.csv", index_col=0)
    polygons = gpd.read_file("docs/examples/data/boundaries_NUTS0.geojson")
    demand_NUTS0_NL = polygons.join(demand)
    return demand_NUTS0_NL
