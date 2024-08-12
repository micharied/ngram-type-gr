#!/usr/bin/env python3

"""
This script was generated from the Mar 23, 2023 free version of ChatGPT.

Prompt: 

I now want to take these three files, bigrams.csv, trigrams.csv 
and tetragrams.csv, and convert them into the following files: 
bigrams.js, trigrams.js, and tetragrams.js.

Write a python script that will read in these three files, and 
output the js files. For each input file, it should take the 
first 200 words, and write it into a `const xgrams` list, where 
xgrams would be bigrams, trigrams or tetragrams respectively. 

The list should be formatted so that we have one word per line.

Some of the ngrams have apostrophes in them. The output js 
should have strings that have double quotes instead of single 
quotes, so that the apostrophes don't cause any problems.
"""

import csv
import os

# Define the input and output filenames
file_info = {
    2: {"input": "/etl/bigrams.csv", "output": "/ngrams/bigrams.js", "var_name": "const bigrams"},
    3: {"input": "/etl/trigrams.csv", "output": "/ngrams/trigrams.js", "var_name": "const trigrams"},
    4: {"input": "/etl/tetragrams.csv", "output": "/ngrams/tetragrams.js", "var_name": "const tetragrams"},
    "words": {"input": "/etl/sorted_wordlist.csv", "output": "/ngrams/words.js", "var_name": "window.words"}
}

# Define the number of n-grams to extract
num_ngrams = 200

# Loop over each input file
for key in file_info.keys():
    # Read in the n-grams or words from the CSV file
    ngrams_or_words = []
    with open(os.getcwd() + file_info[key]["input"], "r") as input_file:
        reader = csv.reader(input_file)
        i = 0
        for row in reader:
            if i >= num_ngrams:
                break
            if key == "words" and len(row[0]) < 5:
                next(reader)
                continue
            ngrams_or_words.append(row[0])
            i += 1

    # Write the n-grams or words to the JavaScript file
    with open(os.getcwd() + file_info[key]["output"], "w") as output_file:
        output_file.write("{} = [\n".format(file_info[key]["var_name"]))
        output_file.write("\n".join(['    "{}",'.format(ngram_or_word) for ngram_or_word in ngrams_or_words]))
        output_file.write("\n];\n")