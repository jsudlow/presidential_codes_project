from itertools import count

class Nuclear:
    _ids = count(0)
    def __init__(self,name):
        self.name = name
        self.codes = [None] * 15
        self.id = next(self._ids)
    def __str__(self):
        ret_string = ""
        real_codes = self.actual_codes()
        accum = 0
        printed_string = ""
        for code in self.codes:
            if code == None: continue
            printed_string += code
            accum += 1
            if accum < real_codes:
                printed_string += ", "
        print(printed_string)
        return ret_string

    def set_code(self,code,idx_location):
        self.codes[idx_location] = code
    def print_codes(self):
        real_codes = self.actual_codes()
        accum = 0
        printed_string = ""
        for code in self.codes:

            if code == None: continue
            printed_string += code
            accum += 1
            if accum < real_codes:
                printed_string += ", "
        print(printed_string)
    def actual_codes(self):
        accum = 0
        for code in self.codes:
            if code == None: continue
            accum += 1
        return accum


