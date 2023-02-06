"""
Author: rahul.savani@gmail.com

Creates an SFZ file (see https://sfzformat.com/tutorials/drum_basics) that 
maps each oneshot across the whole keyboard

and uses the pitch in the filename as the root (pitch_keycenter)

The function process_one_dir takes as input a path to one directory of one shots
and it creates an SFZ filefor each one of them

__main__ runs process_one_dir for every subdirectory in a root directory for
batch processing

"""

import os
import argparse
import sys

def process_one_dir(rootdir, oneshotdir, file_ending='wav'):

    # get a listing of the one shots and sort them
    listing = os.listdir(os.path.join(rootdir, oneshotdir))

    # filter by file_ending (want to ignore crap like .DS_Store)
    listing = [l for l in listing if l.split('.')[-1] == file_ending]

    # sort 
    # (use case: one shots have same prefix and suffices 001,002,.. as generate by recycle)
    listing.sort() 

    for idx, l in enumerate(listing):
        # get the pitch_keycenter from the filename
        tmp = l.split('_')[-1].replace('.wav','')
        print("pitch_keycenter = %s" % tmp)

        output_fname = l.replace('.wav','.sfz') #+ '.sfz'
        output_fpath = os.path.join(rootdir, oneshotdir, output_fname) 

        print('output_fpath', output_fpath)

        with open(output_fpath, 'w') as f: 
            out_str = "<region> "
            out_str += "sample=%s " % l
            out_str += "pitch_keycenter=%s%s" % (tmp, '') # (tmp, '2')
            out_str += "lokey=0 hikey=127"
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
