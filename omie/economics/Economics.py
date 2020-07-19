import tkinter as tk
from cash_flow import AddProject

def return_to_main_menu(window):
    """Return to the Main Menu GUI"""
    window.destroy()
    main()

def main():
    main_menu = Economics()
    main_menu.mainloop()

class Economics(tk.Tk):

    def __init__(self):
        super().__init__()
        # Window Name
        self.title("OMIE - Economics")

        # Set dummy frame to destroy and create/pack main menu frame
        self.current_frame = tk.Frame()
        self.main_menu()

    def main_menu(self):
        self.current_frame.destroy()
        main_menu_frame = tk.Frame()
        self.test = tk.Label(main_menu_frame, text="Hello World!")
        self.test.pack()
        self.addproj = tk.Button(main_menu_frame, text="Add Project", command=self.add_project)
        self.addproj.pack()
        main_menu_frame.pack(fill = "both", expand=True)
        self.current_frame = main_menu_frame

    def add_project(self):
        self.current_frame.destroy()
        project = AddProject()
        self.next_button = tk.Button(project, text = "Next Step", command=self.param_detail)
        self.return_button = tk.Button(project, text = "Return To Main Menu", command = self.main_menu)
        self.next_button.grid(row = 0, column = 2, padx = 5)
        self.return_button.grid(row = 1, column = 2, padx = 5)
        project.pack(fill = "both", expand=True)
        self.current_frame = project

    def param_detail(self):
        """param detail frame"""
        pass

if __name__ == "__main__":
    main()