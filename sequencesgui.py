from sequences import Sequences
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import mplcursors

class GraphGui(Sequences):
    def __init__(self, curr_seq = 'Collatz'):
        self.curr_seq = curr_seq
        #self.make_graph(self.collatz(15))
        self.sequence_window = tk.Tk()

    def make_graph(self, sequence: list) -> plt.plot:
        plt.style.use('seaborn-darkgrid')
        
        xticks = [num for num in range(1, len(sequence) + 1, 2)]
        self.root = tk.Tk()
        self.sequence_window = tk.Tk()
        
        self.sequence_window.wm_title('Sequence/Value Picker')
        self.sequence_window.geometry('200x150')

        self.root.wm_title('Sequences Plot')
        self.root.geometry('1000x500')
        
        seq_var = tk.StringVar(self.sequence_window)
        self.ent_var = tk.IntVar(self.sequence_window)
        
        buttons_frame = tk.Frame(self.sequence_window, bg = '#828282', padx = 10)
        
        sequence_lst = ['Collatz', 'Recaman', 'Fibonacci', 'Square Nums', 'Tri Nums',
                        'Penta Nums', 'Lazy Caterer', 'Magic Squares', 'Catalan', 'Primes']
        seq_var.set(sequence_lst[0])

        seq_menu = tk.OptionMenu(buttons_frame, seq_var, *sequence_lst, command = self.seq_menu_select)
        seq_menu.pack(side = tk.TOP, fill = tk.BOTH, pady = 20)
        
        self.value_ent = tk.Entry(buttons_frame, textvariable = self.ent_var)
        self.value_ent.pack(side = tk.TOP, pady = 20)
        
        buttons_frame.pack(fill = tk.BOTH, expand = 1)
        
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.set_facecolor('#828282')
        
        ax = fig.add_subplot(111)
        ax.tick_params(colors = 'white')
        ax.set_xticks(xticks)
        ax.set_xlabel('Cycle', color = 'white')
        ax.set_ylabel('Value', color = 'white')
        ax.format_coord = lambda x, y: f'Cycle: {x + 1:.0f}, Value: {y:.0f}'
        marker = ax.plot(sequence, color = 'black', marker = 'o', markerfacecolor = 'silver')
        
        canvas = FigureCanvasTkAgg(fig, master = self.root)
        mplcursors.cursor(marker)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, self.root)
        toolbar.update()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH)
        
        tk.mainloop()

    def get_value(self):
        return self.ent_var.get()
        
    
    def seq_menu_select(self, event):
        sequence_dict = {'Collatz': self.collatz, 'Recaman': self.recaman, 'Fibonacci': self.fib,
        'Square Nums': self.square_nums, 'Tri Nums': self.tri_nums,
        'Penta Nums': self.penta_nums, 'Lazy Caterer': self.lazy_caterer,
        'Magic Squares': self.magic_squares, 'Catalan': self.catalan,
        'Primes': self.primes}
        
        
        self.sequence_window.destroy()
        self.curr_seq = sequence_dict[event]
        self.make_graph(self.curr_seq(self.get_value()))
        

if __name__ == '__main__':
    bailey = GraphGui()
    bailey.make_graph(bailey.collatz(15))