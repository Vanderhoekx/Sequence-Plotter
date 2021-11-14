from functools import lru_cache

class Helpers:
    @lru_cache(maxsize = 1000)
    def _fib_calc(self, n: int) -> int:
        if n <= 2: return 1
        else:
            return self._fib_calc(n - 2) + self._fib_calc(n - 1)

    def _factorial(self, n: int) -> int:
            total = 1
            for i in range(1, n + 1):
                total *= i
            return total