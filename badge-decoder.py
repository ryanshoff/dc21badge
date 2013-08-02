#!/usr/bin/env python
# 
# allow someone to put in a string of integers, and then output the ordinal 
# letters in both plain text and rot13

# Build the ordinal char array
ords = map(chr, range(97, 123))

# Grab input from user
ciphertext = raw_input("Enter the numbers from the badge: ")

cleartext = ""
# Decode string into integers. Note that the way Python array slicing works
# requires that to be inclusive, I have to go one over.
for i in range(0,len(ciphertext),2):
  cleartext += ords[int(ciphertext[i:i+2])-1]

print "Cleartext:        " + cleartext
print "rot13(cleartext): " + cleartext.decode('rot13')
