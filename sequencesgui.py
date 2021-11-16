from sequences import Sequences
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import mplcursors
import sys

class GraphGui(Sequences):
    def make_graph(self, sequence: list) -> plt.plot:
        plt.style.use('seaborn-darkgrid')
        
        xticks = [num for num in range(0, len(sequence) + 1, 5)]
        
        root = tk.Tk()
        root.wm_title('Sequences Plot')
        
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.set_facecolor('#828282')
        
        
        ax = fig.add_subplot(111)
        ax.tick_params(colors = 'white')
        ax.set_xticks(xticks)
        ax.set_xlabel('Cycle', color = 'white')
        ax.set_ylabel('Value', color = 'white')
        ax.format_coord = lambda x, y: f'Cycle: {x:.0f}, Value: {y:.0f}'
        marker = ax.plot(sequence, color = 'black', marker = 'o', markerfacecolor = 'silver')
        
        canvas = FigureCanvasTkAgg(fig, master=root)
        mplcursors.cursor(marker)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        tk.mainloop()


if __name__ == '__main__':
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
        print('Usage: python sequencesgui.py <sequence> <value>')
        print('for sequence choices type: python sequencesgui.py -h')
    
    elif len(sys.argv) == 3:
        val_choice = int(sys.argv[2])
        seq_choice = sys.argv[1]
        bailey.make_graph(x[seq_choice](val_choice))
