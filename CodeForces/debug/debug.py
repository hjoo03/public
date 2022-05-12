from datetime import datetime
# Author: logoo03


class Debug:
    def __init__(self):
        self.count_2 = 1
        self.count_3 = 1
        self.count_4 = 1
        self.count_5 = 1

    def dbg(self, args):
        apos = "'"

        if type(args) == str:
            if "@@@@@" in args:
                print(f"debug breakpoint @@@@@ #{self.count_5}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_5 += 1
                return

            elif "@@@@" in args:
                print(f"debug breakpoint @@@@ #{self.count_4}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_4 += 1
                return

            elif "@@@" in args:
                print(f"debug breakpoint @@@ #{self.count_3}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_3 += 1
                return

            elif "@@" in args:
                print(f"debug breakpoint @@ #{self.count_2}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_2 += 1
                return

        if type(args) in (int, str, list, tuple, dict, type):
            print(f'{args}; (type: {str(type(args))[8:str(type(args))[8:].find(apos)+8]}) '
                  f'[{datetime.now().strftime("%H:%M:%S.%f")[:-3]}]')
        else:
            print(f"{args}; (type: {type(args)}) [{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
