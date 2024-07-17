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

        self.txt_book = Entry(self.window, width=25)
        self.txt_book.grid(row=0, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        lbl_price = Label(self.window, text="Price :")
        lbl_price.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        self.txt_price = Entry(self.window, width=25)
        self.txt_price.grid(row=1, column=1, padx=5, pady=5, sticky=W, columnspan=2)

        lbl_quantity = Label(self.window, text="Quantity :")
        lbl_quantity.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.txt_quantity = Entry(self.window, width=25)
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
        lbl_delivery = Label(self.window, text="Delivery :")
        lbl_delivery.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.delivery_var = IntVar()
        self.rd_normal = Radiobutton(self.window, text="Normal (Free)", variable=self.delivery_var, value=0)
        self.rd_normal.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        self.rd_express = Radiobutton(self.window, text="Express ($2)", variable=self.delivery_var, value=2)
        self.rd_express.grid(row=5, column=1, padx=5, pady=5, sticky=W)

        self.rd_immediate = Radiobutton(self.window, text="Immediate ($5)", variable=self.delivery_var, value=5)
        self.rd_immediate.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    def __btn_payment_clicked(self):
        try:
            price = float(self.txt_price.get())
            quantity = int(self.txt_quantity.get())
            total_price = price * quantity

            if self.cover_var.get() == True:
                total_price += 1
            
            if self.card_var.get():
                total_price += 1.5
            
            total_price += self.delivery_var.get()

            msb.showinfo("Payment", f"Total Price: ${total_price}")
        except ValueError:
            msb.showerror("Error", "Please enter valid price and quantity")

    # Only run method needs to be public
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BookStoreGUI()
    app.run()