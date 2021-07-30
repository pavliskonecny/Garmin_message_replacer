import time
from datetime import date


class My_Time:

    def __init__(self, round_nr: int):
        self.start_time = None
        self.round_nr = round_nr

    def get_time_stamp(self) -> str:
        if self.start_time is None:
            self.start_time = time.time()
        elapsed_time = time.time() - self.start_time
        return f"[{elapsed_time:.{self.round_nr}f}]: "

    @staticmethod
    def today() -> str:
        today = date.today()
        return f"{today.year}-{today.day:02}_{today.month:02}"

