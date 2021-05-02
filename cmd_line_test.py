#!/usr/bin/python

import sys
import getopt

usageMsg = f"{sys.argv[0]} [--approved=true] [--approval_rate=75]"
paramDict = dict()

def processCmdLine(args):
    try:
      options, remainder = getopt.getopt(args,"",["approved=","approval_rate="])
    #   print(f"options={options}")
    #   print(f"remainder={remainder}")
    except getopt.GetoptError:
      print (usageMsg)
      return paramDict
    
    for opt, arg in options:
      if opt == '--approved':
          paramDict['approved'] = False if arg!="true" else True
        #   if arg != "true": 
        #       paramDict['approved'] = False
        #   else:
        #       paramDict['approved'] = True

          print (f"Generate a single inference")
          break
      elif opt == '--approval_rate':
          paramDict['approval_rate'] = int(arg)
          print (f"Generate continuous inferences (ctrl-c to stop)")
          break
    
    print (f"paramDict={paramDict}")
    return paramDict

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print(usageMsg)
        sys.exit(1)
        
    paramDict = processCmdLine(sys.argv[1:])
    sys.exit(0)
