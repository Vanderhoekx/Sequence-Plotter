from sequences import Sequences
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

class GraphGui(Sequences):
    def make_graph(self, sequence: list) -> plt.plot:
        root = tk.Tk()
        root.wm_title('Sequences Plot')
        
        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot(sequence)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        tk.mainloop()


if __name__ == '__main__':
    bailey = GraphGui()

    print(bailey.make_graph(bailey.penta_nums(15)))