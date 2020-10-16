import time


class My_time():

    def __init__(self, round_nr: int):
        self.start_time = None
        self.round_nr = round_nr

    def get_time_stamp(self) -> str:
        if self.start_time == None:
            self.start_time = time.time()

        res = time.time() - self.start_time                 # difference between start time and NOW is elapsed time
        res = round(res, self.round_nr)                     # rounded to constructor value

        my_format = '{:0<' + str(self.round_nr+2) + '}'     # make format - fill 0 to rounded constructor value
                                                            # because you have to add "0."
        res = my_format.format(res)

        return "[" + str(res) + "]: "
