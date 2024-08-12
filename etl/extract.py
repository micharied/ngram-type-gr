#!/usr/bin/env python3

"""
This script was generated from the Mar 23, 2023 free version of ChatGPT.

Prompt: 

Lets say I have a file called "1gramstop10k.csv". It contains a 
list of the most common 1grams, and their frequency. Each row is 
a comma separated vector of the word, and the frequency. For example, 
the first 10 lines are:

de,1024824
la,602084
et,563643
le,489172
à,411923
les,401243
que,308583
il,252601
des,246732
en,239320

Can you write me some good python code that can extract the 2, 3 and 
4-grams from these words? The ngrams that are extracted from each row 
should be multiplied by the frequency of the word.

I am thinking you could store any ngrams you find in a hash table 
(dictionary) where the key is the ngram, and the value is the frequency 
of occurence. If you find the same ngram in a subsequent word, 
you would add the words frequency to the value.

There should be one dictionary each for the bigrams,
trigrams, and tetragrams. 


I would like the extracted ngrams written to 3 files:

1. "bigrams.csv", which contains most frequent 2-grams present in the dataset
1. "trigrams.csv", which contains most frequent 3-grams present in the dataset
1. "tetragrams.csv", which contains most frequent 4-grams present in the dataset
"""

import csv
from collections import defaultdict
import os

# Define the filenames for the input and output files
input_filename = os.getcwd() + "/etl/wordlist.csv"
output_filenames = {
    2: "/etl/bigrams.csv",
    3: "/etl/trigrams.csv",
    4: "/etl/tetragrams.csv"
}

# Define the n-gram lengths to extract
ngram_lengths = [2, 3, 4]

# Define a dictionary to store the n-grams and their frequencies for each length
ngrams = {}
for n in ngram_lengths:
    ngrams[n] = defaultdict(int)

# Open the input file and read its contents into a list of tuples
with open(input_filename, "r") as input_file:
    reader = csv.reader(input_file)
    data = [(row[0].lower(), float(row[1])) for row in reader]

# Loop over each word in the input file, and extract its n-grams
for word, frequency in data:
    for n in ngram_lengths:
        for i in range(len(word) - n + 1):
            ngram = word[i:i+n]
            ngrams[n][ngram] += frequency

# Loop over each n-gram length, and write the most frequent n-grams to a file
for n in ngram_lengths:
    # Sort the n-grams by frequency, in descending order
    sorted_ngrams = sorted(ngrams[n].items(), key=lambda x: x[1], reverse=True)
    # Write the most frequent n-grams to a file
    with open(os.getcwd() + output_filenames[n], "w") as output_file:
        for i in range(min(1000, len(sorted_ngrams))):
            ngram, frequency = sorted_ngrams[i]
            output_file.write(f"{ngram},{frequency}\n")