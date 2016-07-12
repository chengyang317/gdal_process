# -*- coding: UTF-8 -*-
# File: tif_to_bin
# Author: Philip Cheng
# Time: 7/9/16 -> 2:33 PM
import gdal
import glob
import os

tif_dir = "/run/media/chenyang/Seagate Backup Plus Drive/evi_deci_national/evi_region/evi_C"
bin_dir = "/scratch/dian/bin/evi_c"

tif_files = glob.glob(os.path.join(tif_dir, "*.tif"))
driver = gdal.GetDriverByName("ENVI")

for tif_file in tif_files:
    src_ds = gdal.Open(tif_file)
    dst_file_path = os.path.join(bin_dir, os.path.basename(tif_file)[:-4] + ".bin")
    if os.path.exists(dst_file_path):
        continue
    print("Process {}".format(dst_file_path))
    dst_ds = driver.CreateCopy(dst_file_path, src_ds, 0)
    src_ds = None
    dst_ds = None

