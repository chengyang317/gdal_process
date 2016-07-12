# -*- coding: UTF-8 -*-
# File: create_timesat_filelist
# Author: Philip Cheng
# Time: 7/9/16 -> 2:48 PM
import os
import glob


bin_dir = "/scratch/dian/bin/evi_c"

years = range(2010, 2013)

bin_files = glob.glob(os.path.join(bin_dir, '*.bin'))


selected_bin_files = []
for year in years:
    files_of_year = [bin_file for bin_file in bin_files if os.path.basename(bin_file).startswith("us" + str(year))]
    selected_bin_files.extend(sorted(files_of_year, key=lambda x: int(os.path.basename(x)[5:os.path.basename(x).find('.')])))

file_list_name = "from_{}_to_{}_files.txt".format(str(years[0]), str(years[-1]))
with open(os.path.join(bin_dir, file_list_name), 'w') as fs:
    fs.write(str(len(selected_bin_files)) + "\n")
    for selected_bin_file in selected_bin_files:
        fs.write((selected_bin_file + "\n"))
