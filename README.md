# oneshot_sfz_mapper

Creates an SFZ file (see https://sfzformat.com/tutorials/drum_basics) that maps
all one shots from a given directoy across the keyboard (a la
http://mildon.me/beagle.php?b=view&id=UVIU)

The function process_one_dir takes as input a path to one directory of one shots
it creates an SFZ file that maps the one shots across the keyboard to adjacent
keys

__main__ runs process_one_dir for every subdirectory in a root directory for
batch processing

