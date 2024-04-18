import customtkinter as ctk
import scrollbar
import database


class App(ctk.CTk):
    width = 400
    height = 400

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("ToDoList")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.item_list = database.load_Tasks()
        self.scroll = scrollbar.ScrollBar(master=self,width=300 ,height=300,  item_list=self.item_list)
        self.scroll.pack(pady=10)
        button = ctk.CTkButton(master=self,width=300 , text="Add Task" , command=self.open_add_task)
        button.pack(pady=10)

        self.add_task_frame = ctk.CTkFrame(master=self,width=300 ,height=300, bg_color= ("gray70", "gray30")) 
        self.task_text = ctk.CTkEntry(master=self.add_task_frame, placeholder_text="Write Your Task")
        self.task_text.pack(pady=20, padx=20)
        close_button = ctk.CTkButton(master=self.add_task_frame, text="Close", command=self.Close_add_frame)
        close_button.pack(pady=20, padx=20)
        add_task_button = ctk.CTkButton(master=self.add_task_frame, text="Add Task", command=self.add_to_list)
        add_task_button.pack(pady=20, padx=20)

    def open_add_task(self):
        self.add_task_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.add_task_frame.lift()
    def add_to_list(self):
        task = self.task_text.get()
        self.scroll.add_item((task,))
        database.add_Task(task)
        self.Close_add_frame()
    def Close_add_frame(self):
        self.task_text.delete(0, ctk.END)
        self.add_task_frame.place_forget()






if __name__ == "__main__":
    app = App()
    app.mainloop()

