import queueprog
import helpers

class Sequences(queueprog.Queue, helpers.Helpers):
    def collatz(self, n: int) -> list:
        '''The Collatz Sequence - A sequence where any number entered will eventually end at 1'''
        self.coll_items = [n]
        while n > 1:
            if n % 2 == 0:
                n //= 2
                self.enqueue(n, self.coll_items)
            else:
                n = 3 * n + 1
                self.enqueue(n, self.coll_items)
        return self.coll_items
    
    def recaman(self, n: int) -> list:
        self.rec_items = [0]
        if n == 0:
            return n
        else:
            for num in range(1, n + 1):
                if (self.rec_items[num - 1]) - num > 0 and (self.rec_items[num - 1]) - num not in self.rec_items:
                    self.enqueue((self.rec_items[num - 1]) - num, self.rec_items)
                else:
                    self.enqueue((self.rec_items[num - 1]) + num, self.rec_items)
        return self.rec_items

    def fib(self, n: int) -> list:
        return [self._fib_calc(num) for num in range(1, n + 1)]
    
    def square_nums(self, n: int) -> list:
        return [num ** 2 for num in range(n + 1)]
    
    def tri_nums(self, n: int) -> list:
        return [num * (num + 1) // 2 for num in range(n + 1)]
        

    def penta_nums(self, n: int) -> list:
        self.penta_items = []
        initial_difference = 4
        for num in range(n + 1):
            if num < 2:
                self.enqueue(num, self.penta_items)
            else:
                self.enqueue(self.penta_items[-1] + initial_difference, self.penta_items)
                initial_difference += 3
        return self.penta_items

    def lazy_caterer(self, n: int) -> list:
        '''it describes the maximum number of pieces of a circle that can be made with a given number of straight cuts'''
        return [(num ** 2 + num + 2) // 2 for num in range(1, n + 1)]

    def magic_squares(self, n: int) -> list:
        return [num * (num ** 2 + 1) // 2 for num in range(n + 1)]

    def catalan(self, n: int) -> list:
        return [1 * self._factorial(num * 2) // ((num + 1) * (self._factorial(num) * self._factorial(num))) for num in range(1, n + 1)]

    def primes(self, n: int) -> list:
        for i in range(2, n + 1):
            for num in range(2, i):
                if i % num == 0:
                    break
            else:
                self.enqueue(i, self.prime_items)
        return self.prime_items
