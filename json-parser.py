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
  parser = argparse.ArgumentParser(description="Parse JSON objects on the command line.\nExample:\n\njson-parser -j '{\"author\": \"Matthias Kesenheimer\"}' -o \"author\"")
  parser.add_argument('path', metavar='JSON-file', type=str, nargs="?", help='Text file with JSON content')
  parser.add_argument('-f', '--file', metavar='JSON-file', dest='fpath', type=str, required=False, help='Text file with JSON content')
  parser.add_argument('-j', '--json', metavar='JSON-string', dest='json', type=str, required=False, help='JSON object as string')
  parser.add_argument('-o', '--object', metavar='object', dest='object', type=str, required=True, help='Object to parse')
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
