"""
Purpose: create an SFZ file (see https://sfzformat.com/tutorials/drum_basics) 
that maps one shots across the keyboard (a la http://mildon.me/beagle.php?b=view&id=UVIU)

process_one_dir takes as input a path to one directory of one shots it creates
an SFZ file that maps the one shots across the keyboard to adjacent keys

__main__: runs process_one_dir for every subdirectory in a root directory for
batch processing
"""

import os
import argparse

def process_one_dir(rootdir, oneshotdir, file_ending='wav'):

    # get a listing of the one shots and sort them
    listing = os.listdir(os.path.join(rootdir, oneshotdir))

    # filter by file_ending (want to ignore crap like .DS_Store)
    listing = [l for l in listing if l.split('.')[-1] == file_ending]

    # sort 
    # (use case: one shorts have same prefix and suffices 001,002,.. as generate by recycle)
    listing.sort() 

    # start from C1
    start_note = 36

    # write output to the root dir
    output_fname = oneshotdir + '.sfz'
    output_fpath = os.path.join(rootdir, output_fname) 

    with open(output_fpath, 'w') as f: 
        for idx, l in enumerate(listing):
            out_str = "<region> sample=%s/%s key=%d" % (oneshotdir, l, start_note+idx)
            print(out_str)
            f.write(out_str + '\n')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Create SFZ instrument from one shots.')
    parser.add_argument('--rootdir', help="Top level directory containing folders of one shots")
    args = parser.parse_args()

    rootdir = os.path.expanduser(args.rootdir)

    # get all subdirs in rootdir
    subdirs = next(os.walk(rootdir))[1]

    for oneshotdir in subdirs:
        process_one_dir(rootdir, oneshotdir)
