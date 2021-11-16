from sequencesgui import GraphGui
import sys

bailey = GraphGui()

sequence_dict = {'collatz': bailey.collatz, 'recaman': bailey.recaman, 'fibonacci': bailey.fib,
        'square nums': bailey.square_nums, 'tri nums': bailey.tri_nums,
        'penta nums': bailey.penta_nums, 'lazy caterer': bailey.lazy_caterer,
        'magic squares': bailey.magic_squares, 'catalan': bailey.catalan,
        'primes': bailey.primes}

if len(sys.argv) == 2 and sys.argv[1] == '-h':
    for key, value in sequence_dict.items():
        print(key)

elif len(sys.argv) != 3:
    print('Usage: python comm_line.py <sequence> <value>')
    print('for sequence choices type: python comm_line.py -h')

elif len(sys.argv) == 3:
    val_choice = int(sys.argv[2])
    seq_choice = sys.argv[1]
    bailey.make_graph(sequence_dict[seq_choice](val_choice))


