import shutil
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

import geopandas as gpd
import pandas as pd
import pytest
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


@pytest.fixture(scope="session")
def large_test_files() -> Path:
    """Download and unzip test files."""
    TEST_FILES = "https://zenodo.org/records/16779120/files/test_suite.zip"
    path_test_files = Path("test/tmp/")
    # If test suite has been downloaded, assume everything is OK.
    # Otherwise, cleanup and re-download.
    if not Path(path_test_files / "test_suite.zip").exists():
        shutil.rmtree(path_test_files, ignore_errors=True)
        Path(path_test_files).mkdir(parents=True, exist_ok=True)
        test_zip = Path(path_test_files / "test_suite.zip")
        urlretrieve(TEST_FILES, test_zip)
        with zipfile.ZipFile(test_zip, "r") as zfile:
            zfile.extractall(path_test_files)
    return path_test_files


@pytest.fixture(scope="session")
def large_raster(large_test_files):
    return rxr.open_rasterio(large_test_files / "europe/proxies/rooftop_pv.tif").squeeze(drop=True)


@pytest.fixture(scope="session")
def large_polygons(large_test_files):
    return gpd.read_parquet(large_test_files / "europe/shapes.parquet")
