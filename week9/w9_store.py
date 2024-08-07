import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
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
        selected_index = self.listbox.curselection()[0]     # get selected index from listbox
        selected_item = self.items[selected_index]          # get selected item from items list
        # update textboxes with selected item details
        self._update_textbox(self.txt_id, selected_item.id)
        self._update_textbox(self.txt_name, selected_item.name)
        self._update_textbox(self.txt_brand, selected_item.brand)
        self._update_textbox(self.txt_price, selected_item.price)
    
    def _update_textbox(self, textbox, value):
        textbox.delete(0, END)
        textbox.insert(0, value)
    
    def _create_entries(self):
        lbl_item_details = Label(self.window, text="Item Details")
        lbl_item_details.grid(row=0, column=2, columnspan=3, sticky=W, padx=5, pady=5)

        lbl_id = Label(self.window, text="ID")
        lbl_id.grid(row=1, column=2, sticky=E, padx=5, pady=5)
        
        self.txt_id = Entry(self.window, width=20)
        self.txt_id.grid(row=1, column=3, columnspan=3, sticky=W, padx=5, pady=5)
        self.txt_id.bind("<Return>", self._txt_id_entered) 

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

    def _txt_id_entered(self, event):
        id = self.txt_id.get()
        for index, item in enumerate(self.items):
            if item.id == id:
                self.listbox.selection_clear(0, END)    # clear current selection
                self.listbox.selection_set(index)       # set new selection
                self.listbox.see(index)                  # scroll to new selection
                self.listbox.activate(index)             # activate new selection
                self._item_selected(None)                # update textboxes with new selection
                messagebox.showinfo("Item Found", f"{item.name} has been found.")
                return
        
        messagebox.showwarning("Item Not Found", "Item with the given ID is not found.")

    def _create_buttons(self):
        btn_load = Button(self.window, text="Load", command=self._load_items)
        btn_load.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        btn_save = Button(self.window, text="Save", command=self._save_items)
        btn_save.grid(row=6, column=1, sticky=E, padx=5, pady=5)

        btn_new = Button(self.window, text="New", command=self._new_item)
        btn_new.grid(row=5, column=3, sticky=W, padx=2, pady=5)

        btn_edit = Button(self.window, text="Edit", command=self._edit_item)
        btn_edit.grid(row=5, column=4, sticky=W, padx=2, pady=5)

        btn_delete = Button(self.window, text="Del", command=self._delete_item)
        btn_delete.grid(row=5, column=5, sticky=W, padx=2, pady=5)

        btn_exit = Button(self.window, text="Exit", width=18, command=self.window.quit)
        btn_exit.grid(row=6, column=3, columnspan=3, sticky=W, padx=5, pady=5)
    
    def _save_items(self):
        # save items to csv file
        csv_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        with open(csv_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Item Name", "Brand", "Price"])
            for item in self.items:
                writer.writerow([item.id, item.name, item.brand, item.price])

        messagebox.showinfo("Save Items", "Items have been saved to the file.")

    def _delete_item(self):
        try:
            # get selected index from listbox
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)     # remove item name from listbox
            self.items.pop(selected_index)          # remove item from items list
            messagebox.showinfo("Delete Item", "Item has been deleted.")
        except IndexError:
            messagebox.showerror("Error", "Please select an item to delete.")

    def _edit_item(self):
        try:
            # get selected index from listbox
            selected_index = self.listbox.curselection()[0]
            selected_item = self.items[selected_index]
            # get item details from textboxes
            name = self.txt_name.get()
            brand = self.txt_brand.get()
            price = float(self.txt_price.get())
            # update selected item details
            selected_item.name = name
            selected_item.brand = brand
            selected_item.price = price
            # update listbox with new item name
            self.listbox.delete(selected_index)
            self.listbox.insert(selected_index, name)
            # inform user that item has been updated
            messagebox.showinfo("Edit Item", f"{name} has been updated.")
        except IndexError:
            messagebox.showerror("Error", "Please select an item to edit.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price.")

    def _new_item(self):
        # get item info from textboxes
        id = int(self.txt_id.get())
        name = self.txt_name.get()
        brand = self.txt_brand.get()
        price = float(self.txt_price.get())
        # create new item object and add it to items list
        item = Item(id, name, brand, price)
        self.items.append(item)
        # add item name to listbox
        self.listbox.insert(END, name)
        # inform user that item has been added
        messagebox.showinfo("New Item", f"{name} has been added to the list.")

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
