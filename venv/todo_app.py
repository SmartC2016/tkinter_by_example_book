import tkinter as tk


class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

    self.title("To-Do App v1")

    self.geometry("300x400")









if __name__ == "__main__":
    root = Root()
    root.mainloop()
