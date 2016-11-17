#James English Assignment 5
#IT 612

import sys 
import os

print("This script checks word frequency in a file and prints out the most frequently used words.")

#Must check file first to see if it exists. If it doesnt, script will exit

file = input("Which file would you like to check? ")
if os.path.isfile(file):
  print("The file", file, "does exist")
else:
  print("The file", file, "was not found, script exiting")
  sys.exit()
  print("")

#Take input from the user and ask the number of results they want to see
output = int(input("How many words would you like to see the frequency of? "))
if type(output) == int:
  print("Script will output", output, "results: ")
else:
  if type(output) == string:
    print("Enter a number only please, script exiting")
    sys.exit()

#Read the file to examined 
readfile = open(file, 'r+')

def wordcount(): #Function will split each word and count how many times it appears 
  words = readfile.read().split()
  wordcount = {} 

  for word in words:
    if word in wordcount:
      wordcount[word] += 1
    else:
      wordcount[word] = 1

  from collections import Counter #Sorting the words based on the frequency in which they occur
  sortbyfreq = Counter(words)
  for word, wordcount[word] in sortbyfreq.most_common(output): #only printing the amount of words the user asked for 
    print("%-20s %10d" % (word, wordcount[word])) 

wordcount() #Call the function to run 

  
