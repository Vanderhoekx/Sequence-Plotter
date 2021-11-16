from sequencesgui import GraphGui
import sys

bailey = GraphGui()

x = {'collatz': bailey.collatz, 'recaman': bailey.recaman, 'fib': bailey.fib,
        'square_nums': bailey.square_nums, 'tri_nums': bailey.tri_nums,
        'penta_nums': bailey.penta_nums, 'lazy_caterer': bailey.lazy_caterer,
        'magic_squares': bailey.magic_squares, 'catalan': bailey.catalan,
        'primes': bailey.primes}

if len(sys.argv) == 2 and sys.argv[1] == '-h':
    for key, value in x.items():
        print(key)

elif len(sys.argv) != 3:
    print('Usage: python comm_line.py <sequence> <value>')
    print('for sequence choices type: python comm_line.py -h')

elif len(sys.argv) == 3:
    val_choice = int(sys.argv[2])
    seq_choice = sys.argv[1]
    bailey.make_graph(x[seq_choice](val_choice))


