# Copyright 2021  SpeechColab Authors

import argparse
import json
from collections import defaultdict
from pathlib import Path

from speechcolab.datasets.gigaspeech import GigaSpeech


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Save the audio segments into flac files.')
    parser.add_argument('corpus', help='The corpus directory')
    parser.add_argument('output', help='The output file')
    args = parser.parse_args()

    gigaspeech = GigaSpeech(args.corpus)

    sid_to_subset = defaultdict(list)

    for subset in ('{XL}', '{L}', '{M}', '{S}', '{XS}', '{DEV}', '{TEST}'):
        for seg in gigaspeech.segments(subset):
            sid_to_subset[seg['sid']].append(subset)
            pass
    
    with open(args.output, 'w') as f:
        json.dump(sid_to_subset, f, indent=2, sort_keys=True)
