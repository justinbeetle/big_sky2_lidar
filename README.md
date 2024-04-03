# Big Sky 2 LIDAR Data

Convert [USGS LIDAR data](https://www.sciencebase.gov/catalog/item/613de9e5d34e40dd9c126360) in the
[LAZ file format](https://rockyweb.usgs.gov/vdelivery/Datasets/Staged/Elevation/LPC/Projects/SD_Southwest_NRCS_SD_2018_D18/SD_Southwest_B5_2018/LAZ/USGS_LPC_SD_Southwest_NRCS_SD_2018_D18_13TFJ030190.laz)
or [USGS digital elevation model (DEM) data](https://www.sciencebase.gov/catalog/item/62e36c45d34e394b653654ce) in the
[TIF file format](https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/SD_Southwest_NRCS_SD_2018_D18/TIFF/USGS_1M_13_x60y482_SD_Southwest_NRCS_SD_2018_D18.tif)
into a txt file of X, Y, Z coordinate csv files which can be used to
[import terrain](https://www.homedesignersoftware.com/videos/watch/2265/importing-terrain-data-from-gps-or-text-file.html?playlist=201)
into [Home Designer](https://www.homedesignersoftware.com/).

The DEM GeoTiff provides the ground elevation while the LIDAR data points also include the vegetation.

## Dependencies

* [geotiff](https://github.com/KipCrossing/geotiff): Python library for parsing geotiff files
* [laspy](https://github.com/laspy/laspy): Python library for parsing las and laz files.
* [laz-rs](https://github.com/laz-rs/laz-rs): Rust library for laz decompression.
* [laz-rs-python](https://github.com/laz-rs/laz-rs-python): Python bindings for laz-rs (allows laz support with laspy).
* [utm](https://github.com/Turbo87/utm): Python library supporting coordinate transformations between WGS-84 geodetic
lat/lon and UTM x/y coordinate transformations.