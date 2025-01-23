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

work_dir = '/mnt/raid/media/tv/Peppa Pig'
src_dirs = [f'{work_dir}/rip/Peppa Pig S1d1',
            f'{work_dir}/rip/Peppa Pig S1d2']

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
    
os.makedirs(f'{work_dir}/Series 1', exist_ok=True)
os.makedirs(f'{work_dir}/Series 1/extras', exist_ok=True)
src_dir = src_dirs[0]

# 17: logo
# 18: logo
transcode(f'{work_dir}/Series 1/s01e01 - Muddy Puddles.mkv',
          ['--input', f'{src_dir}',
           '--title', '70',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e02 - Mr Dinosaur is Lost.mkv',
          ['--input', f'{src_dir}',
           '--title', '71',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e03 - Best Friend.mkv',
          ['--input', f'{src_dir}',
           '--title', '72',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e04 - Polly Parrot.mkv',
          ['--input', f'{src_dir}',
           '--title', '73',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e05 - Hide and Seek.mkv',
          ['--input', f'{src_dir}',
           '--title', '74',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e06 - The Playgroup.mkv',
          ['--input', f'{src_dir}',
           '--title', '75',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e07 - Mummy Pig at Work.mkv',
          ['--input', f'{src_dir}',
           '--title', '76',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e08 - Piggy in the Middle.mkv',
          ['--input', f'{src_dir}',
           '--title', '77',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e09 - Daddy Loses His Glasses.mkv',
          ['--input', f'{src_dir}',
           '--title', '78',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e10 - Gardening.mkv',
          ['--input', f'{src_dir}',
           '--title', '79',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e11 - Hiccups.mkv',
          ['--input', f'{src_dir}',
           '--title', '80',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e12 - Bicycles.mkv',
          ['--input', f'{src_dir}',
           '--title', '81',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e13 - Secrets.mkv',
          ['--input', f'{src_dir}',
           '--title', '82',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e14 - Flying a Kite.mkv',
          ['--input', f'{src_dir}',
           '--title', '83',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e15 - Picnic.mkv',
          ['--input', f'{src_dir}',
           '--title', '84',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e16 - Musical Instruments.mkv',
          ['--input', f'{src_dir}',
           '--title', '85',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e17 - Frogs and Worms and Butterflies.mkv',
          ['--input', f'{src_dir}',
           '--title', '86',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e18 - Dressing Up.mkv',
          ['--input', f'{src_dir}',
           '--title', '87',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e19 - New Shoes.mkv',
          ['--input', f'{src_dir}',
           '--title', '88',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e20 - The School Fete.mkv',
          ['--input', f'{src_dir}',
           '--title', '89',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e21 - Mummy Pigs Birthday.mkv',
          ['--input', f'{src_dir}',
           '--title', '90',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e22 - The Tooth Fairy.mkv',
          ['--input', f'{src_dir}',
           '--title', '91',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e23 - The New Car.mkv',
          ['--input', f'{src_dir}',
           '--title', '92',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e24 - Treasure Hunt.mkv',
          ['--input', f'{src_dir}',
           '--title', '93',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e25 - Not Very Well.mkv',
          ['--input', f'{src_dir}',
           '--title', '94',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e26 - Snow.mkv',
          ['--input', f'{src_dir}',
           '--title', '95',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])

src_dir = src_dirs[1]

transcode(f'{work_dir}/Series 1/s01e27 - Windy Castle.mkv',
          ['--input', f'{src_dir}',
           '--title', '70',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e28 - My Cousin Chloé.mkv',
          ['--input', f'{src_dir}',
           '--title', '71',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e29 - Pancakes.mkv',
          ['--input', f'{src_dir}',
           '--title', '72',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e30 - Babysitting.mkv',
          ['--input', f'{src_dir}',
           '--title', '73',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e31 - Ballet Lesson.mkv',
          ['--input', f'{src_dir}',
           '--title', '74',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e32 - Thunderstorm.mkv',
          ['--input', f'{src_dir}',
           '--title', '75',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e33 - Cleaning the Car.mkv',
          ['--input', f'{src_dir}',
           '--title', '76',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e34 - Lunch.mkv',
          ['--input', f'{src_dir}',
           '--title', '77',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e35 - Camping.mkv',
          ['--input', f'{src_dir}',
           '--title', '78',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e36 - The Sleepy Princess.mkv',
          ['--input', f'{src_dir}',
           '--title', '79',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e37 - The Tree House.mkv',
          ['--input', f'{src_dir}',
           '--title', '80',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e38 - Fancy Dress Party.mkv',
          ['--input', f'{src_dir}',
           '--title', '81',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e39 - The Museum.mkv',
          ['--input', f'{src_dir}',
           '--title', '82',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e40 - Very Hot Day.mkv',
          ['--input', f'{src_dir}',
           '--title', '83',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/s01e41 - Chloé's Puppet Show.mkv",
          ['--input', f'{src_dir}',
           '--title', '84',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e42 - Daddy Gets Fit.mkv',
          ['--input', f'{src_dir}',
           '--title', '85',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e43 - Tidying Up.mkv',
          ['--input', f'{src_dir}',
           '--title', '86',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e44 - The Playground.mkv',
          ['--input', f'{src_dir}',
           '--title', '87',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e45 - Daddy Puts up a Picture.mkv',
          ['--input', f'{src_dir}',
           '--title', '88',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e46 - At the Beach.mkv',
          ['--input', f'{src_dir}',
           '--title', '89',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e47 - Mister Skinnylegs.mkv',
          ['--input', f'{src_dir}',
           '--title', '90',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/s01e48 - Grandpa Pig's Boat.mkv",
          ['--input', f'{src_dir}',
           '--title', '91',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e49 - Shopping.mkv',
          ['--input', f'{src_dir}',
           '--title', '92',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e50 - My Birthday Party.mkv',
          ['--input', f'{src_dir}',
           '--title', '93',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/s01e51 - Daddy's Movie Camera.mkv",
          ['--input', f'{src_dir}',
           '--title', '94',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 1/s01e52 - School Play.mkv',
          ['--input', f'{src_dir}',
           '--title', '95',
           '--audio', '1,2',
           '--aname', 'English,French',
           '--subtitle', '1',
           '--subname', 'English'])
