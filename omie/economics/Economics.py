import tkinter as tk
from add_project import AddProject
from param_detail import ParamDetail

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
        self.geometry("1100x700")  # width x height

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
        project = AddProject()
        self.current_frame.destroy()

        ## Menu Bar
        # File Menu - Return to Main Menu
        self.basic_menu_bar(project)
        # Edit Menu - Default Params
        project.editMenu = tk.Menu(project.menubar)
        project.editMenu.add_command(label="Default Params", command=project.restore_defaults)
        project.menubar.add_cascade(label="Edit", menu=project.editMenu)

        ## Next Button, Pack Frame, & Set Current Frame
        self.next_button = tk.Button(project, text = "Next",
            command=lambda proj=project: self.param_detail(proj), bg = "#00bd21", fg = "#f5fcf6")
        self.next_button.grid(row = 0, column = 2, padx = 5)
        project.pack(fill = "both", expand=True)
        self.current_frame = project

    def param_detail(self, proj):
        """param detail frame"""
        details = ParamDetail(proj)
        self.current_frame.destroy()

        ## Menu Bar
        self.basic_menu_bar(details)

        ## Compute Rates Button, Pack Frame, & Set Current Frame
        details.pack(fill = "both", expand=True)
        self.current_frame = details

    def basic_menu_bar(self, frame):
        """Create basic menu bar for frame, including File -> Return To Main Menu"""
        ## Menu Bar
        frame.menubar = tk.Menu(frame.master)
        frame.master.config(menu=frame.menubar)
        # File Menu - Return to Main Menu
        frame.fileMenu = tk.Menu(frame.menubar)
        frame.fileMenu.add_command(label="Return to Main Menu", command=self.main_menu)
        frame.menubar.add_cascade(label="File", menu=frame.fileMenu)


if __name__ == "__main__":
    main()