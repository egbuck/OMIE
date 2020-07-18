import tkinter as tk
import tkinter.messagebox as msg

class AddProject(tk.Tk):
    def __init__(self):
        # Initialize Tk() class
        super().__init__()

        # Title & Size of Window
        self.title("Project Dialog")
        self.geometry("350x250")  # width x height

        # Default Parameters
        self.ini_name = "Project1"
        self.ini_num_invest, self.ini_num_flows = 0, 5
        self.ini_rand_data = True
        self.ini_mult, self.ini_inflation, self.ini_taxes, self.ini_uncertainty = \
            False, False, False, False
        self.ini_depreciation, self.ini_distribution, self.ini_estimate = \
            "None", "Triangular", "Mean"

        # Entry widgets & their labels
        self.name_label, self.name = \
            tk.Label(self, text="Name"), tk.Entry(self)
        self.num_invest_label, self.num_invest = \
            tk.Label(self, text = "Number of Investments"), tk.Entry(self)
        self.num_flows_label, self.num_flows = \
            tk.Label(self, text = "Number of Cash Flows"), tk.Entry(self)

        self.name_label.grid(row=0,column=0)
        self.name.grid(row=0,column=1)
        self.num_invest_label.grid(row=1,column=0)
        self.num_invest.grid(row=1,column=1)
        self.num_flows_label.grid(row=2,column=0)
        self.num_flows.grid(row=2,column=1)

        # Checkboxes & their labels
        self.rand_data = tk.IntVar()
        self.rand_data_button = tk.Checkbutton(self,
            text="Random Data", variable=self.rand_data)

        self.mult = tk.IntVar()
        self.mult_button = tk.Checkbutton(self,
            text="Multiple Compounds", variable=self.rand_data)

        self.inflation = tk.IntVar()
        self.inflation_button = tk.Checkbutton(self,
            text="Include Inflation", variable=self.rand_data)

        self.taxes = tk.IntVar()
        self.taxes_button = tk.Checkbutton(self,
            text="Include Taxes", variable=self.rand_data)

        self.uncertainty = tk.IntVar()
        self.uncertainty_button = tk.Checkbutton(self,
            text="Include Uncertainty", variable=self.rand_data)

        # Single Choices & their labels
        self.depreciation = tk.StringVar()
        self.depreciation.set(self.ini_depreciation)
        self.depreciation_options = [
            ("None", "None"),
            ("MACRS(GDS)", "MACRS(GDS)"),
            ("Straight Line", "Straight Line"),
            ("SYD", "SYD"),
            ("DRDB", "DRDB")
        ]
        row_index = 4
        for text, option in self.depreciation_options:
            b = tk.Radiobutton(self, text=text,
                variable=self.depreciation, value=option)
            b.grid(row = row_index, column = 0, sticky = tk.W, padx = 5, pady = 5)
            row_index += 1
        self.depreciation_label = tk.Label(self, text = "Depreciation")
        self.depreciation_label.grid(row=3, column = 0)

        self.distribution = tk.StringVar()
        self.distribution.set(self.ini_distribution)
        self.distribution_options = [
            ("Uniform", "Uniform"),
            ("Triangular", "Triangular"),
            ("Beta", "Beta"),
            ("Normal", "Normal"),
            ("General", "General")
        ]
        row_index = 4
        for text, option in self.distribution_options:
            b = tk.Radiobutton(self, text=text,
                variable=self.distribution, value=option)
            b.grid(row = row_index, column = 1, sticky = tk.W, padx = 5, pady = 5)
            row_index += 1
        self.distribution_label = tk.Label(self, text = "Distribution")
        self.distribution_label.grid(row=3, column = 1)

        self.estimate = tk.StringVar()
        self.estimate.set(self.ini_estimate)
        self.estimate_options = [
            ("Mean", "Mean"),
            ("Quantile", "Quantile"),
            ("Simulate", "Simulate")
        ]
        row_index = 4
        for text, option in self.estimate_options:
            b = tk.Radiobutton(self, text=text,
                variable=self.estimate, value=option)
            b.grid(row = row_index, column = 2, sticky = tk.W, padx = 5, pady = 5)
            row_index += 1
        self.estimate_label = tk.Label(self, text = "Estimate")
        self.estimate_label.grid(row=3, column = 2)

        # Buttons - Ok, Cancel, Default
        self.ok_button = tk.Button(self, text = "OK")
        self.quit_button = tk.Button(self, text = "Quit")
        self.default_button = tk.Button(self, text = "Default")
        self.ok_button.grid(row=0, column = 2)
        self.quit_button.grid(row=1, column = 2)
        self.default_button.grid(row=2, column = 2)


if __name__ == "__main__":
    project = AddProject()
    project.mainloop()