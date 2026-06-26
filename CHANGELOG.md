Changelog
=========

v0.0.3.dev
------------------------------------------------------------
- Reduce computational load of disaggretation by re-organising code and allowing parallelisation with dask [#18](https://github.com/modelblocks-org/gregor/pull/18).
- Add a more computationally expensive performance test, which disaggregates rooftop PV capacities in Europe, to be run locally [#18](https://github.com/modelblocks-org/gregor/pull/18).
- Add CI testing [#19](https://github.com/modelblocks-org/gregor/pull/19).
- Add more unit tests [#17](https://github.com/modelblocks-org/gregor/pull/17).
- Fix failing aggregation when polygon index is unnamed [#14](https://github.com/modelblocks-org/gregor/pull/14).


v0.0.2 (2024-11-21)
------------------------------------------------------------
- Add a function that allows to disaggregate polygons to points [#5](https://github.com/jnnr/gregor/pull/5).
- Rearrange CLI to offer disaggregation and aggregation to/from raster and points [#5](https://github.com/jnnr/gregor/pull/5).
- Fix CLI example [#7](https://github.com/jnnr/gregor/pull/7).
- Accomodate for geopandas API change and raise FutureWarning  [#6](https://github.com/jnnr/gregor/pull/6).
- Extend readme [#8](https://github.com/jnnr/gregor/pull/8)

v0.0.1 (2024-08-12)
------------------------------------------------------------
- Initial release