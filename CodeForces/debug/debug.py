from datetime import datetime
# Author: logoo03


class Debug:
    def __init__(self):
        self.count = 0

    def dbg(self, args):
        apos = "'"
        if type(args) == str:
            if "@@" in args:
                print(f"debug breakpoint #{self.count}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count += 1
                return
        if type(args) in (int, str, list, tuple, dict, type):
            print(f'{args}; (type: {str(type(args))[8:str(type(args))[8:].find(apos)+8]}) '
                  f'[{datetime.now().strftime("%H:%M:%S.%f")[:-3]}]')
        else:
            print(f"{args}; (type: {type(args)}) [{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
