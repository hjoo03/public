from datetime import datetime
# Author: logoo03


def dbg(args):
    apos = "'"
    if type(args) in (int, str, list, tuple, dict, type):
        print(f'{args}; (type: {str(type(args))[8:str(type(args))[8:].find(apos)+8]}) [{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}]')
    else:
        print(f"{args}; (type: {type(args)}) [{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}]")
