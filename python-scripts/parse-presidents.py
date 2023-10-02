#!/usr/bin/env python3

import csv
from collections import defaultdict

# key = president, value = party
parties = defaultdict(str)

# key = party, value = party count
party_count = defaultdict(int)

# open and read the data file
with open("presidents.csv", 'r') as file:
    # create a csv reader object
    reader = csv.reader(file, delimiter=',')

    
  #  counter = 0

    # loop over all the lines
    for line in reader:
        # skipping the header line
   #     counter +=1 
        if(line[0].strip() == 'Presidency'):
            continue

        # else it's a data line
        else:
            name = line[1].strip()
            party = line[5]
            parties[name] = party
   
# print("output would print", counter, "lines right now")


for pres, party in parties.items():
    party_count[party] +=1

    output_list = [pres, party, str(party_count[party])]
    print("\t".join(output_list))












