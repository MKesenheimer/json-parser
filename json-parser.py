#!/usr/bin/env python3
import json
import argparse
import sys

def parse(jsn, obj):
  jdict = json.loads(jsn)
  for o in obj.split("."):
    try:
      jdict = jdict[o]
    except:
      print("Object {} in {} not found.".format(obj, jsn))
      exit(-1)
  print(jdict)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="")
  parser.add_argument('path', metavar='file.json', type=str, nargs="?", help='')
  parser.add_argument('-f', '--file', dest='fpath', type=str, required=False, help='')
  parser.add_argument('-j', '--json', dest='json', type=str, required=False, help='')
  parser.add_argument('-o', '--object', dest='object', type=str, required=True, help='')
  args = parser.parse_args()

  if  args.path != None or args.fpath != None: 
    path = args.path if args.path != None else args.fpath
    try:
      with open(path, 'r') as infile:
        jsn = infile.read()
    except:
      print("File not found.")
      parser.print_help()
      exit(-1)
    parse(jsn, args.object)
  
  elif args.json != None:
    parse(args.json, args.object)

  else:
    parser.print_help()
    sys.exit(-1)
