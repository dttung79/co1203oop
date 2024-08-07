import csv
from tkinter import *
from tkinter import filedialog
from w9_base_gui import BaseGUI
from w9_item import Item

class StoreGUI(BaseGUI):
    def __init__(self):
        super().__init__("Sport Store", "450x350")
    
    # override the abstract method from BaseGUI
    def _create_widgets(self):
        self._create_listbox()
        self._create_entries()
        self._create_buttons()
    
    def _create_listbox(self):
        lbl_items = Label(self.window, text="Items List")
        lbl_items.grid(row=0, column=0, columnspan=2, sticky=W, padx=5, pady=5)

        self.listbox = Listbox(self.window, width=20, height=10, selectmode=SINGLE, exportselection=False)
        self.listbox.grid(row=1, column=0, columnspan=2, rowspan=5, sticky=W, padx=5, pady=5)
        self.listbox.bind("<<ListboxSelect>>", self._item_selected)
    
    def _item_selected(self, event):
        pass
    
    def _create_entries(self):
        lbl_item_details = Label(self.window, text="Item Details")
        lbl_item_details.grid(row=0, column=2, columnspan=3, sticky=W, padx=5, pady=5)

        lbl_id = Label(self.window, text="ID")
        lbl_id.grid(row=1, column=2, sticky=E, padx=5, pady=5)
        
        self.txt_id = Entry(self.window, width=20)
        self.txt_id.grid(row=1, column=3, columnspan=3, sticky=W, padx=5, pady=5)

        lbl_name = Label(self.window, text="Name")
        lbl_name.grid(row=2, column=2, sticky=E, padx=5, pady=5)

        self.txt_name = Entry(self.window, width=20)
        self.txt_name.grid(row=2, column=3, columnspan=3, sticky=W, padx=5, pady=5)

        lbl_brand = Label(self.window, text="Brand")
        lbl_brand.grid(row=3, column=2, sticky=E, padx=5, pady=5)

        self.txt_brand = Entry(self.window, width=20)
        self.txt_brand.grid(row=3, column=3, columnspan=3, sticky=W, padx=5, pady=5)

        lbl_price = Label(self.window, text="Price")
        lbl_price.grid(row=4, column=2, sticky=E, padx=5, pady=5)

        self.txt_price = Entry(self.window, width=20)
        self.txt_price.grid(row=4, column=3, columnspan=3, sticky=W, padx=5, pady=5)

    def _create_buttons(self):
        btn_load = Button(self.window, text="Load", command=self._load_items)
        btn_load.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        btn_save = Button(self.window, text="Save", command=None)
        btn_save.grid(row=6, column=1, sticky=E, padx=5, pady=5)

        btn_new = Button(self.window, text="New", command=None)
        btn_new.grid(row=5, column=3, sticky=W, padx=2, pady=5)

        btn_edit = Button(self.window, text="Edit", command=None)
        btn_edit.grid(row=5, column=4, sticky=W, padx=2, pady=5)

        btn_delete = Button(self.window, text="Del", command=None)
        btn_delete.grid(row=5, column=5, sticky=W, padx=2, pady=5)

        btn_exit = Button(self.window, text="Exit", width=18, command=self.window.quit)
        btn_exit.grid(row=6, column=3, columnspan=3, sticky=W, padx=5, pady=5)

    def _load_items(self):
        # clear listbox
        self.listbox.delete(0, END)
        self.items = []
        # load items from csv file
        csv_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                id, name, brand, price = row
                item = Item(id, name, brand, price)
                self.items.append(item)
                self.listbox.insert(END, name)

if __name__ == "__main__":
    store_gui = StoreGUI()
    store_gui.run()
