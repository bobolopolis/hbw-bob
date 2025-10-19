#!/usr/bin/env python3
'''Script to transcode a disc using HandBrake'''

import os
import subprocess
import sys

# Ripped with: dvdbackup -i /dev/sr0 -M -p

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

work_dir = '/mnt/raid/media/tv/Miss Fishers Murder Mysteries'
src_dirs = [f'{work_dir}/rip/Mfmm S1 D1',
            f'{work_dir}/rip/Mfmm S1 D2',
            f'{work_dir}/rip/Mfmm S1 D3',
            f'{work_dir}/rip/Mfmm S1 D4',
            f'{work_dir}/rip/Mfmm S2 D1',
            f'{work_dir}/rip/Mfmm S2 D2',
            f'{work_dir}/rip/Mfmm S2 D3',
            f'{work_dir}/rip/Mfmm S2 D4',
            f'{work_dir}/rip/Ms Fisher S3  Disc 1',
            f'{work_dir}/rip/Ms Fisher S3  Disc 2',
            f'{work_dir}/rip/Ms Fisher S3  Disc 3']

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
os.makedirs(f'{work_dir}/Series 2', exist_ok=True)
os.makedirs(f'{work_dir}/Series 2/extras', exist_ok=True)
os.makedirs(f'{work_dir}/Series 3', exist_ok=True)
os.makedirs(f'{work_dir}/Series 3/extras', exist_ok=True)

# Series 1 Disc 1
src_dir = src_dirs[0]

# 1: Copy warning
# 2: Acorn ad
# 3: Acorn ad
# 4: same as 5
transcode(f'{work_dir}/Series 1/s1e01 - Cocaine Blues.mkv',
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 6: same as 5
# 7: same as 8
transcode(f'{work_dir}/Series 1/s1e02 - Murder on the Ballarat Train.mkv',
          ['--input', f'{src_dir}',
           '--title', '8',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 9: same as 8
# 10: same as 11
transcode(f'{work_dir}/Series 1/s1e03 - The Green Mill Murder.mkv',
          ['--input', f'{src_dir}',
           '--title', '11',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 12: same as 11
# 13: same as 14
transcode(f'{work_dir}/Series 1/s1e04 - Death at Victoria Dock.mkv',
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 15: same as 14

# Series 1 Disc 2
src_dir = src_dirs[1]

# 1: Copy warning
# 2: same as 3
transcode(f'{work_dir}/Series 1/s1e05 - Raisins and Almonds.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 4: same as 3
# 5: same as 6
transcode(f'{work_dir}/Series 1/s1e06 - Ruddy Gore.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 7: same as 6
# 8: same as 9
transcode(f'{work_dir}/Series 1/s1e07 - Murder in Montparnasse.mkv',
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 10: same as 9

# Series 1 Disc 3
src_dir = src_dirs[2]

# 1: Copy warning
# 2: same as 3
transcode(f'{work_dir}/Series 1/s1e08 - Away with the Fairies.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 4: same as 3
# 5: same as 6
transcode(f'{work_dir}/Series 1/s1e09 - Queen of the Flowers.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 7: same as 6
# 8: same as 9
transcode(f'{work_dir}/Series 1/s1e10 - Death by Miss Adventure.mkv',
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 10: same as 9

# Series 1 Disc 4
src_dir = src_dirs[3]
# 1: Copy warning
# 2: same as 3
transcode(f'{work_dir}/Series 1/s1e11 - Blood and Circuses.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 4: same as 3
# 5: same as 6
transcode(f'{work_dir}/Series 1/s1e12 - Murder in the Dark.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 7: same as 6
# 8: same as 9
transcode(f"{work_dir}/Series 1/s1e13 - Kind Memses' Curse.mkv",
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# 10: same as 9
transcode(f"{work_dir}/Series 1/extras/The Look.mkv",
          ['--input', f'{src_dir}',
           '--title', '11',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Meet the Creators.mkv",
          ['--input', f'{src_dir}',
           '--title', '12',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Set Tour.mkv",
          ['--input', f'{src_dir}',
           '--title', '13',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Cast Interviews.mkv",
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Vehicles of the Series.mkv",
          ['--input', f'{src_dir}',
           '--title', '15',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Steam Train Experts.mkv",
          ['--input', f'{src_dir}',
           '--title', '16',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Locations of Melbourne.mkv",
          ['--input', f'{src_dir}',
           '--title', '17',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 1/extras/Photo Gallery.mkv",
          ['--input', f'{src_dir}',
           '--title', '18',
           '--audio', '1',
           '--aname', 'English'])

# Series 2 Disc 1
src_dir = src_dirs[4]

transcode(f'{work_dir}/Series 2/s2e01 - Murder Most Scandalous.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e02 - Death Comes Knocking.mkv',
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 2/s2e03 - Dead Man's Chest.mkv",
          ['--input', f'{src_dir}',
           '--title', '12',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e04 - Deadweight.mkv',
          ['--input', f'{src_dir}',
           '--title', '15',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Series 2 Disc 2
src_dir = src_dirs[5]

transcode(f'{work_dir}/Series 2/s2e05 - Murder a la Mode.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e06 - Marked for Murder.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e07 - Blood at the Wheel.mkv',
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Series 2 Disc 3
src_dir = src_dirs[6]

transcode(f'{work_dir}/Series 2/s2e08 - The Blood of Juana the Mad.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e09 - Framed for Murder.mkv',
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e10 - Death of the Vine.mkv',
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Series 2 Disc 4
src_dir = src_dirs[7]

transcode(f'{work_dir}/Series 2/s2e11 - Dead Air.mkv',
          ['--input', f'{src_dir}',
           '--title', '4',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e12 - Unnatural Habits.mkv',
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/s2e13 - Murder under the Mistletoe.mkv',
          ['--input', f'{src_dir}',
           '--title', '10',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Welcome to Season Two.mkv',
          ['--input', f'{src_dir}',
           '--title', '13',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Phryne Promo.mkv',
          ['--input', f'{src_dir}',
           '--title', '15',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Dot Promo.mkv',
          ['--input', f'{src_dir}',
           '--title', '17',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Jack Promo.mkv',
          ['--input', f'{src_dir}',
           '--title', '19',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Queenscliff.mkv',
          ['--input', f'{src_dir}',
           '--title', '21',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Boxing.mkv',
          ['--input', f'{src_dir}',
           '--title', '23',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Murder a la Mode.mkv',
          ['--input', f'{src_dir}',
           '--title', '25',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/House of Phryne.mkv',
          ['--input', f'{src_dir}',
           '--title', '27',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Football Message from Jack.mkv',
          ['--input', f'{src_dir}',
           '--title', '29',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/How to Become Dr. Mac.mkv',
          ['--input', f'{src_dir}',
           '--title', '31',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/The Cars.mkv',
          ['--input', f'{src_dir}',
           '--title', '33',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Winery.mkv',
          ['--input', f'{src_dir}',
           '--title', '35',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Essie Davis.mkv',
          ['--input', f'{src_dir}',
           '--title', '37',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Polly Woodside.mkv',
          ['--input', f'{src_dir}',
           '--title', '39',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Stunts.mkv',
          ['--input', f'{src_dir}',
           '--title', '41',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Guest Cast.mkv',
          ['--input', f'{src_dir}',
           '--title', '43',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Christmas.mkv',
          ['--input', f'{src_dir}',
           '--title', '45',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 2/extras/Aunt Prudence's Christmas Message.mkv",
          ['--input', f'{src_dir}',
           '--title', '47',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 2/extras/Season's Greetings from Phryne.mkv",
          ['--input', f'{src_dir}',
           '--title', '49',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 2/extras/Photo Gallery.mkv',
          ['--input', f'{src_dir}',
           '--title', '51',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Series 3 Disc 1
src_dir = src_dirs[8]

transcode(f'{work_dir}/Series 3/s3e01 - Death Defying Feats.mkv',
          ['--input', f'{src_dir}',
           '--title', '1',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/s3e02 - Murder and the Maiden.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/s3e03 - Murder and Mozzarella.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Old Fashioned.mkv",
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Sidecar.mkv",
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Champagne Punch.mkv",
          ['--input', f'{src_dir}',
           '--title', '8',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Series 3 Disc 2
src_dir = src_dirs[9]

transcode(f'{work_dir}/Series 3/s3e04 - Blood and Money.mkv',
          ['--input', f'{src_dir}',
           '--title', '1',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/s3e04 - Death and Hysteria.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/s3e05 - Death at the Grand.mkv',
          ['--input', f'{src_dir}',
           '--title', '3',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Sherry Cobbler.mkv",
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Martini.mkv",
          ['--input', f'{src_dir}',
           '--title', '7',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Fallen Angel.mkv",
          ['--input', f'{src_dir}',
           '--title', '8',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Series 3 Disc 3
src_dir = src_dirs[10]

transcode(f'{work_dir}/Series 3/s3e07 - Game, Set, and Murder.mkv',
          ['--input', f'{src_dir}',
           '--title', '1',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/s3e08 - Death Do Us Part.mkv',
          ['--input', f'{src_dir}',
           '--title', '2',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Maiden's Prayer.mkv",
          ['--input', f'{src_dir}',
           '--title', '5',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f"{work_dir}/Series 3/extras/Mr Butler's Drink of the Week - Negroni.mkv",
          ['--input', f'{src_dir}',
           '--title', '6',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Behind the Scenes Featurettes:
transcode(f'{work_dir}/Series 3/extras/Tony Tilse (Director).mkv',
          ['--input', f'{src_dir}',
           '--title', '8',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Robert Perkins (Production Designer).mkv',
          ['--input', f'{src_dir}',
           '--title', '9',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Greg J Walker (Composer).mkv',
          ['--input', f'{src_dir}',
           '--title', '10',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Anna Karpinski (Make Up and Hair Designer).mkv',
          ['--input', f'{src_dir}',
           '--title', '11',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Miriam Margoyles (Aunt Prudence).mkv',
          ['--input', f'{src_dir}',
           '--title', '12',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Roger Lanser (Director of Photography).mkv',
          ['--input', f'{src_dir}',
           '--title', '13',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Marion Boyce (Costume Designer).mkv',
          ['--input', f'{src_dir}',
           '--title', '14',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Death Do Us Part.mkv',
          ['--input', f'{src_dir}',
           '--title', '15',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Phryne: The Action Hero.mkv',
          ['--input', f'{src_dir}',
           '--title', '16',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])

# Character Clips:
transcode(f'{work_dir}/Series 3/extras/Bert and Cec.mkv',
          ['--input', f'{src_dir}',
           '--title', '18',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Aunt Prudence.mkv',
          ['--input', f'{src_dir}',
           '--title', '19',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Dot Williams.mkv',
          ['--input', f'{src_dir}',
           '--title', '20',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Hugh Collins.mkv',
          ['--input', f'{src_dir}',
           '--title', '21',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Jack Robinson.mkv',
          ['--input', f'{src_dir}',
           '--title', '22',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Henry Fisher.mkv',
          ['--input', f'{src_dir}',
           '--title', '23',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
transcode(f'{work_dir}/Series 3/extras/Dot Williams (Wedding).mkv',
          ['--input', f'{src_dir}',
           '--title', '24',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
# Behind the Scenes Photo Gallery
transcode(f'{work_dir}/Series 3/extras/Photo Gallery.mkv',
          ['--input', f'{src_dir}',
           '--title', '25',
           '--audio', '1',
           '--aname', 'English',
           '--subtitle', '1',
           '--subname', 'English'])
