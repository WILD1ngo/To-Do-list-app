import customtkinter as ctk
import database


class ScrollBar(ctk.CTkScrollableFrame):
    def __init__(self, master , item_list , **kwargs):
        super().__init__(master , **kwargs)
        self.item_list = item_list
        self.items_list = []
        if item_list:
            for item in self.item_list:
                self.add_item(item)
    
    def add_item(self, item):
        item_frame = Item(self, item)
        item_frame.grid(row=len(self.items_list), column=0 ,pady=(0, 10), sticky="ew")
        self.items_list.append(item_frame)

    def delete_item(self , item):
        try:
            self.items_list.remove(item)
            item.destroy()
        except:
            print("item not found in list")




class Item(ctk.CTkFrame):
    def __init__(self, master , text):
        super().__init__(master)
        self.width = 250
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.text = text
        self.master = master
        main_text = ctk.CTkLabel(self, text=self.text ,width=200, wraplength=200)
        main_text.grid(row=0, column=0, sticky="W" ,padx=20)
        delete_button = ctk.CTkButton(self, text="X", command=self.delete ,width= 25)
        delete_button.grid(row=0, column=1, sticky="N")
        complete_button = ctk.CTkButton(self, text="✓", command=self.complete ,width= 25)
        complete_button.grid(row=0, column=2, sticky="N")

    def delete(self):
        database.remove_Task(self.text)
        self.master.delete_item(self)

    def complete(self):
        self.master.delete_item(self)
