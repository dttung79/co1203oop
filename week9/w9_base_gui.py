from tkinter import *
from abc import ABC, abstractmethod

class BaseGUI(ABC):
    def __init__(self, title, dimension):
        self.window = self._create_window(title, dimension) # protected method (1 _ before method name)
        self._create_widgets()
    
    def _create_window(self, title, dimension):
        window = Tk()
        window.geometry(dimension)
        window.title(title)
        return window

    @abstractmethod
    def _create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()