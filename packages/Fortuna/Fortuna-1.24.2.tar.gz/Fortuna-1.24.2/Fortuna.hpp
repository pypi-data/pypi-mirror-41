#pragma once
#include <random>
#include <functional>
#include <algorithm>
#include <cmath>

namespace Fortuna {

namespace RNG {
    static std::random_device hardware_seed;
    static std::mt19937_64 generator(hardware_seed());
}

int random_range(int lo, int hi) {
    if (lo < hi) {
        std::uniform_int_distribution<int> distribution(lo, hi);
        return distribution(Fortuna::RNG::generator);
    }
    else if (hi == lo) return hi;
    else return Fortuna::random_range(hi, lo);
}

double random_float() {
    static std::uniform_real_distribution<> distribution(0.0, 1.0);
    return distribution(Fortuna::RNG::generator);
}

int analytic_continuation(const std::function<int(int)> & func, int num) {
    if (num < 0) return -func(-num);
    else if (num == 0) return 0;
    else return func(num);
}

int random_below(int size) {
    if (size > 0) return Fortuna::random_range(0, size - 1);
    else return Fortuna::analytic_continuation(random_below, size);
}

int d(int sides) {
    if (sides > 0) return Fortuna::random_range(1, sides);
    else return Fortuna::analytic_continuation(d, sides);
}

int dice(int rolls, int sides) {
    if (rolls > 0) {
        int total = 0;
        for (int i=0; i<rolls; ++i) total += Fortuna::d(sides);
        return total;
    }
    else if (rolls == 0) return 0;
    else return -Fortuna::dice(-rolls, sides);
}

bool percent_true(int num) {
    return Fortuna::d(100) <= num;
}

bool percent_true_float(double num) {
    return Fortuna::random_below(100) + Fortuna::random_float() <= num;
}

int min_max(int target, int lo, int hi) {
    if (lo < hi) return std::min(std::max(target, lo), hi);
    else if (lo == hi) return hi;
    else return Fortuna::min_max(target, hi, lo);
}

int plus_or_minus(int num) {
    return Fortuna::random_range(-num, num);
}

int plus_or_minus_linear(int num) {
    const int n = std::abs(num);
    return Fortuna::dice(2, n + 1) - (n + 2);
}

int stretched_bell(int num) {
    const double PI = 3.14159265359;
    std::normal_distribution<double> distribution(0.0, num / PI);
    return round(distribution(RNG::generator));
}

int plus_or_minus_curve(int num) {
    const int n = std::abs(num);
    int result = Fortuna::stretched_bell(n);
    while (result < -n or result > n) { result = Fortuna::stretched_bell(n); };
    return result;
}

int zero_flat(int num) {
    return Fortuna::random_range(0, num);
}

int zero_cool(int num) {
    if (num > 0) {
        int result = Fortuna::plus_or_minus_linear(num);
        while (result < 0) { result = Fortuna::plus_or_minus_linear(num); };
        return result;
    } else return Fortuna::analytic_continuation(Fortuna::zero_cool, num);
}

int zero_extreme(int num) {
    if (num > 0) {
        int result = Fortuna::plus_or_minus_curve(num);
        while (result < 0) { result = Fortuna::plus_or_minus_curve(num); };
        return result;
    } else return Fortuna::analytic_continuation(Fortuna::zero_extreme, num);
}

int max_cool(int num) {
    if (num > 0) return num - Fortuna::zero_cool(num);
    else return Fortuna::analytic_continuation(Fortuna::max_cool, num);
}

int max_extreme(int num) {
    if (num > 0) return num - Fortuna::zero_extreme(num);
    else return Fortuna::analytic_continuation(Fortuna::max_extreme, num);
}

int mostly_middle(int num) {
    if (num > 0) {
        const int mid_point = num / 2;
        if (num % 2 == 0) return Fortuna::plus_or_minus_linear(mid_point) + mid_point;
        else if (Fortuna::percent_true(50)) return Fortuna::max_cool(mid_point);
        else return 1 + Fortuna::zero_cool(mid_point) + mid_point;
    } else return Fortuna::analytic_continuation(Fortuna::mostly_middle, num);
}

int mostly_center(int num) {
    if (num > 0) {
        const int mid_point = num / 2;
        if (num % 2 == 0) return Fortuna::plus_or_minus_curve(mid_point) + mid_point;
        else if (Fortuna::percent_true(50)) return Fortuna::max_extreme(mid_point);
        else return 1 + Fortuna::zero_extreme(mid_point) + mid_point;
    } else return Fortuna::analytic_continuation(Fortuna::mostly_center, num);
}

int ability_dice(int num) {
    const int n = Fortuna::min_max(num, 3, 9);
    if (n == 3) return Fortuna::dice(3, 6);
    std::vector<int> theRolls(n);
    std::generate(begin(theRolls), end(theRolls), []() { return Fortuna::d(6); });
    std::sort(begin(theRolls), end(theRolls), std::greater<int>());
    return std::accumulate(begin(theRolls), begin(theRolls) + 3, 0);
}

int half_the_zeros(const std::function<int(int)> & func, int num) {
    if (Fortuna::percent_true(50)) return func(num);
    else {
        int t = 0;
        while (t == 0) t = func(num);
        return t;
    }
}

int plus_or_minus_linear_down(int num) {
    if (num == 0) return 0;
    const int n = std::abs(num);
    if (Fortuna::percent_true(50)) return Fortuna::half_the_zeros(max_cool, n);
    else return Fortuna::half_the_zeros(Fortuna::max_cool, -n);
}

int plus_or_minus_curve_down(int num) {
    if (num == 0) return 0;
    const int n = std::abs(num);
    if (Fortuna::percent_true(50)) return Fortuna::half_the_zeros(max_extreme, n);
    else return Fortuna::half_the_zeros(Fortuna::max_extreme, -n);
}

int mostly_not_middle(int num) {
    if (num > 0) {
        const int mid_point = num / 2;
        if (num % 2 == 0) return Fortuna::plus_or_minus_linear_down(mid_point) + mid_point;
        else if (Fortuna::percent_true(50)) return Fortuna::zero_cool(mid_point);
        else return 1 + Fortuna::max_cool(mid_point) + mid_point;
    } else return Fortuna::analytic_continuation(Fortuna::mostly_not_middle, num);
}

int mostly_not_center(int num) {
    if (num > 0) {
        const int mid_point = num / 2;
        if (num % 2 == 0) return Fortuna::plus_or_minus_curve_down(mid_point) + mid_point;
        else if (percent_true(50)) return Fortuna::zero_extreme(mid_point);
        else return 1 + Fortuna::max_extreme(mid_point) + mid_point;
    } else return Fortuna::analytic_continuation(Fortuna::mostly_center, num);
}

} // end namespace Fortuna
