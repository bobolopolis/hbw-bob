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

work_dir = '/mnt/raid/media/tv/Octonauts'
src_dirs = [f'{work_dir}/rip/Octonauts Season 1 Disc1',
            f'{work_dir}/rip/Octonauts Season 1 Disc2',
            f'{work_dir}/rip/Octonauts Season 1 Disc 3',
            f'{work_dir}/rip/Octonauts Season 1 Disc 4']

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
    
os.makedirs(f'{work_dir}/Season 1', exist_ok=True)
os.makedirs(f'{work_dir}/Season 1/extras', exist_ok=True)
src_dir = src_dirs[0]

# 1: all episodes
transcode(f'{work_dir}/Season 1/s01e02 - Octonauts and the Undersea Storm.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e06 - Octonauts and the Giant Squid.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e08 - Octonauts and the Great Algae Escape.mkv',
          ['--input', f'{src_dir}',
           '--title', '4',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e04 - Octonauts and the Walrus Chief.mkv',
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e05 - Octonauts and the Flying Fish.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e17 - Octonauts and the Narwhal.mkv',
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 8: creature report
# 9: creature report
# 10: creature report
# 11: creature report
# 12: creature report
# 13: creature report
transcode(f'{work_dir}/Season 1/s01e12 - Octonauts and the Moster Map.mkv',
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 15: creature report
transcode(f'{work_dir}/Season 1/s01e03 - Octonauts and the Crab and Urchin.mkv',
          ['--input', f'{src_dir}',
           '--title', '16',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 17: creature report
transcode(f'{work_dir}/Season 1/s01e14 - Octonauts and the Albino Humpback Whale.mkv',
          ['--input', f'{src_dir}',
           '--title', '18',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e09 - Octonauts and the Remipedes.mkv',
          ['--input', f'{src_dir}',
           '--title', '19',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e07 - Octonauts and the Orcas.mkv',
          ['--input', f'{src_dir}',
           '--title', '20',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e11 - Octonauts and the Blobfish Brothers.mkv',
          ['--input', f'{src_dir}',
           '--title', '21',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e25 - Octonauts and the Decorator Crab.mkv',
          ['--input', f'{src_dir}',
           '--title', '22',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e01 - Octonauts and the Whale Shark.mkv',
          ['--input', f'{src_dir}',
           '--title', '23',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 25: creature report
# 26: creature report
# 27: creature report
# 28: creature report
# 29: creature report
# 30: creature report
# 32: copy warning
# 33: Floogals ad
# 34: kiwi, mac & moxy, dino dan ads
# 37: gumby ad

src_dir = src_dirs[1]
# 1: all episodes
transcode(f'{work_dir}/Season 1/s01e31 - Octonauts and the Cookiecutter Sharks.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e34 - Octonauts and the Jellyfish Bloom.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e10 - Octonauts and the Speedy Sailfish.mkv',
          ['--input', f'{src_dir}',
           '--title', '4',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e28 - Octonauts and the Vampire Squid.mkv',
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f"{work_dir}/Season 1/s01e49 - Octonauts and the Humuhumunukunukuapua'a.mkv",
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e50 - Octonauts and the Giant Spider Crab.mkv',
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 8-13: creature report
transcode(f'{work_dir}/Season 1/s01e15 - Octonauts and the Giant Kelp Forest.mkv',
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 15: creature report
transcode(f'{work_dir}/Season 1/s01e22 - Octonauts and the Hermit Crabs.mkv',
          ['--input', f'{src_dir}',
           '--title', '16',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 17: creature report
transcode(f'{work_dir}/Season 1/s01e27 - Octonauts and the Hungry Pilot Fish.mkv',
          ['--input', f'{src_dir}',
           '--title', '18',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e26 - Octonauts and the Beluga Whales.mkv',
          ['--input', f'{src_dir}',
           '--title', '19',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e20 - Octonauts and the Snot Sea Cucumber.mkv',
          ['--input', f'{src_dir}',
           '--title', '20',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e21 - Octonauts and the Giant Whirlpool.mkv',
          ['--input', f'{src_dir}',
           '--title', '21',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e38 - Octonauts and the Slime Eels.mkv',
          ['--input', f'{src_dir}',
           '--title', '22',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e37 - Octonauts and the Arctic Orcas.mkv',
          ['--input', f'{src_dir}',
           '--title', '23',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 25-30: creature report
# 32: copy warning
# 33: little wolf's book of badness, the day henry met... ads
# 34: the cat in the hat knows a lot about camping, thomas edison's secret lab ads

src_dir = src_dirs[2]
# 1: all episodes
transcode(f'{work_dir}/Season 1/s01e13 - Octonauts and the Lost Sea Star.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e30 - Octonauts and the Giant Jelly.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e19 - Octonauts and the Snapping Shrimp.mkv',
          ['--input', f'{src_dir}',
           '--title', '4',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e24 - Octonauts and the Kelp Forest Rescue.mkv',
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e39 - Octonauts and the Enormous Elephant Seal.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e40 - Octonauts and the Saradine School.mkv',
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 8-13: creature report
transcode(f'{work_dir}/Season 1/s01e42 - Octonauts and the Eel Ordeal.mkv',
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 15: creature report
transcode(f'{work_dir}/Season 1/s01e41 - Octonauts and the Dolphin Reef Rescue.mkv',
          ['--input', f'{src_dir}',
           '--title', '16',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 17: creature report
transcode(f'{work_dir}/Season 1/s01e45 - Octonauts and the Pirate Parrotfish.mkv',
          ['--input', f'{src_dir}',
           '--title', '18',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e46 - Octonauts and the Electric Torpedo Rays.mkv',
          ['--input', f'{src_dir}',
           '--title', '19',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e18 - Octonauts and the Midnight Zone.mkv',
          ['--input', f'{src_dir}',
           '--title', '20',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e23 - Octonauts and the Mixed Up Whales.mkv',
          ['--input', f'{src_dir}',
           '--title', '21',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e29 - Octonauts and the Seahorse Tale.mkv',
          ['--input', f'{src_dir}',
           '--title', '22',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e16 - Octonauts and the Enemy Anemones.mkv',
          ['--input', f'{src_dir}',
           '--title', '23',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 25-30: creature report
# 32: copy warning
# 33: ads
# 34: ads

src_dir = src_dirs[3]
# 1: all episodes
transcode(f'{work_dir}/Season 1/s01e47 - Octonauts and the Crafty Cuttlefish.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e48 - Octonauts and the Lost Lemon Shark.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e35 - Octonauts and the Baby Dolphin.mkv',
          ['--input', f'{src_dir}',
           '--title', '4',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e36 - Octonauts and the Scary Spookfish.mkv',
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e32 - Octonauts and the Oarfish.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/s01e33 - Octonauts and the Combtooth Blenny.mkv',
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 8-13: creature report
transcode(f'{work_dir}/Season 1/s01e43 - Octonauts and the Marine Iguanas.mkv',
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 15: creature report
transcode(f'{work_dir}/Season 1/s01e44 - Octonauts and the Dwarf Lanternshark.mkv',
          ['--input', f'{src_dir}',
           '--title', '16',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 17: creature report
transcode(f'{work_dir}/Season 1/extras/Octonauts and the Great Penguin Race.mkv',
          ['--input', f'{src_dir}',
           '--title', '18',
           '--audio', '1,2',
           '--aname', 'English,español'])
transcode(f'{work_dir}/Season 1/extras/Octonauts and the Great Christmas Rescue.mkv',
          ['--input', f'{src_dir}',
           '--title', '19',
           '--audio', '1,2',
           '--aname', 'English,español'])
# 22: white screen?
# 23: ads
# 24: ads
