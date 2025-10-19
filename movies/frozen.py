#!/usr/bin/env python3
'''Script to transcode a disc using HandBrake'''

import os
import subprocess
import sys

# ripped with:
# dvdbackup -i /dev/sr0 -M -p -o .

def transcode(out, options):
    '''Call HandBrakeCLI with specified options.'''
    if os.path.isfile(out):
        print(f'File {out} exists, skipping')
    else:
        cmd = ['HandBrakeCLI',
               '--preset', 'AV1 MKV 2160p60 4K',
               '--output', f'{out}']
        cmd.extend(options)
        subprocess.run(cmd, check=True)

work_dir = '/mnt/raid/media/movies/Frozen (2013)'
src_dirs = [f'{work_dir}/rip/Frozen']

for src_dir in src_dirs:
    scan_file = f'{src_dir}.scan'
    if not os.path.exists(scan_file):
        print('Scanning...')
        with open(scan_file, 'w', encoding='utf8') as scan:
            subprocess.run(['HandBrakeCLI',
                            '-i', src_dir,
                            '--scan',
                            '--title', '0'],
                            stdout=scan,
                            stderr=subprocess.STDOUT, check=True)

os.makedirs(f'{work_dir}/extras', exist_ok=True)
src_dir = src_dirs[0]

transcode(f'{work_dir}/Frozen (2013).mkv',
          ['--input', f'{src_dir}',
           '--title', '1',
           '--angle', '1',
           '--audio', '1,2,3,4',
           '--aname', 'English,English Visually Impaired,Francais,español',
           '--subtitle', '1,2,3,4,5,6,7,8,9',
           '--subname', 'English CC Wide Screen,English CC Letterbox,English Wide Screen,English Letterbox,Francais Wide Screen,Francais Letterbox,español Wide Screen,español Letterbox,English CC'])
transcode(f'{work_dir}/extras/Mickey Mouse - Get a Horse.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1,2,3,4',
           '--aname', 'English,English Visually Impaired,Francais,español',
           '--subtitle', '1,2,3,4,5,6,7,8,9,10,11',
           '--subname', 'English CC Wide Screen,English CC Letterbox,English Wide Screen,English Letterbox,Francais Wide Screen,Francais Letterbox,español Wide Screen,español Letterbox,español Wide Screen,español Letterbox,English CC'])
transcode(f'{work_dir}/extras/Let it Go (Demi Lovato Version).mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English'])
transcode(f'{work_dir}/extras/Let it Go (Martina Stoessel Version - Libre Soy.mkv',
          ['--input', f'{src_dir}',
           '--title', '4',
           '--audio', '1',
           '--aname', 'español'])
transcode(f"{work_dir}/extras/Let it Go (Martina Stoessel Version - All'alba Sorgero).mkv",
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1',
           '--aname', 'italiano'])
transcode(f'{work_dir}/extras/Let it Go (Marsha Milan Version).mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'Bahasa Melayu'])
transcode(f'{work_dir}/extras/Trailer.mkv',
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1',
           '--aname', 'English'])
# 12: Disney Fast Play menu
# 15: Disney DVD logo
# 16: Disney logo
