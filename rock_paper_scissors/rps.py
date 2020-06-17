#!/usr/bin/python

import sys

#n = number of plays
def rock_paper_scissors(n):
  output=[]   # gives possible permutations
  words=["rock", "paper", "scissors"]
 
  if len(output)==0:
    return output  #empty array
  
  elif len(output)==1:
    return output.append(words) # [[a,b,c]]
 
  
  # elif len(output)>1:
   
  # return output.append() # [[],[],[],[],[]....]

 

  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')