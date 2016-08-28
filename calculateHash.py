#!/usr/bin/python

import sys
import itertools
import hashlib

def _fetchChoice():
    while True:
        print('1. MD5 hash ')
        print('2. SHA1 hash ')
        print('3. SHA256 hash ')
        print('4. All hashes ')
        print('Enter your choice: ')
        choice = int(input())
        if choice == 1 or 2 or 3 or 4:
            return choice
        else:
            print('Enter either "1" "2" "3" or "4" ')


#function  reads file and calculate the MD5 signature
def calcMd5Hash(filename):
    hash = hashlib.md5()
    with open(filename) as f:
        for chunk in iter(lambda: f.read(4096), ""):
            hash.update(chunk)
    return hash.hexdigest()


def calculateSha1Hash(filename):
    hash = hashlib.sha1()
    with open(filename) as f:
	for chunk in iter(lambda: f.read(1024), ""):
	    hash.update(chunk)
    return hash.hexdigest()


def calculateSha256Hash(filename):
    hash = hashlib.sha256()
    with open(filename) as f:
	for chunk in iter(lambda: f.read(1024), ""):
	    hash.update(chunk)
    return hash.hexdigest()


def _getFetchedChoice(choice):
    hashString = calcMd5Hash(sys.argv[1]) 
    hashString2 = calculateSha1Hash(sys.argv[1])
    hashString3 = calculateSha256Hash(sys.argv[1])
    if choice == 1:
        result = calcMd5Hash(sys.argv[1])
    elif choice == 2:
        result = calculateSha1Hash(sys.argv[1])  
    elif choice == 3:
        result = calculateSha256Hash(sys.argv[1])
    elif choice == 4:
        result = str("The MD5 hash of file named: "+str(sys.argv[1])+" is: "+calcMd5Hash(sys.argv[1])+"\nThe SHA1 hash of file named: "+str(sys.argv[1])+" is: "+ calculateSha1Hash(sys.argv[1])+"\nThe SHA256 hash of file named: "+str(sys.argv[1])+" is: "+calculateSha256Hash(sys.argv[1]))
        
    return result
 
def main():
 
 #test for enough command line arguments
 if len(sys.argv) <2:
    print("Usage python claculate_hash.py <filename>")
    return

 choice = _fetchChoice() 
 print(choice)          
 print(_getFetchedChoice(choice))


 
 
 

    
    
 











main()
