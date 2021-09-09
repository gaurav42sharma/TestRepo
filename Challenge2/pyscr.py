import json
import os
import sys, getopt
import argparse
from ec2_metadata import ec2_metadata

def prop(key):  # pass property name as a string
    return getattr(ec2_metadata, key)

def main(argv):
    res = {}
    try:
      opts, args = getopt.getopt(argv, 'k:',["key=",])
    except getopt.GetoptError:
      print ('pyscr.py -k <key_name>')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-k':
            key = arg
            val = prop(key)
            res[key] = val
    
    print(res)

if __name__ == "__main__":
    main(sys.argv[1:])
