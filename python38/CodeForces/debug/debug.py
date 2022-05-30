from datetime import datetime
# Author: logoo03


class Debug:
    def __init__(self):
        self.count_1 = 1
        self.count_2 = 1
        self.count_3 = 1
        self.count_4 = 1
        self.count_5 = 1

    def debug(self, arg1=None, arg2=None, arg3=None, arg4=None):
        apos = "'"
        if not (arg1 or arg2 or arg3 or arg4):
            if arg1 != 0 and arg2 != 0 and arg3 != 0 and arg4 != 0:
                print(f"debug breakpoint @ #{self.count_1}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_1 += 1
                return

        if type(arg1) == str:
            if "@@@@@" in arg1:
                print(f"debug breakpoint @@@@@ #{self.count_5}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_5 += 1
                return

            elif "@@@@" in arg1:
                print(f"debug breakpoint @@@@ #{self.count_4}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_4 += 1
                return

            elif "@@@" in arg1:
                print(f"debug breakpoint @@@ #{self.count_3}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_3 += 1
                return

            elif "@@" in arg1:
                print(f"debug breakpoint @@ #{self.count_2}; "
                      f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")
                self.count_2 += 1
                return

        def type_info(ar):
            print(f'{ar}({str(type(ar))[8:str(type(ar))[8:].find(apos)+8]})', end=' ; ')

        def print_time():
            print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}]")

        args = []
        for arg in [arg1, arg2, arg3, arg4]:
            if arg:
                args.append(arg)
            elif arg == 0:
                args.append(arg)

        for arg in args:
            type_info(arg)
        print_time()

        return
