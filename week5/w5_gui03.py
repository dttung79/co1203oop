from tkinter import *

class AppleStore:
    def __init__(self):
        self.window = self.__create_window()
        self.__create_widgets()
    
    def __create_window(self):
        window = Tk()
        window.geometry("300x250")
        window.title("Apple Store")
        return window
    
    def __create_widgets(self):
        lbl_store = Label(self.window, text="Apple Store")
        lbl_store.grid(row=0, column=0)

        lbl_select_macbook = Label(self.window, text="Select MacBook")
        lbl_select_macbook.grid(row=1, column=0)

        self.__create_radiobuttons()

        lbl_select_options = Label(self.window, text="Select Options")
        lbl_select_options.grid(row=5, column=0)

        self.__create_checkbuttons()

        self.lbl_price = Label(self.window, text="Total Price: $0")
        self.lbl_price.grid(row=8, column=0)
    
    def __create_checkbuttons(self):
        self.cover_var = BooleanVar()
        self.chk_cover = Checkbutton(self.window, text="Cover ($10)", variable=self.cover_var, 
                                        command=self.calculate_price)
        self.chk_cover.grid(row=6, column=0)

        self.case_var = BooleanVar()
        self.chk_case = Checkbutton(self.window, text="Case ($20)", variable=self.case_var, 
                                        command=self.calculate_price)
        self.chk_case.grid(row=7, column=0)

    def __create_radiobuttons(self):
        self.price_var = IntVar() # variable to bind to all radiobuttons
        
        self.rd_air13 = Radiobutton(self.window, text="Macbook Air 13 ($1500)", 
                                    variable=self.price_var, value=1500, command=self.calculate_price)
        self.rd_air13.grid(row=2, column=0)

        self.rd_pro13 = Radiobutton(self.window, text="Macbook Pro 13 ($2000)", 
                                    variable=self.price_var, value=2000, command=self.calculate_price)
        self.rd_pro13.grid(row=3, column=0)

        self.rd_pro16 = Radiobutton(self.window, text="Macbook Pro 16 ($2500)",
                                    variable=self.price_var, value=2500, command=self.calculate_price)
        self.rd_pro16.grid(row=4, column=0)

    def calculate_price(self):
        price = self.price_var.get()        # get price of selected MacBook
        if self.cover_var.get():            # check if cover is selected
            price += 10
        if self.case_var.get():             # check if case is selected
            price += 20
        # update label with price
        self.lbl_price.configure(text="Total Price: $" + str(price))
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    store = AppleStore()
    store.run()