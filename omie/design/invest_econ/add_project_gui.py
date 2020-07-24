import tkinter as tk

class AddProjectGUI(tk.Frame):
    def __init__(self):
        # Initialize Tk() class
        super().__init__()

        ## Default Parameters
        self.ini_name = "Project1"
        self.ini_num_invest, self.ini_num_flows = 1, 5
        self.ini_rand_data = True
        self.ini_mult, self.ini_inflation, self.ini_taxes, self.ini_uncertainty = \
            False, False, False, False
        self.ini_depreciation, self.ini_distribution, self.ini_estimate = \
            "None", "Triangular", "Mean"

        ## Window Title
        self.master.title("Add Project")

        ## Entry widgets & their labels
        self.name_label, self.name = \
            tk.Label(self, text="Project Name"), tk.Entry(self)
        self.num_invest_label, self.num_invest = \
            tk.Label(self, text = "Number of Investments"), tk.Entry(self)
        self.num_flows_label, self.num_flows = \
            tk.Label(self, text = "Number of Cash Flows"), tk.Entry(self)

        ## Checkboxes & their labels
        self.rand_data = tk.BooleanVar()
        self.mult = tk.BooleanVar()
        self.inflation = tk.BooleanVar()
        self.taxes = tk.BooleanVar()
        self.uncertainty = tk.BooleanVar()

        self.rand_data_button = tk.Checkbutton(self,
            text="Random Data", variable=self.rand_data)
        self.mult_button = tk.Checkbutton(self,
            text="Multiple Compounds", variable=self.mult)
        self.inflation_button = tk.Checkbutton(self,
            text="Include Inflation", variable=self.inflation)
        self.taxes_button = tk.Checkbutton(self,
            text="Include Taxes", variable=self.taxes)
        self.uncertainty_button = tk.Checkbutton(self,
            text="Include Uncertainty", variable=self.uncertainty)

        ## Radio Buttons & their labels
        # Depreciation
        self.depreciation = tk.StringVar()
        self.depreciation_options = [
            ("None", "None"),
            ("MACRS(GDS)", "MACRS(GDS)"),
            ("Straight Line", "Straight Line"),
            ("SYD", "SYD"),
            ("DRDB", "DRDB")
        ]
        row_index = 8
        for text, option in self.depreciation_options:
            b = tk.Radiobutton(self, text=text,
                variable=self.depreciation, value=option)
            b.grid(row = row_index, column = 0, sticky = tk.W)
            row_index += 1
        self.depreciation_label = tk.Label(self, text = "Depreciation")

        # Distribution
        self.distribution = tk.StringVar()
        self.distribution_options = [
            ("Uniform", "Uniform"),
            ("Triangular", "Triangular"),
            ("Beta", "Beta"),
            ("Normal", "Normal"),
            ("General", "General")
        ]
        row_index = 8
        for text, option in self.distribution_options:
            b = tk.Radiobutton(self, text=text,
                variable=self.distribution, value=option)
            b.grid(row = row_index, column = 1, sticky = tk.W)
            row_index += 1
        self.distribution_label = tk.Label(self, text = "Distribution")

        # Estimate Function
        self.estimate = tk.StringVar()
        self.estimate_options = [
            ("Mean", "Mean"),
            ("Quantile", "Quantile"),
            ("Simulate", "Simulate")
        ]
        row_index = 8
        for text, option in self.estimate_options:
            b = tk.Radiobutton(self, text=text,
                variable=self.estimate, value=option)
            b.grid(row = row_index, column = 2, sticky = tk.W)
            row_index += 1
        self.estimate_label = tk.Label(self, text = "Estimate")

        ## Place Widgets in Grids (Except Radio Buttons: Row 7 through 11)
        # Entries
        self.name_label.grid(row = 0, column = 0, sticky = tk.E)
        self.name.grid(row = 0, column = 1)
        self.num_invest_label.grid(row = 1, column = 0, sticky = tk.E)
        self.num_invest.grid(row = 1, column = 1)
        self.num_flows_label.grid(row = 2, column = 0, sticky = tk.E)
        self.num_flows.grid(row = 2, column = 1)

        # Checkboxes
        self.rand_data_button.grid(row = 3, column = 0, sticky = tk.W)
        self.mult_button.grid(row = 4, column = 0, sticky = tk.W)
        self.inflation_button.grid(row = 5, column = 0, sticky = tk.W)
        self.taxes_button.grid(row = 6, column = 0, sticky = tk.W)
        self.uncertainty_button.grid(row = 6, column = 1, sticky = tk.W)

        # Radio Button Labels
        self.depreciation_label.grid(row = 7, column = 0, sticky = tk.W, pady=(3,0))
        self.distribution_label.grid(row = 7, column = 1, sticky = tk.W, pady=(3,0))
        self.estimate_label.grid(row = 7, column = 2, sticky = tk.W, pady=(3,0))

        ## Fill widgets with their default values
        self.restore_defaults()

    def restore_defaults(self):
        """Restore parameters to their default values"""
        # Entry Widgets
        self.name.delete(0, tk.END)
        self.num_invest.delete(0, tk.END)
        self.num_flows.delete(0, tk.END)

        self.name.insert(0, self.ini_name)
        self.num_invest.insert(0, self.ini_num_invest)
        self.num_flows.insert(0, self.ini_num_flows)

        # Checkboxes
        self.rand_data.set(self.ini_rand_data)
        self.mult.set(self.ini_mult)
        self.inflation.set(self.ini_inflation)
        self.taxes.set(self.ini_taxes)
        self.uncertainty.set(self.ini_uncertainty)

        # Radio Buttons
        self.depreciation.set(self.ini_depreciation)
        self.distribution.set(self.ini_distribution)
        self.estimate.set(self.ini_estimate)


if __name__ == "__main__":
    project_frame = AddProject()
    project_frame.pack(fill="both", expand=True)
    project_frame.mainloop()