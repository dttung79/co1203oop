from tkinter import *
from tkinter import messagebox as msb

class BookStoreGUI:
    def __init__(self):
        self.window = self.__create_window()
        self.__create_widgets()

    def __create_window(self):
        window = Tk()
        window.title("Book Store")
        window.geometry("400x400")
        return window
    
    def __create_widgets(self):
        self.__create_text_entries()
        self.__create_checkboxes()
        self.__create_radio_buttons()
        btn_payment = Button(self.window, text="Payment", command=self.__btn_payment_clicked)
        btn_payment.grid(row=7, column=1, columnspan=2, padx=5, pady=5, sticky=W)
    
    def __create_text_entries(self):
        lbl_book = Label(self.window, text="Book :")
        lbl_book.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.txt_book = Entry(self.window, width=20)
        self.txt_book.grid(row=0, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        lbl_price = Label(self.window, text="Price :")
        lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.txt_price = Entry(self.window, width=20)
        self.txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        lbl_quantity = Label(self.window, text="Quantity :")
        lbl_quantity.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.txt_quantity = Entry(self.window, width=20)
        self.txt_quantity.grid(row=2, column=1, padx=5, pady=5, sticky=W, columnspan=2)
    
    def __create_checkboxes(self):
        lbl_extra = Label(self.window, text="Extra :")
        lbl_extra.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.cover_var = BooleanVar()
        self.cb_cover = Checkbutton(self.window, text="Cover ($1)", variable=self.cover_var)
        self.cb_cover.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.card_var = BooleanVar()
        self.cb_card = Checkbutton(self.window, text="Card ($1.5)", variable=self.card_var)
        self.cb_card.grid(row=3, column=2, padx=5, pady=5, sticky=W)
    
    def __create_radio_buttons(self):
        pass

    def __btn_payment_clicked(self):
        pass

    # Only run method needs to be public
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BookStoreGUI()
    app.run()