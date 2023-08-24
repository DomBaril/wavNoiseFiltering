import soundpy as sp
import IPython.display as ipd
import os
import argparse
import sys
import logging

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file_path', type=str)
parser.add_argument('-o', '--output_file_path', type=str)
args = parser.parse_args()
if args.input_file_path == None or args.output_file_path == None:
    logging.exception('Arguments not properly set. -i for input file, -o for output file')
    sys.exit()

input_file_path = args.input_file_path
output_file_path = args.output_file_path

noisy_sound = sp.string2pathlib(input_file_path)
sr = 48000

# sp.plotsound(noisy_sound, sr=sr, feature_type='signal',
#                title = 'Noisy Speech', subprocess=True)

filtered_sound, sr = sp.filtersignal(noisy_sound,
                                 sr = sr,
                                 filter_type = 'wiener') # default

sp.files.savesound(output_file_path, filtered_sound, sr)