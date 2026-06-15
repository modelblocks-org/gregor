from gregor.disaggregate import disaggregate_polygon_to_raster
import pytest
import numpy as np
from memory_log import MemoryLogger


@pytest.mark.benchmark
def test_performance_disaggregate_to_raster(large_raster, large_polygons):
    data = large_polygons.copy()
    data["value"] = np.random.rand(len(data))
    mlogger = MemoryLogger(interval_sec=0.5)
    mlogger.start()

    disaggregate_polygon_to_raster(
        data=data,
        column="value",
        proxy=large_raster,
    )    
    mlogger.stop()
    mlogger.save_csv("test/performance_disaggregate_to_raster.csv")
