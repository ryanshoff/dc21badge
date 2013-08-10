#!/bin/sh
./alphaotp disk.txt keyhol.txt > 1.txt 
./alphaotp 1.txt rotary.txt > 2.txt
./alphaotp 2.txt smiley.txt > 3.txt 
./sub plaintext.txt 3.txt > 4.txt 

