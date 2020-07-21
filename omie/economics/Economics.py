import tkinter as tk
from add_project import AddProject

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
        # Window Size
        self.geometry("425x350")  # width x height

        # Set dummy frame to destroy and create/pack main menu frame
        self.current_frame = tk.Frame()
        self.main_menu()

    def main_menu(self):
        self.current_frame.destroy()
        # Remove menu bar & add title
        emptymenu = tk.Menu(self)
        self.config(menu = emptymenu)
        self.title("OMIE - Economics")
        # Create main menu frame
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

        ## Menu Bar
        project.menubar = tk.Menu(project.master)
        project.master.config(menu=project.menubar)
        # File Menu - Return to Main Menu
        project.fileMenu = tk.Menu(project.menubar)
        project.fileMenu.add_command(label="Return to Main Menu", command=self.main_menu)
        project.menubar.add_cascade(label="File", menu=project.fileMenu)
        # Edit Menu - Default Params
        project.editMenu = tk.Menu(project.menubar)
        project.editMenu.add_command(label="Default Params", command=project.restore_defaults)
        project.menubar.add_cascade(label="Edit", menu=project.editMenu)

        ## Next Button, Pack Frame, & Set Current Frame
        self.next_button = tk.Button(project, text = "Next", 
            command=self.param_detail, bg = "green")
        self.next_button.grid(row = 0, column = 2, padx = 5)
        project.pack(fill = "both", expand=True)
        self.current_frame = project

    def param_detail(self):
        """param detail frame"""
        pass

if __name__ == "__main__":
    main()