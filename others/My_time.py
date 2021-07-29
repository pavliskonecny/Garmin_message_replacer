import time
from datetime import date


class My_Time:

    def __init__(self, round_nr: int):
        self.start_time = None
        self.round_nr = round_nr
        self.my_format = '{:0<' + str(self.round_nr + 2) + '}'
        # make format - fill 0 to (round_nr + 2) because you have to add "0."

    def get_time_stamp(self) -> str:
        if self.start_time is None:
            self.start_time = time.time()

        res = time.time() - self.start_time             # difference between start time and NOW is elapsed time
        res = round(res, self.round_nr)                     # rounded to constructor value
        res = self.my_format.format(res)

        return "[" + str(res) + "]: "

    @staticmethod
    def today() -> str:
        today = date.today()
        return f"{today.year}-{today.day:02}_{today.month:02}"
