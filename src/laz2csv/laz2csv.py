#!/usr/bin/env python
""" TODO """

# Imports to support type annotations
from typing import Tuple, Union

import geotiff
import laspy
import utm
import traceback


def main() -> None:
    laz_filename = "data/USGS_LPC_SD_Southwest_NRCS_SD_2018_D18_13TFJ030190.laz"
    tif_filename = "data/USGS_1M_13_x60y482_SD_Southwest_NRCS_SD_2018_D18.tif"
    laz_csv_filename = "data/laz_xyz.csv"
    tif_csv_filename = "data/tif_xyz.csv"

    # Corner coordinates for lot
    nw_corner_lat = 43.52039
    nw_corner_lon = -103.72338
    se_corner_lat = 43.51859
    se_corner_lon = -103.72213

    # FUTURE: Download files

    # laz to xyz csv
    corner_coords = utm.from_latlon(nw_corner_lat, nw_corner_lon), utm.from_latlon(se_corner_lat, se_corner_lon)
    min_x, max_x = sorted(coord[0] for coord in corner_coords)
    min_y, max_y = sorted(coord[1] for coord in corner_coords)
    with open(laz_csv_filename, "w") as csv_file:
        with laspy.open(laz_filename) as las_reader:
            for points in las_reader.chunk_iterator(2**16):
                x, y = points.x.copy(), points.y.copy()
                mask = (min_x <= x) & (x <= max_x) & (min_y <= y) & (y <= max_y)
                for point in points[mask]:
                    point_x = point.array[0] * point.scales[0]
                    point_y = point.array[1] * point.scales[1]
                    point_z = point.array[2] * point.scales[2]
                    csv_file.write(f"{point_x},{point_y},{point_z}\n")  # meters

    # geotiff to xyz csv
    with open(tif_csv_filename, "w") as csv_file:
        geo_tiff = geotiff.GeoTiff(tif_filename)
        points = geo_tiff.read_box([(nw_corner_lon, nw_corner_lat), (se_corner_lon, se_corner_lat)])

        for y, x_points in enumerate(reversed(points)):
            for x, z in enumerate(x_points):
                csv_file.write(f"{x},{y},{z}\n")  # meters


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()