import numpy as np
import pytest
from memory_log import MemoryLogger

from gregor.disaggregate import disaggregate_polygon_to_raster


@pytest.mark.benchmark
def test_performance_disaggregate_to_raster(large_raster, large_polygons):
    data = large_polygons.copy()
    data["value"] = np.random.rand(len(data))
    mlogger = MemoryLogger(interval_sec=0.5)
    mlogger.start()

    large_raster_chunked = large_raster.chunk("auto")

    disaggregate_polygon_to_raster(
        data=data,
        column="value",
        proxy=large_raster_chunked,
    )
    mlogger.stop()
    mlogger.save_csv("test/performance_disaggregate_to_raster.csv")
