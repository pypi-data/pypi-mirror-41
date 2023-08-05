#!python3
#distutils: language = c++
import random
from datetime import datetime


cdef extern from "Fortuna.hpp":
    int _random_range "random_range"(int, int)
    int _random_below "random_below"(int)
    int _d "d"(int)
    int _dice "dice"(int, int)
    int _ability_dice "ability_dice"(int)
    int _min_max "min_max"(int, int, int)
    int _percent_true "percent_true"(int)
    int _plus_or_minus "plus_or_minus"(int)
    int _plus_or_minus_linear "plus_or_minus_linear"(int)
    int _plus_or_minus_curve "plus_or_minus_curve"(int, int)
    int _zero_flat "zero_flat"(int)
    int _zero_cool "zero_cool"(int)
    int _zero_extreme "zero_extreme"(int)
    int _max_cool "max_cool"(int)
    int _max_extreme "max_extreme"(int)
    int _mostly_middle "mostly_middle"(int)
    int _mostly_center "mostly_center"(int)


def random_range(int lo, int hi) -> int:
    return _random_range(lo, hi)

def random_below(int num) -> int:
    return _random_below(num)

def d(int sides) -> int:
    return _d(sides)

def dice(int rolls, int sides) -> int:
    return _dice(rolls, sides)

def ability_dice(int num) -> int:
    return _ability_dice(num)

def min_max(int n, int lo, int hi) -> int:
    return _min_max(n, lo, hi)

def percent_true(int num = 50) -> bool:
    return _percent_true(_min_max(num, 0, 100)) == 1

def plus_or_minus(int num) -> int:
    return _plus_or_minus(num)

def plus_or_minus_linear(int num) -> int:
    return _plus_or_minus_linear(num)

def plus_or_minus_curve(int num, bounded=True) -> int:
    cdef int bound = 1 if bounded else 0
    return _plus_or_minus_curve(num, bound)

def zero_flat(int num) -> int:
    return _zero_flat(num)

def zero_cool(int num) -> int:
    return _zero_cool(num)

def zero_extreme(int num) -> int:
    return _zero_extreme(num)

def max_cool(int num) -> int:
    return _max_cool(num)

def max_extreme(int num) -> int:
    return _max_extreme(num)

def mostly_middle(int num) -> int:
    return _mostly_middle(num)

def mostly_center(int num) -> int:
    return _mostly_center(num)

def random_value(arr):
    size = len(arr)
    return arr[_random_below(size)]

def pop_random_value(list arr):
    size = len(arr)
    return arr.pop(_random_below(size))

def cumulative_weighted_choice(table):
    max_weight = table[-1][0]
    rand = _random_below(max_weight)
    for weight, value in table:
        if weight > rand:
            return value

def flatten(itm):
    if not callable(itm):
        return itm
    else:
        try:
            return flatten(itm())
        except TypeError:
            return itm

def n_samples(func: staticmethod, *args, n=10, **kwargs):
    return [func(*args, **kwargs) for _ in range(n)]


def n_samples_flat(func: staticmethod, *args, n=10, **kwargs):
    return [flatten(func(*args, **kwargs)) for _ in range(n)]


def bind(func: staticmethod, *args, **kwargs):
    return lambda: func(*args, **kwargs)


class RandomCycle:

    def __init__(self, arr, flat_map=True):
        self.arr = arr
        self.flat_map = flat_map
        self.size = len(arr)
        assert self.size >= 3, f"Input Error, sequence length must be >= 3."
        self.data = list(arr)
        random.shuffle(self.data)
        self.next = self.data.pop()
        self.out_idx = len(self.data) - 1
        self.in_idx = len(self.data) - 2

    def __call__(self):
        result = self.next
        self.next = self.data.pop(max_extreme(self.out_idx))
        self.data.insert(zero_extreme(self.in_idx), result)
        return flatten(result) if self.flat_map else result

    def __repr__(self):
        return f"RandomCycle({self.arr})"


class BlockCycle:

    def __init__(self, arr, flat_map=True):
        self.arr = arr
        self.flat_map = flat_map
        assert len(arr) >= 3, f"Input Error, sequence length must be >= 3."
        self.data = list(arr)
        random.shuffle(self.data)
        self.next = pop_random_value(self.data)

    def __call__(self):
        result = self.next
        while result is self.next:
            self.next = pop_random_value(self.data)
        if len(self.data) < 1:
            self.data = list(self.arr)
            random.shuffle(self.data)
        return flatten(result) if self.flat_map else result

    def __repr__(self):
        return f"BlockCycle({self.arr})"


class QuantumMonty:

    def __init__(self, data, flat_map=True):
        self.flat_map = flat_map
        self.data = tuple(data)
        self.max_id = len(data) - 1
        self.random_cycle = RandomCycle(data, flat_map)

    def flatten(self, itm):
        return flatten(itm) if self.flat_map else itm

    def __call__(self):
        return self.quantum_monty()

    def __repr__(self):
        return f"QuantumMonty({self.data})"

    def dispatch(self, quantum_bias="monty"):
        return {
            "monty": self.quantum_monty,
            "cycle": self.mostly_cycle,
            "front": self.mostly_front,
            "middle": self.mostly_middle,
            "back": self.mostly_back,
            "first": self.mostly_first,
            "center": self.mostly_center,
            "last": self.mostly_last,
            "flat": self.mostly_flat,
        }[quantum_bias]

    def mostly_flat(self):
        return self.flatten(random_value(self.data))

    def mostly_cycle(self):
        return self.random_cycle()

    def mostly_front(self):
        return self.flatten(self.data[_zero_cool(self.max_id)])

    def mostly_back(self):
        return self.flatten(self.data[_max_cool(self.max_id)])

    def mostly_middle(self):
        return self.flatten(self.data[_mostly_middle(self.max_id)])

    def mostly_first(self):
        return self.flatten(self.data[_zero_extreme(self.max_id)])

    def mostly_last(self):
        return self.flatten(self.data[_max_extreme(self.max_id)])

    def mostly_center(self):
        return self.flatten(self.data[_mostly_center(self.max_id)])

    def quantum_monty(self):
        monty_methods = (
            self.mostly_front,
            self.mostly_middle,
            self.mostly_back,
            self.mostly_first,
            self.mostly_center,
            self.mostly_last,
        )
        return random_value(monty_methods)()


class FlexCat:

    def __init__(self, data, y_bias="front", x_bias="cycle", flat_map=True):
        self.data = data
        self.y_bias = y_bias
        self.x_bias = x_bias
        self.flat_map = flat_map
        self.cat_keys = tuple(data.keys())
        self.random_cat = QuantumMonty(self.cat_keys).dispatch(y_bias)
        self.random_selection = {
            key: QuantumMonty(sequence, flat_map=flat_map).dispatch(x_bias) for key, sequence in data.items()
        }

    def __call__(self, cat_key=None):
        return self.random_selection[cat_key if cat_key else self.random_cat()]()

    def __repr__(self):
        return f"FlexCat({self.data}, y_bias='{self.y_bias}', x_bias='{self.x_bias}')"


class RelativeWeightedChoice:

    def __init__(self, weighted_table, flat_map=True):
        self.flat_map = flat_map
        self.weighted_table = weighted_table
        optimized_data = sorted([list(itm) for itm in weighted_table], key=lambda x: x[0], reverse=True)
        cum_weight = 0
        for w_pair in optimized_data:
            cum_weight += w_pair[0]
            w_pair[0] = cum_weight
        self.max_weight = optimized_data[-1][0]
        self.data = tuple(tuple(itm) for itm in optimized_data)

    def __call__(self):
        result = self.weighted_choice()
        return flatten(result) if self.flat_map else result

    def weighted_choice(self):
        rand = _random_below(self.max_weight)
        for weight, value in self.data:
            if weight > rand:
                return value

    def __repr__(self):
        return f"RelativeWeightedChoice({self.weighted_table})"


class CumulativeWeightedChoice:

    def __init__(self, weighted_table, flat_map=True):
        self.flat_map = flat_map
        self.weighted_table = weighted_table
        data = sorted([list(itm) for itm in weighted_table], key=lambda x: x[0])
        prev_weight = 0
        for w_pair in data:
            w_pair[0], prev_weight = w_pair[0] - prev_weight, w_pair[0]
        optimized_data = sorted(data, key=lambda x: x[0], reverse=True)
        cum_weight = 0
        for w_pair in optimized_data:
            cum_weight += w_pair[0]
            w_pair[0] = cum_weight
        self.max_weight = optimized_data[-1][0]
        self.data = tuple(tuple(itm) for itm in optimized_data)

    def __call__(self):
        result = self.weighted_choice()
        return flatten(result) if self.flat_map else result

    def weighted_choice(self):
        rand = _random_below(self.max_weight)
        for weight, value in self.data:
            if weight > rand:
                return value

    def __repr__(self):
        return f"CumulativeWeightedChoice({self.weighted_table})"


class RandomWalk:

    def __init__(self, arr, flat_map=True):
        self.flat = flat_map
        self.data = arr
        self.len_data = len(self.data)
        assert self.len_data > 0, "RandomWalk requires a non-empty container."
        self.idx = _random_below(self.len_data)

    def __call__(self):
        modifier = 1 if _percent_true(50) else -1
        self.idx = (self.idx + modifier) % self.len_data
        result = self.data[self.idx]
        return flatten(result) if self.flat else result

    def __repr__(self):
        return f"RandomWalk({self.data})"


class CatWalk:

    def __init__(self, table, flat_map=True):
        self.flat = flat_map
        self.data = table
        self.len_x = max(len(itm) for itm in self.data)
        self.len_y = len(self.data)
        assert self.len_y > 0 and self.len_x > 0, "Containers in CatWalk must not be empty."
        assert min(len(itm) for itm in self.data) == self.len_x, "Containers in CatWalk must be of equal length."
        self.x_idx = _random_below(self.len_x)
        self.y_idx = _random_below(self.len_y)

    def __call__(self):
        x_mod = 1 if _percent_true(50) else -1
        y_mod = 1 if _percent_true(50) else -1
        if _percent_true(50):
            self.x_idx = (self.x_idx + x_mod) % self.len_x
            self.y_idx = (self.y_idx + y_mod) % self.len_y
        elif _percent_true(50):
            self.x_idx = (self.x_idx + x_mod) % self.len_x
        else:
            self.y_idx = (self.y_idx + y_mod) % self.len_y
        result = self.data[self.y_idx][self.x_idx]
        return flatten(result) if self.flat else result

    def __repr__(self):
        return f"CatWalk({self.data})"


def distribution_timer(func: staticmethod, *args, call_sig=None, num_cycles=100000, **kwargs):
    start_time = datetime.now()
    results = n_samples(func, *args, n=num_cycles, **kwargs)
    end_time = datetime.now()
    total_time = (end_time - start_time).total_seconds()
    if call_sig is None:
        if hasattr(func, "__qualname__"):
            call_sig = f"{func.__qualname__}{f'({args[0]})' if len(args) == 1 else args}"
        else:
            call_sig = f"f(x)"
    total_time_ms = round(total_time * 1000.0, 2)
    average_time_nano = round((total_time_ms / num_cycles) * 1000000)
    print(f"{call_sig} x {num_cycles}: Total time: {total_time_ms} ms, Average time: {average_time_nano} nano")
    if type(results[0]) is list:
        for i, _ in enumerate(results):
            results[i] = results[i][0]
    unique_results = list(set(results))
    if all([not callable(x) for x in unique_results]):
        unique_results.sort()
    result_obj = {
        key: f"{results.count(key) / (num_cycles / 100)}%" for key in unique_results
    }
    for key, val in result_obj.items():
        print(f" {key}: {val}")
    print("")


def analytic_continuation(func: staticmethod, num: int) -> int:
    if num < 0:
        return -func(-num)
    elif num == 0:
        return 0
    else:
        return func(num)
