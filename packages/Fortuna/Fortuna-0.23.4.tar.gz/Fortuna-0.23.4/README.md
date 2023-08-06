# Fortuna: Fast & Flexible Random Value Generators
Fortuna replaces much of the functionality of Python's Random module, often achieving 10x better performance. However, the most interesting bits of Fortuna are found in the high-level abstractions like FlexCat, QuantumMonty and TruffleShuffle.

The core functionality of Fortuna is based on the C++ `random.h` implementation of the Mersenne Twister Algorithm by Makoto Matsumoto (松本 眞) and Takuji Nishimura (西村 拓士). Fortuna is not appropriate for cryptography of any kind. Fortuna is for games, data science, AI and experimental programming, not security.

Fortuna is designed to employ hardware seeding exclusively, this allows the generator to be completely encapsulated at the binary level. The API offers no direct access to the generator itself. This makes Fortuna non-deterministic and inappropriate for some projects. This is a design choice and could change in the future.

Fortuna is designed, built and tested for MacOS X, it also happens to work out-of-the-box with many flavors of Linux and Unix.

Console Installation: `$ pip3 install Fortuna` or download and build from source, if that's your thing. Installation on some platforms may require Cython and a compiler to be installed first. Cython is the link between C++ and Python. Cython is used for installation only when needed. Installing Fortuna on MacOS via pip should not require it.

Fortuna is built for the default CPython implementation standard, other implementations may or may not support c-extensions like Fortuna. A pure Python version of Fortuna is included in the extras folder. The c-extension is roughly order of magnitude faster in CPython than the pure Python version.


## Documentation Table of Contents
```
I.   Fortuna Core Functions
        a. Random Numbers
        b. Random Truth
        c. Random Sequence Values
        d. Random Table Values
        e. Utility Functions

II.  Fortuna Abstraction Classes
        a. Sequence Wrappers
            1. TruffleShuffle
            2. QuantumMonty
            3. RandomWalk
        b. Table Wrappers
            1. Cumulative Weighted Choice
            2. Relative Weighted Choice
            3. CatWalk
        c. Dictionary Wrapper
            1. FlexCat

III. Test Suite, output distributions and performance data.

IV.  Development Log

V.   Legal Information

```

---

## Fortuna Random Functions
### Random Numbers
`Fortuna.random_range(lo: int, hi: int) -> int`. Returns a random integer in range [lo..hi] inclusive. Up to 15x faster than `random.randint()`. Flat uniform distribution.

`Fortuna.random_below(num: int) -> int`. Returns a random integer in the exclusive range [0..num) for positive values of num. Flat uniform distribution.

`Fortuna.d(sides: int) -> int`. Represents a single die roll of a given size die. Returns a random integer in the range [1..sides]. Flat uniform distribution.

`Fortuna.dice(rolls: int, sides: int) -> int`. Returns a random integer in range [X..Y] where X = rolls and Y = rolls * sides. The return value represents the sum of multiple rolls of the same size die. Geometric distribution based on the number and size of the dice rolled. Complexity scales primarily with the number of rolls, not the size of the dice.

`Fortuna.plus_or_minus(num: int) -> int`. Negative and positive input values of num will produce equivalent distributions. Returns a random integer in range [-num..num]. Flat uniform distribution.

`Fortuna.plus_or_minus_linear(num: int) -> int`. Negative and positive input values of num will produce equivalent distributions. Returns a random integer in range [-num..num]. Zero peak geometric distribution, up triangle.

`Fortuna.plus_or_minus_curve(num: int) -> int`. Returns a random integer in the bounded range [-num..num]. Zero peak gaussian distribution, bounded stretched bell curve: mean = 0, variance = num / pi.

`Fortuna.stretched_bell(num: int) -> int`. This is an unbounded plus_or_minus_curve. Returns a random integer with high probability (~98% +/-2%) to be in range [-num..num]. Zero peak gaussian distribution, unbounded stretched bell curve: mean = 0, variance = num / pi.

`Fortuna.zero_flat(num: int) -> int`. Returns a random integer in range [0..num]. Flat uniform distribution.

`Fortuna.zero_cool(num: int) -> int`. Returns a random integer in range [0..num]. Zero peak, geometric distribution, half triangle.

`Fortuna.zero_extreme(num: int) -> int`. Returns a random integer in range [0..num]. Zero peak, gaussian distribution, half bell curve: mean = 0, variance = num / pi.

`Fortuna.max_cool(num: int) -> int`. Returns a random integer in range [0..num]. Max peak (num), geometric distribution, half triangle.

`Fortuna.max_extreme(num: int) -> int`. Returns a random integer in range [0..num]. Max peak (num), gaussian distribution, half bell curve: mean = num, variance = num / pi.

`Fortuna.mostly_middle(num: int) -> int`. Returns a random integer in range [0..num]. Middle peak (num / 2), geometric distribution, up triangle. Ranges that span an even number of values will have two dominant values in the middle, this will guarantee that the probability distribution is always symmetrical.

`Fortuna.mostly_center(num: int) -> int`. Returns a random integer in range [0..num]. Middle peak (num / 2), gaussian distribution, bell curve: mean = num / 2, variance = num / pi.

`Fortuna.random_float() -> float`. Returns a random double in range [0.0..1.0) exclusive.

### Random Truth
`Fortuna.percent_true(num: int) -> bool`. Always returns False if num is 0 or less, always returns True if num is 100 or more. Any value of num in range [1..99] will produce True or False based on the value of num - the probability of True as a percentage.

### Random Sequence Values
`Fortuna.random_value(arr) -> value`. Returns a random value from a sequence (list or tuple), uniform distribution, non-destructive. Up to 10x faster than random.choice().

`Fortuna.pop_random_value(arr: list) -> value`. Returns and removes a random value from a sequence list, uniform distribution, destructive. Not included in the test suite due to it's destructive nature. This is the only destructive function in the module, use with care. It will raise an error if the list is empty.

### Random Table Values
`Fortuna.cumulative_weighted_choice(table) -> value`. Core function for the WeightedChoice base class. Produces a custom distribution of values based on cumulative weights. Requires input format: `[(weight, value), ... ]` sorted in ascending order by weight. Weights must be unique positive integers. See WeightedChoice class for a more comprehensive solution that verifies and optimizes the table. Up to 15x faster than random.choices()

### Utility Functions
`Fortuna.min_max(num: int, lo: int, hi: int) -> int`. Used to force a number in to the range [lo..hi]. Returns num if it is already in the proper range. Returns lo if num is less than lo. Returns hi if num is greater than hi.

`Fortuna.analytic_continuation(func: staticmethod, num: int) -> int`. Used to map a positive only function to the negative number line for complete input domain coverage. The "C" version of this function is used throughout the Fortuna extension. The function to be analytically continued must take an integer as input and return an integer.

`Fortuna.distribution_timer(func: staticmethod, call_sig=None, num_cycles=100000)`. The `func` arg is the callable object to be analyzed. `call_sig` is an optional label, this is useful for methods that don't have the `__qualname__` property. Optional arg `num_cycles` will set the total number invocations.

`Fortuna.flatten(itm: object) -> object`. Flatten will recursively unpack callable objects. If itm is not callable - flatten will return it, otherwise it recursively calls itm() and returns the result. Callable objects that require arguments are returned in an uncalled state.

`Fortuna.bind(func: staticmethod, *args, **kwargs) -> lambda`. Returns the passed function object and all arguments wrapped in a lambda for lazy evaluation.

`Fortuna.n_samples(func: staticmethod, *args, n=10, **kwargs) -> list`. Returns a list of n values by calling `func(*args, **kwargs)` n times.

`Fortuna.shuffle(arr: list) -> None`. Fisher-Yates Shuffle Algorithm. More than an order of magnitude faster than random.shuffle().

## Fortuna Random Classes
### Sequence Wrappers
#### Truffle Shuffle
Returns a random value from the wrapped sequence.

Produces a uniform distribution with a wide spread. Longer sequences will naturally push duplicates even farther apart. This behavior gives rise to output sequences that seem less mechanical than other random sequences.

TruffleShuffle will recursively unpack callable objects in the data set. Callable objects that require arguments are returned in an uncalled state. To disable this behavior pass the optional argument flat=False during instantiation. By default flat=True.

- Constructor takes a copy of a sequence (list or tuple) of arbitrary values.
- Values can be any Python object that can be passed around.
- Features continuous smart micro-shuffling: The Truffle Shuffle.
- Performance scales by some small fraction of the length of the input sequence.

```python
from Fortuna import TruffleShuffle


truffle_shuffle = TruffleShuffle(["Alpha", "Beta", "Delta", "Eta", "Gamma", "Kappa", "Zeta"])
truffle_shuffle()  # returns a random value, cycled uniform distribution.
```

#### The Quantum Monty
A set of strategies for producing random values from a sequence where the probability
of each value is based on the monty you choose. For example: the mostly_front monty
produces random values where the beginning of the sequence is geometrically more common than the back. The Quantum Monty Algorithm results from overlapping the probability waves of six of the other eight methods. The distribution it produces is a gentle curve with a bump in the middle.

QuantumMonty instances can return a list of samples rather than just one value, control the length of the list via the optional n_samples argument. By default n_samples=1.

QuantumMonty will recursively unpack callable objects in the data set. Callable objects that require arguments are not called. To disable this behavior pass the optional argument flat=False during instantiation. By default flat=True.

- Constructor takes a copy of a sequence (list or tuple) of arbitrary values.
- Sequence length must be greater than three, best if ten or more.
- Values can be any Python object that can be passed around... string, int, list, function etc.
- Performance scales by some tiny fraction of the length of the sequence. Method scaling may vary slightly.

```python
from Fortuna import QuantumMonty


quantum_monty = QuantumMonty(["Alpha", "Beta", "Delta", "Eta", "Gamma", "Kappa", "Zeta"])

# Each of the following methods will return a random value from the sequence.
quantum_monty.mostly_front()    # Mostly from the front of the list (geometric descending)
quantum_monty.mostly_middle()   # Mostly from the middle of the list (geometric pyramid)
quantum_monty.mostly_back()     # Mostly from the back of the list (geometric ascending)
quantum_monty.mostly_first()    # Mostly from the very front of the list (stretched gaussian descending)
quantum_monty.mostly_center()   # Mostly from the very center of the list (stretched gaussian bell curve)
quantum_monty.mostly_last()     # Mostly from the very back of the list (stretched gaussian ascending)
quantum_monty.quantum_monty()   # Quantum Monty Algorithm. Overlapping probability waves.
quantum_monty.mostly_flat()     # Uniform flat distribution (see Fortuna.random_value if this is the only behavior you need.)
quantum_monty.mostly_cycle()    # Cycled uniform flat distribution (see TruffleShuffle)
```

#### RandomWalk
RandomWalk wraps a sequence of values, the data is modeled as a continuous ring. The sequence must not be empty.
When instantiated, RandomWalk will randomly pick a starting point.
When called, the algorithm randomly walks to an adjacent position and returns the value.
RandomWalk will move forward or backward in the data set and never fall off the edge, instead it will wrap to the other side.

RandomWalk produces a uniform distribution.

```python
from Fortuna import RandomWalk


random_walk = RandomWalk(["Alpha", "Beta", "Delta", "Eta", "Gamma", "Kappa", "Zeta"])
random_walk()      # returns a random value from the table by randomly walking to an adjacent position.
```

### Table Wrappers
#### Weighted Choice: Custom Rarity
Two strategies for selecting random values from a sequence where rarity counts. Both produce a custom distribution of values based on the weights of the values. Up to 10x faster than random.choices()

WeightedChoice instances can return a list of samples rather than just one value, control the length of the list via the optional n_samples argument. By default n_samples=1.

WeightedChoice will recursively unpack callable objects in the data set. Callable objects that require arguments are returned in an uncalled state. To disable this behavior pass the optional argument flat=False during instantiation. By default flat=True.

- Constructor takes a copy of a sequence of weighted value pairs... `[(weight, value), ... ]`
- Automatically optimizes the sequence for correctness and optimal call performance for large data sets.
- The sequence must not be empty, and each pair must contain a weight and a value.
- Weights must be positive integers.
- Values can be any Python object that can be passed around... string, int, list, function etc.
- Performance scales by some fraction of the length of the sequence.

The following examples produce equivalent distributions with comparable performance.
The choice to use one strategy over the other is purely about which one suits you or your data best. Relative weights are easier to understand at a glance. However, many RPG Treasure Tables map rather nicely to a cumulative weighted strategy.

##### Cumulative Weight Strategy
_Note: Logic dictates Cumulative Weights must be unique!_

```python
from Fortuna import CumulativeWeightedChoice


cumulative_weighted_choice = CumulativeWeightedChoice([
    (7, "Apple"),
    (11, "Banana"),
    (13, "Cherry"),
    (23, "Grape"),
    (26, "Lime"),
    (30, "Orange"),
])

cumulative_weighted_choice()  # returns a weighted random value
```

##### Relative Weight Strategy

```python
from Fortuna import RelativeWeightedChoice


relative_weighted_choice = RelativeWeightedChoice([
    (7, "Apple"),
    (4, "Banana"),
    (2, "Cherry"),
    (10, "Grape"),
    (3, "Lime"),
    (4, "Orange"),
])

relative_weighted_choice()  # returns a weighted random value
```

#### CatWalk
CatWalk wraps a two dimensional sequence of values, the data is modeled as the surface of a torus or donut.
When called, the algorithm randomly walks to an adjacent position and returns the value.
CatWalk will move; up, down, forward, backward or diagonally in the data set. It will never fall off the edge, instead it will wrap to the other side.

Each sequence inside a CatWalk must be of equal length and must not be empty.

CatWalk produces a uniform distribution.

```python
from Fortuna import CatWalk


cat_walk = CatWalk([
    (10, 11, 12, 13, 14, 15),
    (20, 21, 22, 23, 24, 25),
    (30, 31, 32, 33, 34, 35),
])

cat_walk()      # returns a random value from the table by randomly walking in the two dimensional plane.
```

### Dictionary Wrappers
#### FlexCat
FlexCat wraps a dictionary of sequences. When the primary method is called it returns a random value from one of the sequences. It takes two optional keyword arguments to specify the algorithms used to make random selections.

By default, FlexCat will use y_bias="front" and x_bias="cycle", this will make the top of the data structure geometrically more common than the bottom and cycle the sequences. This config is known as Top Cat, it produces a descending-step cycled distribution for the data. Many other combinations are possible (9 algorithms, 2 dimensions = 81 configs).

FlexCat requires a dict with at least three sequences with at least 3 values each. Even though the total value limit is much higher, data sets with more than one million values are not recommended for all platforms.

FlexCat generally works best if all sequences in a set are sufficiently large and close to the same size, this is not enforced. Values in a shorter sequence will naturally be more common, since probability balancing between categories is not considered. For example: in a flat/flat set where it might be expected that all values have equal probability (and they would, given sequences with equal length). However, values in a sequence half the size of the others in the set would have exactly double the probability of the other items. This effect scales with the size delta and affects all nine methods. Cross category balancing might be considered for a future release.

FlexCat instances can return a list of samples rather than just one value, control the length of the list via the optional n_samples argument. By default n_samples=1.

FlexCat will recursively unpack callable objects in the data set. Callable objects that require arguments are returned in an uncalled state. To disable this behavior pass the optional argument flat=False during instantiation. By default flat=True.


Algorithm Options: _See QuantumMonty & TruffleShuffle for more details._
- front, geometric descending
- middle, geometric pyramid
- back, geometric ascending
- first, stretched gaussian descending
- center, stretched gaussian bell
- last, stretched gaussian ascending
- monty, The Quantum Monty
- flat, uniform flat
- cycle, TruffleShuffle uniform flat

```python
from Fortuna import FlexCat


flex_cat = FlexCat({
    "Cat_A": ("A1", "A2", "A3", "A4", "A5"),
    "Cat_B": ("B1", "B2", "B3", "B4", "B5"),
    "Cat_C": ("C1", "C2", "C3", "C4", "C5"),
}, y_bias="front", x_bias="cycle")

flex_cat()          # returns a random value from a random category
flex_cat("Cat_A")   # returns a random value from "Cat_A"
flex_cat("Cat_B")   #                             "Cat_B"
flex_cat("Cat_C")   #                             "Cat_C"
```

## Fortuna Test Suite
#### Testbed:
- **Software** _MacOS 10.14.2, Python 3.7.2, Fortuna Extension_
- **Hardware** _Intel 2.7GHz i7 Skylake, 16GB RAM, 1TB SSD_

```
Fortuna 0.23.4 Sample Distribution and Performance Test Suite

Random Numbers
-------------------------------------------------------------------------

Base Case:
random.randint(1, 10) x 10000: Total time: 15.76 ms, Average time: 1576 nano
 1: 10.0%
 2: 9.96%
 3: 9.9%
 4: 9.88%
 5: 10.25%
 6: 9.9%
 7: 10.2%
 8: 10.19%
 9: 9.97%
 10: 9.75%

random_range(1, 10) x 10000: Total time: 1.01 ms, Average time: 101 nano
 1: 10.32%
 2: 10.28%
 3: 9.43%
 4: 9.56%
 5: 10.04%
 6: 10.07%
 7: 10.32%
 8: 9.76%
 9: 9.87%
 10: 10.35%

Base Case:
random.randrange(10) x 10000: Total time: 10.19 ms, Average time: 1019 nano
 0: 9.58%
 1: 10.04%
 2: 10.41%
 3: 10.44%
 4: 10.39%
 5: 10.0%
 6: 10.03%
 7: 9.96%
 8: 9.39%
 9: 9.76%

random_below(10) x 10000: Total time: 0.91 ms, Average time: 91 nano
 0: 10.26%
 1: 10.1%
 2: 9.98%
 3: 10.07%
 4: 9.9%
 5: 9.52%
 6: 10.63%
 7: 10.3%
 8: 9.4%
 9: 9.84%

d(10) x 10000: Total time: 0.87 ms, Average time: 87 nano
 1: 9.89%
 2: 10.45%
 3: 10.06%
 4: 9.89%
 5: 10.13%
 6: 10.36%
 7: 10.04%
 8: 10.08%
 9: 9.37%
 10: 9.73%

dice(2, 6) x 10000: Total time: 1.17 ms, Average time: 117 nano
 2: 3.0%
 3: 5.48%
 4: 8.66%
 5: 11.16%
 6: 13.87%
 7: 16.11%
 8: 13.73%
 9: 11.1%
 10: 8.88%
 11: 5.6%
 12: 2.41%

plus_or_minus(5) x 10000: Total time: 0.76 ms, Average time: 76 nano
 -5: 9.2%
 -4: 9.03%
 -3: 8.95%
 -2: 9.3%
 -1: 8.76%
 0: 9.24%
 1: 9.52%
 2: 9.59%
 3: 8.57%
 4: 9.67%
 5: 8.17%

plus_or_minus_linear(5) x 10000: Total time: 1.04 ms, Average time: 104 nano
 -5: 3.06%
 -4: 5.23%
 -3: 8.45%
 -2: 11.89%
 -1: 13.82%
 0: 16.3%
 1: 13.31%
 2: 11.06%
 3: 8.5%
 4: 5.73%
 5: 2.65%

plus_or_minus_curve(5) x 10000: Total time: 1.22 ms, Average time: 122 nano
 -5: 0.18%
 -4: 1.05%
 -3: 4.34%
 -2: 10.97%
 -1: 20.78%
 0: 24.72%
 1: 20.53%
 2: 11.69%
 3: 4.46%
 4: 1.11%
 5: 0.17%

stretched_bell(5) x 10000: Total time: 1.26 ms, Average time: 126 nano
 -6: 0.01%
 -5: 0.24%
 -4: 1.05%
 -3: 4.24%
 -2: 11.43%
 -1: 20.7%
 0: 24.38%
 1: 20.75%
 2: 11.58%
 3: 4.29%
 4: 1.14%
 5: 0.17%
 6: 0.02%

zero_flat(10) x 10000: Total time: 0.81 ms, Average time: 81 nano
 0: 9.39%
 1: 9.18%
 2: 9.68%
 3: 9.41%
 4: 8.77%
 5: 9.12%
 6: 8.86%
 7: 8.93%
 8: 8.78%
 9: 9.01%
 10: 8.87%

zero_cool(10) x 10000: Total time: 1.78 ms, Average time: 178 nano
 0: 17.23%
 1: 14.31%
 2: 13.22%
 3: 11.83%
 4: 10.89%
 5: 9.26%
 6: 8.07%
 7: 6.01%
 8: 4.54%
 9: 3.18%
 10: 1.46%

zero_extreme(10) x 10000: Total time: 1.84 ms, Average time: 184 nano
 0: 22.38%
 1: 21.31%
 2: 18.21%
 3: 14.39%
 4: 10.46%
 5: 6.37%
 6: 3.49%
 7: 1.87%
 8: 0.94%
 9: 0.45%
 10: 0.13%

max_cool(10) x 10000: Total time: 1.79 ms, Average time: 179 nano
 0: 1.39%
 1: 3.16%
 2: 4.62%
 3: 5.99%
 4: 7.42%
 5: 9.3%
 6: 10.45%
 7: 11.96%
 8: 14.12%
 9: 14.99%
 10: 16.6%

max_extreme(10) x 10000: Total time: 1.9 ms, Average time: 190 nano
 0: 0.18%
 1: 0.35%
 2: 0.85%
 3: 2.03%
 4: 3.72%
 5: 6.44%
 6: 10.35%
 7: 14.4%
 8: 18.24%
 9: 20.97%
 10: 22.47%

mostly_middle(10) x 10000: Total time: 1.05 ms, Average time: 105 nano
 0: 2.73%
 1: 5.68%
 2: 8.31%
 3: 10.81%
 4: 13.38%
 5: 17.21%
 6: 13.93%
 7: 11.32%
 8: 8.29%
 9: 5.51%
 10: 2.83%

mostly_center(10) x 10000: Total time: 1.23 ms, Average time: 123 nano
 0: 0.17%
 1: 1.05%
 2: 4.52%
 3: 11.14%
 4: 20.69%
 5: 24.46%
 6: 20.31%
 7: 11.8%
 8: 4.41%
 9: 1.26%
 10: 0.19%


Random Truth
-------------------------------------------------------------------------

percent_true(25) x 10000: Total time: 0.72 ms, Average time: 72 nano
 False: 74.6%
 True: 25.4%


Random Values from a Sequence
-------------------------------------------------------------------------

Base Case:
random.choice(some_list) x 10000: Total time: 7.53 ms, Average time: 753 nano
 Alpha: 14.83%
 Beta: 14.0%
 Delta: 13.69%
 Eta: 14.49%
 Gamma: 13.93%
 Kappa: 14.35%
 Zeta: 14.71%

random_value(some_list) x 10000: Total time: 0.69 ms, Average time: 69 nano
 Alpha: 14.1%
 Beta: 14.28%
 Delta: 13.45%
 Eta: 14.56%
 Gamma: 14.12%
 Kappa: 15.1%
 Zeta: 14.39%

monty.mostly_flat() x 10000: Total time: 1.99 ms, Average time: 199 nano
 Alpha: 14.68%
 Beta: 13.95%
 Delta: 14.46%
 Eta: 13.88%
 Gamma: 14.54%
 Kappa: 14.46%
 Zeta: 14.03%

monty.mostly_middle() x 10000: Total time: 2.17 ms, Average time: 217 nano
 Alpha: 6.38%
 Beta: 12.22%
 Delta: 18.19%
 Eta: 24.94%
 Gamma: 19.32%
 Kappa: 12.42%
 Zeta: 6.53%

monty.mostly_center() x 10000: Total time: 2.55 ms, Average time: 255 nano
 Alpha: 0.44%
 Beta: 5.32%
 Delta: 24.47%
 Eta: 39.33%
 Gamma: 24.49%
 Kappa: 5.55%
 Zeta: 0.4%

monty.mostly_front() x 10000: Total time: 2.8 ms, Average time: 280 nano
 Alpha: 25.41%
 Beta: 20.97%
 Delta: 18.21%
 Eta: 13.97%
 Gamma: 10.51%
 Kappa: 7.3%
 Zeta: 3.63%

monty.mostly_back() x 10000: Total time: 2.77 ms, Average time: 277 nano
 Alpha: 3.52%
 Beta: 7.18%
 Delta: 11.23%
 Eta: 14.11%
 Gamma: 17.68%
 Kappa: 21.04%
 Zeta: 25.24%

monty.mostly_first() x 10000: Total time: 3.09 ms, Average time: 309 nano
 Alpha: 34.91%
 Beta: 30.32%
 Delta: 20.01%
 Eta: 9.89%
 Gamma: 3.46%
 Kappa: 1.1%
 Zeta: 0.31%

monty.mostly_last() x 10000: Total time: 3.1 ms, Average time: 310 nano
 Alpha: 0.3%
 Beta: 1.3%
 Delta: 3.82%
 Eta: 10.05%
 Gamma: 20.23%
 Kappa: 29.28%
 Zeta: 35.02%

monty.quantum_monty() x 10000: Total time: 5.51 ms, Average time: 551 nano
 Alpha: 11.92%
 Beta: 12.95%
 Delta: 15.86%
 Eta: 19.24%
 Gamma: 16.06%
 Kappa: 12.92%
 Zeta: 11.05%

monty.mostly_cycle() x 10000: Total time: 6.03 ms, Average time: 603 nano
 Alpha: 14.53%
 Beta: 14.68%
 Delta: 14.02%
 Eta: 13.99%
 Gamma: 13.99%
 Kappa: 14.5%
 Zeta: 14.29%

truffle_shuffle() x 10000: Total time: 5.56 ms, Average time: 556 nano
 Alpha: 14.14%
 Beta: 14.17%
 Delta: 14.15%
 Eta: 14.58%
 Gamma: 14.57%
 Kappa: 14.06%
 Zeta: 14.33%


Random Values by Weighted Table
-------------------------------------------------------------------------

Cumulative Base Case:
random.choices(population, cum_weights=cum_weights) x 10000: Total time: 18.97 ms, Average time: 1897 nano
 Apple: 23.47%
 Banana: 13.29%
 Cherry: 6.06%
 Grape: 33.24%
 Lime: 10.05%
 Orange: 13.89%

Relative Base Case:
random.choices(population, rel_weights) x 10000: Total time: 22.15 ms, Average time: 2215 nano
 Apple: 23.44%
 Banana: 13.23%
 Cherry: 6.62%
 Grape: 33.7%
 Lime: 10.1%
 Orange: 12.91%

Fortuna.cumulative_weighted_choice(cumulative_table) x 10000: Total time: 1.55 ms, Average time: 155 nano
 Apple: 23.97%
 Banana: 12.85%
 Cherry: 6.55%
 Grape: 33.64%
 Lime: 9.85%
 Orange: 13.14%

cumulative_choice() x 10000: Total time: 3.6 ms, Average time: 360 nano
 Apple: 22.93%
 Banana: 13.19%
 Cherry: 6.67%
 Grape: 33.94%
 Lime: 10.0%
 Orange: 13.27%

relative_choice() x 10000: Total time: 3.6 ms, Average time: 360 nano
 Apple: 23.87%
 Banana: 13.32%
 Cherry: 6.58%
 Grape: 33.85%
 Lime: 10.16%
 Orange: 12.22%


Random Values by Category
-------------------------------------------------------------------------

flex_cat('Cat_A') x 10000: Total time: 6.33 ms, Average time: 633 nano
 A1: 33.95%
 A2: 33.05%
 A3: 33.0%

flex_cat('Cat_B') x 10000: Total time: 6.35 ms, Average time: 635 nano
 B1: 33.0%
 B2: 33.19%
 B3: 33.81%

flex_cat('Cat_C') x 10000: Total time: 6.46 ms, Average time: 646 nano
 C1: 33.66%
 C2: 33.4%
 C3: 32.94%

flex_cat() x 10000: Total time: 9.28 ms, Average time: 928 nano
 A1: 16.9%
 A2: 16.83%
 A3: 16.42%
 B1: 10.74%
 B2: 11.12%
 B3: 11.09%
 C1: 5.67%
 C2: 5.84%
 C3: 5.39%


Random Walks
-------------------------------------------------------------------------

random_walk() x 10000: Total time: 3.3 ms, Average time: 330 nano
 Alpha: 14.47%
 Beta: 14.62%
 Delta: 14.77%
 Eta: 14.73%
 Gamma: 13.99%
 Kappa: 13.61%
 Zeta: 13.81%

catwalk() x 10000: Total time: 4.91 ms, Average time: 491 nano
 10: 6.74%
 11: 6.7%
 12: 6.56%
 13: 6.84%
 14: 7.11%
 20: 6.77%
 21: 6.66%
 22: 6.49%
 23: 6.8%
 24: 6.61%
 30: 6.78%
 31: 6.12%
 32: 6.43%
 33: 6.76%
 34: 6.63%


List Shuffle
-------------------------------------------------------------------------

Base Case:
random.shuffle(shuffle_list) x 10000: Total time: 71.35 ms, Average time: 7135 nano
 None: 100.0%

Fortuna.shuffle(shuffle_list) x 10000: Total time: 3.49 ms, Average time: 349 nano
 None: 100.0%


-------------------------------------------------------------------------
Total Test Time: 0.31 sec
```

## Fortuna Development Log
##### Fortuna 0.23.4, first release candidate.
- RandomCycle, BlockCycle and TruffleShuffle have been refactored and combined into one class: TruffleShuffle.
- QuantumMonty and FlexCat will now use the new TruffleShuffle for cycling.
- Minor refactoring across the module.

##### Fortuna 0.23.3, internal
- Function shuffle(arr: list) added.

##### Fortuna 0.23.2, internal
- Simplified the plus_or_minus_curve(num: int) function, output will now always be bounded to the range [-num..num].
- Function stretched_bell(num: int) added, this matches the previous behavior of an unbounded plus_or_minus_curve.

##### Fortuna 0.23.1, internal
- Small bug fixes and general clean up.

##### Fortuna 0.23.0
- The number of test cycles in the test suite has been reduced to 10,000 (down from 100,000). The performance of the pure python implementation and the c-extension are now directly comparable.
- Minor tweaks made to the examples in `.../fortuna_extras/fortuna_examples.py`

##### Fortuna 0.22.2
- BlockCycle class added.
- RandomWalk class added.
- CatWalk class added.

##### Fortuna 0.22.1
- Fortuna classes no longer return lists of values, this behavior has been extracted to a free function called n_samples.

##### Fortuna 0.22.0
- Fortuna 0.22.x may introduce breaking changes.
- Function bind added.
- Function n_samples added.

##### Fortuna 0.21.3
- Flatten will no longer raise an error if passed a callable item that it can't call. It correctly returns such items in an uncalled state without error.
- Simplified `.../fortuna_extras/fortuna_examples.py` - removed unnecessary class structure.

##### Fortuna 0.21.2
- Fix some minor bugs.

##### Fortuna 0.21.1
- Fixed a bug in `.../fortuna_extras/fortuna_examples.py`

##### Fortuna 0.21.0
- Function flatten added.
- The Fortuna classes will recursively unpack callable objects in the data set via flatten.

##### Fortuna 0.20.10
- Documentation updated.

##### Fortuna 0.20.9
- Minor bug fixes.

##### Fortuna 0.20.8, internal
- Testing cycle for potential new features.

##### Fortuna 0.20.7
- Documentation updated for clarity.

##### Fortuna 0.20.6
- Tests updated based on recent changes.

##### Fortuna 0.20.5, internal
- Documentation updated based on recent changes.

##### Fortuna 0.20.4, internal
- WeightedChoice (both types) can optionally return a list of samples rather than just one value, control the length of the list via the n_samples argument.

##### Fortuna 0.20.3, internal
- RandomCycle can optionally return a list of samples rather than just one value,
control the length of the list via the n_samples argument.

##### Fortuna 0.20.2, internal
- QuantumMonty can optionally return a list of samples rather than just one value,
control the length of the list via the n_samples argument.

##### Fortuna 0.20.1, internal
- FlexCat can optionally return a list of samples rather than just one value,
control the length of the list via the n_samples argument.

##### Fortuna 0.20.0, internal
- FlexCat now accepts a standard dict as input. The ordered(ness) of dict is now part of the standard in Python 3.7.1. Previously FlexCat required an OrderedDict, now it accepts either and treats them the same.

##### Fortuna 0.19.7
- Fixed bug in `.../fortuna_extras/fortuna_examples.py`.

##### Fortuna 0.19.6
- Updated documentation formatting.
- Small performance tweak for QuantumMonty and FlexCat.

##### Fortuna 0.19.5
- Minor documentation update.

##### Fortuna 0.19.4
- Minor update to all classes for better debugging.

##### Fortuna 0.19.3
- Updated plus_or_minus_curve to allow unbounded output.

##### Fortuna 0.19.2
- Internal development cycle.
- Minor update to FlexCat for better debugging.

##### Fortuna 0.19.1
- Internal development cycle.

##### Fortuna 0.19.0
- Updated documentation for clarity.
- MultiCat has been removed, it is replaced by FlexCat.
- Mostly has been removed, it is replaced by QuantumMonty.

##### Fortuna 0.18.7
- Fixed some more README typos.

##### Fortuna 0.18.6
- Fixed some README typos.

##### Fortuna 0.18.5
- Updated documentation.
- Fixed another minor test bug.

##### Fortuna 0.18.4
- Updated documentation to reflect recent changes.
- Fixed some small test bugs.
- Reduced default number of test cycles to 10,000 - down from 100,000.

##### Fortuna 0.18.3
- Fixed some minor README typos.

##### Fortuna 0.18.2
- Fixed a bug with Fortuna Pure.

##### Fortuna 0.18.1
- Fixed some minor typos.
- Added tests for `.../fortuna_extras/fortuna_pure.py`

##### Fortuna 0.18.0
- Introduced new test format, now includes average call time in nanoseconds.
- Reduced default number of test cycles to 100,000 - down from 1,000,000.
- Added pure Python implementation of Fortuna: `.../fortuna_extras/fortuna_pure.py`
- Promoted several low level functions to top level.
    - `zero_flat(num: int) -> int`
    - `zero_cool(num: int) -> int`
    - `zero_extreme(num: int) -> int`
    - `max_cool(num: int) -> int`
    - `max_extreme(num: int) -> int`
    - `analytic_continuation(func: staticmethod, num: int) -> int`
    - `min_max(num: int, lo: int, hi: int) -> int`

##### Fortuna 0.17.3
- Internal development cycle.

##### Fortuna 0.17.2
- User Requested: dice() and d() functions now support negative numbers as input.

##### Fortuna 0.17.1
- Fixed some minor typos.

##### Fortuna 0.17.0
- Added QuantumMonty to replace Mostly, same default behavior with more options.
- Mostly is depreciated and may be removed in a future release.
- Added FlexCat to replace MultiCat, same default behavior with more options.
- MultiCat is depreciated and may be removed in a future release.
- Expanded the Treasure Table example in `.../fortuna_extras/fortuna_examples.py`

##### Fortuna 0.16.2
- Minor refactoring for WeightedChoice.

##### Fortuna 0.16.1
- Redesigned fortuna_examples.py to feature a dynamic random magic item generator.
- Raised cumulative_weighted_choice function to top level.
- Added test for cumulative_weighted_choice as free function.
- Updated MultiCat documentation for clarity.

##### Fortuna 0.16.0
- Pushed distribution_timer to the .pyx layer.
- Changed default number of iterations of tests to 1 million, up form 1 hundred thousand.
- Reordered tests to better match documentation.
- Added Base Case Fortuna.fast_rand_below.
- Added Base Case Fortuna.fast_d.
- Added Base Case Fortuna.fast_dice.

##### Fortuna 0.15.10
- Internal Development Cycle

##### Fortuna 0.15.9
- Added Base Cases for random.choices()
- Added Base Case for randint_dice()

##### Fortuna 0.15.8
- Clarified MultiCat Test

##### Fortuna 0.15.7
- Fixed minor typos.

##### Fortuna 0.15.6
- Fixed minor typos.
- Simplified MultiCat example.

##### Fortuna 0.15.5
- Added MultiCat test.
- Fixed some minor typos in docs.

##### Fortuna 0.15.4
- Performance optimization for both WeightedChoice() variants.
- Cython update provides small performance enhancement across the board.
- Compilation now leverages Python3 all the way down.
- MultiCat pushed to the .pyx layer for better performance.

##### Fortuna 0.15.3
- Reworked the MultiCat example to include several randomizing strategies working in concert.
- Added Multi Dice 10d10 performance tests.
- Updated sudo code in documentation to be more pythonic.

##### Fortuna 0.15.2
- Fixed: Linux installation failure.
- Added: complete source files to the distribution (.cpp .hpp .pyx).

##### Fortuna 0.15.1
- Updated & simplified distribution_timer in `fortuna_tests.py`
- Readme updated, fixed some typos.
- Known issue preventing successful installation on some linux platforms.

##### Fortuna 0.15.0
- Performance tweaks.
- Readme updated, added some details.

##### Fortuna 0.14.1
- Readme updated, fixed some typos.

##### Fortuna 0.14.0
- Fixed a bug where the analytic continuation algorithm caused a rare issue during compilation on some platforms.

##### Fortuna 0.13.3
- Fixed Test Bug: percent sign was missing in output distributions.
- Readme updated: added update history, fixed some typos.

##### Fortuna 0.13.2
- Readme updated for even more clarity.

##### Fortuna 0.13.1
- Readme updated for clarity.

##### Fortuna 0.13.0
- Minor Bug Fixes.
- Readme updated for aesthetics.
- Added Tests: `.../fortuna_extras/fortuna_tests.py`

##### Fortuna 0.12.0
- Internal test for future update.

##### Fortuna 0.11.0
- Initial Release: Public Beta

##### Fortuna 0.10.0
- Module name changed from Dice to Fortuna

##### Dice 0.1.x - 0.9.x
- Experimental Phase

## Legal Information
Fortuna © 2018 Broken aka Robert W Sharp, all rights reserved.

Fortuna is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License.

See online version of this license here: <http://creativecommons.org/licenses/by-nc/3.0/>

```
License
-------

THE WORK (AS DEFINED BELOW) IS PROVIDED UNDER THE TERMS OF THIS CREATIVE
COMMONS PUBLIC LICENSE ("CCPL" OR "LICENSE"). THE WORK IS PROTECTED BY
COPYRIGHT AND/OR OTHER APPLICABLE LAW. ANY USE OF THE WORK OTHER THAN AS
AUTHORIZED UNDER THIS LICENSE OR COPYRIGHT LAW IS PROHIBITED.

BY EXERCISING ANY RIGHTS TO THE WORK PROVIDED HERE, YOU ACCEPT AND AGREE TO BE
BOUND BY THE TERMS OF THIS LICENSE. TO THE EXTENT THIS LICENSE MAY BE
CONSIDERED TO BE A CONTRACT, THE LICENSOR GRANTS YOU THE RIGHTS CONTAINED HERE
IN CONSIDERATION OF YOUR ACCEPTANCE OF SUCH TERMS AND CONDITIONS.

1. Definitions

  a. "Adaptation" means a work based upon the Work, or upon the Work and other
  pre-existing works, such as a translation, adaptation, derivative work,
  arrangement of music or other alterations of a literary or artistic work, or
  phonogram or performance and includes cinematographic adaptations or any
  other form in which the Work may be recast, transformed, or adapted
  including in any form recognizably derived from the original, except that a
  work that constitutes a Collection will not be considered an Adaptation for
  the purpose of this License. For the avoidance of doubt, where the Work is a
  musical work, performance or phonogram, the synchronization of the Work in
  timed-relation with a moving image ("synching") will be considered an
  Adaptation for the purpose of this License.

  b. "Collection" means a collection of literary or artistic works, such as
  encyclopedias and anthologies, or performances, phonograms or broadcasts, or
  other works or subject matter other than works listed in Section 1(f) below,
  which, by reason of the selection and arrangement of their contents,
  constitute intellectual creations, in which the Work is included in its
  entirety in unmodified form along with one or more other contributions, each
  constituting separate and independent works in themselves, which together
  are assembled into a collective whole. A work that constitutes a Collection
  will not be considered an Adaptation (as defined above) for the purposes of
  this License.

  c. "Distribute" means to make available to the public the original and
  copies of the Work or Adaptation, as appropriate, through sale or other
  transfer of ownership.

  d. "Licensor" means the individual, individuals, entity or entities that
  offer(s) the Work under the terms of this License.

  e. "Original Author" means, in the case of a literary or artistic work, the
  individual, individuals, entity or entities who created the Work or if no
  individual or entity can be identified, the publisher; and in addition (i)
  in the case of a performance the actors, singers, musicians, dancers, and
  other persons who act, sing, deliver, declaim, play in, interpret or
  otherwise perform literary or artistic works or expressions of folklore;
  (ii) in the case of a phonogram the producer being the person or legal
  entity who first fixes the sounds of a performance or other sounds; and,
  (iii) in the case of broadcasts, the organization that transmits the
  broadcast.

  f. "Work" means the literary and/or artistic work offered under the terms of
  this License including without limitation any production in the literary,
  scientific and artistic domain, whatever may be the mode or form of its
  expression including digital form, such as a book, pamphlet and other
  writing; a lecture, address, sermon or other work of the same nature; a
  dramatic or dramatico-musical work; a choreographic work or entertainment in
  dumb show; a musical composition with or without words; a cinematographic
  work to which are assimilated works expressed by a process analogous to
  cinematography; a work of drawing, painting, architecture, sculpture,
  engraving or lithography; a photographic work to which are assimilated works
  expressed by a process analogous to photography; a work of applied art; an
  illustration, map, plan, sketch or three-dimensional work relative to
  geography, topography, architecture or science; a performance; a broadcast;
  a phonogram; a compilation of data to the extent it is protected as a
  copyrightable work; or a work performed by a variety or circus performer to
  the extent it is not otherwise considered a literary or artistic work.

  g. "You" means an individual or entity exercising rights under this License
  who has not previously violated the terms of this License with respect to
  the Work, or who has received express permission from the Licensor to
  exercise rights under this License despite a previous violation.

  h. "Publicly Perform" means to perform public recitations of the Work and to
  communicate to the public those public recitations, by any means or process,
  including by wire or wireless means or public digital performances; to make
  available to the public Works in such a way that members of the public may
  access these Works from a place and at a place individually chosen by them;
  to perform the Work to the public by any means or process and the
  communication to the public of the performances of the Work, including by
  public digital performance; to broadcast and rebroadcast the Work by any
  means including signs, sounds or images.

  i. "Reproduce" means to make copies of the Work by any means including
  without limitation by sound or visual recordings and the right of fixation
  and reproducing fixations of the Work, including storage of a protected
  performance or phonogram in digital form or other electronic medium.

2. Fair Dealing Rights. Nothing in this License is intended to reduce, limit,
or restrict any uses free from copyright or rights arising from limitations or
exceptions that are provided for in connection with the copyright protection
under copyright law or other applicable laws.

3. License Grant. Subject to the terms and conditions of this License,
Licensor hereby grants You a worldwide, royalty-free, non-exclusive, perpetual
(for the duration of the applicable copyright) license to exercise the rights
in the Work as stated below:

  a. to Reproduce the Work, to incorporate the Work into one or more
  Collections, and to Reproduce the Work as incorporated in the Collections;

  b. to create and Reproduce Adaptations provided that any such Adaptation,
  including any translation in any medium, takes reasonable steps to clearly
  label, demarcate or otherwise identify that changes were made to the
  original Work. For example, a translation could be marked "The original work
  was translated from English to Spanish," or a modification could indicate
  "The original work has been modified.";

  c. to Distribute and Publicly Perform the Work including as incorporated in
  Collections; and,

  d. to Distribute and Publicly Perform Adaptations.

The above rights may be exercised in all media and formats whether now known
or hereafter devised. The above rights include the right to make such
modifications as are technically necessary to exercise the rights in other
media and formats. Subject to Section 8(f), all rights not expressly granted
by Licensor are hereby reserved, including but not limited to the rights set
forth in Section 4(d).

4. Restrictions. The license granted in Section 3 above is expressly made
subject to and limited by the following restrictions:

  a. You may Distribute or Publicly Perform the Work only under the terms of
  this License. You must include a copy of, or the Uniform Resource Identifier
  (URI) for, this License with every copy of the Work You Distribute or
  Publicly Perform. You may not offer or impose any terms on the Work that
  restrict the terms of this License or the ability of the recipient of the
  Work to exercise the rights granted to that recipient under the terms of the
  License. You may not sublicense the Work. You must keep intact all notices
  that refer to this License and to the disclaimer of warranties with every
  copy of the Work You Distribute or Publicly Perform. When You Distribute or
  Publicly Perform the Work, You may not impose any effective technological
  measures on the Work that restrict the ability of a recipient of the Work
  from You to exercise the rights granted to that recipient under the terms of
  the License. This Section 4(a) applies to the Work as incorporated in a
  Collection, but this does not require the Collection apart from the Work
  itself to be made subject to the terms of this License. If You create a
  Collection, upon notice from any Licensor You must, to the extent
  practicable, remove from the Collection any credit as required by Section
  4(c), as requested. If You create an Adaptation, upon notice from any
  Licensor You must, to the extent practicable, remove from the Adaptation any
  credit as required by Section 4(c), as requested.

  b. You may not exercise any of the rights granted to You in Section 3 above
  in any manner that is primarily intended for or directed toward commercial
  advantage or private monetary compensation. The exchange of the Work for
  other copyrighted works by means of digital file-sharing or otherwise shall
  not be considered to be intended for or directed toward commercial advantage
  or private monetary compensation, provided there is no payment of any
  monetary compensation in connection with the exchange of copyrighted works.

  c. If You Distribute, or Publicly Perform the Work or any Adaptations or
  Collections, You must, unless a request has been made pursuant to Section
  4(a), keep intact all copyright notices for the Work and provide, reasonable
  to the medium or means You are utilizing: (i) the name of the Original
  Author (or pseudonym, if applicable) if supplied, and/or if the Original
  Author and/or Licensor designate another party or parties (e.g., a sponsor
  institute, publishing entity, journal) for attribution ("Attribution
  Parties") in Licensor's copyright notice, terms of service or by other
  reasonable means, the name of such party or parties; (ii) the title of the
  Work if supplied; (iii) to the extent reasonably practicable, the URI, if
  any, that Licensor specifies to be associated with the Work, unless such URI
  does not refer to the copyright notice or licensing information for the
  Work; and, (iv) consistent with Section 3(b), in the case of an Adaptation,
  a credit identifying the use of the Work in the Adaptation (e.g., "French
  translation of the Work by Original Author," or "Screenplay based on
  original Work by Original Author"). The credit required by this Section 4(c)
  may be implemented in any reasonable manner; provided, however, that in the
  case of a Adaptation or Collection, at a minimum such credit will appear, if
  a credit for all contributing authors of the Adaptation or Collection
  appears, then as part of these credits and in a manner at least as prominent
  as the credits for the other contributing authors. For the avoidance of
  doubt, You may only use the credit required by this Section for the purpose
  of attribution in the manner set out above and, by exercising Your rights
  under this License, You may not implicitly or explicitly assert or imply any
  connection with, sponsorship or endorsement by the Original Author, Licensor
  and/or Attribution Parties, as appropriate, of You or Your use of the Work,
  without the separate, express prior written permission of the Original
  Author, Licensor and/or Attribution Parties.

  d. For the avoidance of doubt:

    i. Non-waivable Compulsory License Schemes. In those jurisdictions in
    which the right to collect royalties through any statutory or compulsory
    licensing scheme cannot be waived, the Licensor reserves the exclusive
    right to collect such royalties for any exercise by You of the rights
    granted under this License;

    ii. Waivable Compulsory License Schemes. In those jurisdictions in which
    the right to collect royalties through any statutory or compulsory
    licensing scheme can be waived, the Licensor reserves the exclusive right
    to collect such royalties for any exercise by You of the rights granted
    under this License if Your exercise of such rights is for a purpose or use
    which is otherwise than noncommercial as permitted under Section 4(b) and
    otherwise waives the right to collect royalties through any statutory or
    compulsory licensing scheme; and,

    iii. Voluntary License Schemes. The Licensor reserves the right to collect
    royalties, whether individually or, in the event that the Licensor is a
    member of a collecting society that administers voluntary licensing
    schemes, via that society, from any exercise by You of the rights granted
    under this License that is for a purpose or use which is otherwise than
    noncommercial as permitted under Section 4(c).

  e. Except as otherwise agreed in writing by the Licensor or as may be
  otherwise permitted by applicable law, if You Reproduce, Distribute or
  Publicly Perform the Work either by itself or as part of any Adaptations or
  Collections, You must not distort, mutilate, modify or take other derogatory
  action in relation to the Work which would be prejudicial to the Original
  Author's honor or reputation. Licensor agrees that in those jurisdictions
  (e.g. Japan), in which any exercise of the right granted in Section 3(b) of
  this License (the right to make Adaptations) would be deemed to be a
  distortion, mutilation, modification or other derogatory action prejudicial
  to the Original Author's honor and reputation, the Licensor will waive or
  not assert, as appropriate, this Section, to the fullest extent permitted by
  the applicable national law, to enable You to reasonably exercise Your right
  under Section 3(b) of this License (right to make Adaptations) but not
  otherwise.

5. Representations, Warranties and Disclaimer

UNLESS OTHERWISE MUTUALLY AGREED TO BY THE PARTIES IN WRITING, LICENSOR OFFERS
THE WORK AS-IS AND MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND
CONCERNING THE WORK, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE, INCLUDING,
WITHOUT LIMITATION, WARRANTIES OF TITLE, MERCHANTIBILITY, FITNESS FOR A
PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER
DEFECTS, ACCURACY, OR THE PRESENCE OF ABSENCE OF ERRORS, WHETHER OR NOT
DISCOVERABLE. SOME JURISDICTIONS DO NOT ALLOW THE EXCLUSION OF IMPLIED
WARRANTIES, SO SUCH EXCLUSION MAY NOT APPLY TO YOU.

6. Limitation on Liability. EXCEPT TO THE EXTENT REQUIRED BY APPLICABLE LAW,
IN NO EVENT WILL LICENSOR BE LIABLE TO YOU ON ANY LEGAL THEORY FOR ANY
SPECIAL, INCIDENTAL, CONSEQUENTIAL, PUNITIVE OR EXEMPLARY DAMAGES ARISING OUT
OF THIS LICENSE OR THE USE OF THE WORK, EVEN IF LICENSOR HAS BEEN ADVISED OF
THE POSSIBILITY OF SUCH DAMAGES.

7. Termination

  a. This License and the rights granted hereunder will terminate
  automatically upon any breach by You of the terms of this License.
  Individuals or entities who have received Adaptations or Collections from
  You under this License, however, will not have their licenses terminated
  provided such individuals or entities remain in full compliance with those
  licenses. Sections 1, 2, 5, 6, 7, and 8 will survive any termination of this
  License.

  b. Subject to the above terms and conditions, the license granted here is
  perpetual (for the duration of the applicable copyright in the Work).
  Notwithstanding the above, Licensor reserves the right to release the Work
  under different license terms or to stop distributing the Work at any time;
  provided, however that any such election will not serve to withdraw this
  License (or any other license that has been, or is required to be, granted
  under the terms of this License), and this License will continue in full
  force and effect unless terminated as stated above.

8. Miscellaneous

  a. Each time You Distribute or Publicly Perform the Work or a Collection,
  the Licensor offers to the recipient a license to the Work on the same terms
  and conditions as the license granted to You under this License.

  b. Each time You Distribute or Publicly Perform an Adaptation, Licensor
  offers to the recipient a license to the original Work on the same terms and
  conditions as the license granted to You under this License.

  c. If any provision of this License is invalid or unenforceable under
  applicable law, it shall not affect the validity or enforceability of the
  remainder of the terms of this License, and without further action by the
  parties to this agreement, such provision shall be reformed to the minimum
  extent necessary to make such provision valid and enforceable.

  d. No term or provision of this License shall be deemed waived and no breach
  consented to unless such waiver or consent shall be in writing and signed by
  the party to be charged with such waiver or consent.

  e. This License constitutes the entire agreement between the parties with
  respect to the Work licensed here. There are no understandings, agreements
  or representations with respect to the Work not specified here. Licensor
  shall not be bound by any additional provisions that may appear in any
  communication from You. This License may not be modified without the mutual
  written agreement of the Licensor and You.

  f. The rights granted under, and the subject matter referenced, in this
  License were drafted utilizing the terminology of the Berne Convention for
  the Protection of Literary and Artistic Works (as amended on September 28,
  1979), the Rome Convention of 1961, the WIPO Copyright Treaty of 1996, the
  WIPO Performances and Phonograms Treaty of 1996 and the Universal Copyright
  Convention (as revised on July 24, 1971). These rights and subject matter
  take effect in the relevant jurisdiction in which the License terms are
  sought to be enforced according to the corresponding provisions of the
  implementation of those treaty provisions in the applicable national law. If
  the standard suite of rights granted under applicable copyright law includes
  additional rights not granted under this License, such additional rights are
  deemed to be included in the License; this License is not intended to
  restrict the license of any rights under applicable law.
```
