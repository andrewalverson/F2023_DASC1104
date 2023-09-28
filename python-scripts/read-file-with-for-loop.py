#!/usr/bin/env python3

album = open("blood_on_the_tracks.txt", "r")
counter = 0

for track in album:
    track = track.rstrip()
    counter += 1
    output_line = "song number " + str(counter) + " is: " + track
    print(output_line)

