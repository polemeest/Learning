from typing import Generator
from typing import Generator
def my_range_gen(stop = 0, start = 0, step = 1) -> Generator[int, int, ValueError]:
    if start == 0 and step > 0:
        current = start
        while current < stop:
            yield current
            current += step
    elif stop > start and step < 0:
        current = stop
        while current > start:
            yield current
            current += step
    elif stop < start and step > 0:
        current = stop
        while current < start:
            yield current
            current += step
    elif step == 0:
        return ValueError("arg 3 must not be zero")
    else:
        pass

# def my_range_gen(stop, start=0, inc=1):
#     if start != 0:
#         stop, start = start, stop
#     while (inc > 0 and start < stop) or (inc < 0 and start > stop):
#         yield start
#         start += inc


# def my_range_gen(start, stop=None, step=1):
#     if stop is None:
#         stop, start = start, 0
#     while (start < stop, start > stop)[step < 0]:
#         yield start
#         start += step