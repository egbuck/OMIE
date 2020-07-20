import tkinter as tk

class ParamDetail(tk.Frame):

    def __init__(self, Proj):
        super().__init__()
        attr_list = ["name", "num_invest", "num_flows", "rand_data", 
            "mult", "inflation", "taxes", "uncertainty", 
            "depreciation", "distribution", "estimate"]
        for attr in attr_list:
            setattr(self, attr, getattr(Proj, attr))
        self.type_choices = ["Single", "Uniform", "Gradient"]

        # Project Name Labels
        self.name_header, self.name_prefix = \
            tk.Label(self, text = "Project Definition", font = "Helvetica 9 bold"), \
            tk.Label(self, text = "Name:")
        self.name_label = tk.Label(self, text = self.name)

        # Periods Params
        self.period_header = tk.Label(self, text = "Periods", font = "Helvetica 9 bold")
        self.life_label, self.life = \
            tk.Label(self, text = "Life (yrs)"), tk.Entry(self)
        self.reps_label, self.reps = \
            tk.Label(self, text = "Repetitions"), tk.Entry(self)
        self.period_length_label, self.period_length = \
            tk.Label(self, text = "Study Period"), tk.Entry(self)

        # Rates Param
        self.rates_header, self.rates_label = \
            tk.Label(self, text = "Rates (%)", font = "Helvetica 9 bold"), \
            tk.Label(self, text = "MARR (/yr)")
        self.rate_percent = tk.Entry(self)

        # Main Table - Title & Headers
        self.table_title = tk.Label(self, 
            text = ("Cash Flow Data - Amounts Negative for "
            "Expenditures and Positive for Revenues"), font = "Helvetica 9 bold")
        self.table_headers = [
            tk.Label(self, text = "Index", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Description", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Amount($)", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Type", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Start", font = "Helvetica 8 bold"),
            tk.Label(self, text = "End", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Parameter", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Factor", font = "Helvetica 8 bold"),
            tk.Label(self, text = "CF. NPW ($)", font = "Helvetica 8 bold")
        ]
        # Type Vars, Type Choices, & Index Labels
        self.types = [tk.StringVar(self) for _ in range(1, self.num_flows + 1)]
        self.indexes = [tk.Label(self, text = str(x)) for x in range(1, self.num_flows + 1)]

        # Entry widgets
        self.description_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.amount_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.start_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.end_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.parameter_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.factor_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.cf_npw_ents = [tk.Entry(self) for _ in range(1, self.num_flows + 1)]
        self.entry_widgets = [self.description_ents, self.amount_ents,
            self.start_ents, self.end_ents, self.parameter_ents,
            self.factor_ents, self.cf_npw_ents]

        # Drop-Down Type Menus
        self.type_menus = [tk.OptionMenu(
            self, self.types[x], *self.type_choices, 
            command = lambda t = self.types[x], 
                e = self.end_ents[x], 
                p = self.parameter_ents[x]: self.check_type(t, e, p)
            ) for x in range(0, self.num_flows)
        ]

        # Place the widgets in grids
        self.place_widgets()

    def check_type(self, distr_type, end_entry, param_entry):
        """
        Check if the distribution type is single or not
        If so, disable the entrys - if not, enable them
        """
        if distr_type == "Single":
            end_entry.configure(state="disabled")
            param_entry.configure(state="disabled")
        else:
            end_entry.configure(state="normal")
            param_entry.configure(state="normal")

    def place_widgets(self):
        """Place the widgets in their grids"""
        # Project Name Labels
        self.name_header.grid(row = 0, column = 0, sticky = tk.W, columnspan = 2)
        self.name_prefix.grid(row = 1, column = 0, sticky = tk.E)
        self.name_label.grid(row = 1, column = 1, sticky = tk.W)

        # Periods Params - row 0 - 3, column 2-3
        self.period_header.grid(row = 0, column = 3)
        self.life_label.grid(row = 1, column = 2, sticky = tk.E) 
        self.life.grid(row = 1, column = 3)
        self.reps_label.grid(row = 2, column = 2, sticky = tk.E)
        self.reps.grid(row = 2, column = 3)
        self.period_length_label.grid(row = 3, column = 2, sticky = tk.E)
        self.period_length.grid(row = 3, column = 3)

        # Rates params
        self.rates_header.grid(row = 0, column = 5)
        self.rates_label.grid(row = 1, column = 4, sticky = tk.E)
        self.rate_percent.grid(row = 1, column = 5)

        # Main Table Title & Headers
        self.table_title.grid(row = 5, column = 0, columnspan = 7, 
            sticky = tk.W, pady = (15,0))
        for col_index, header in enumerate(self.table_headers):
            header.grid(row = 6, column = col_index)

        # Index Labels
        for row_index, index_num in enumerate(self.indexes):
            index_num.grid(row = row_index + 7, column = 0)

        # Entry Widgets
        column_index = 1
        for entry_widget in self.entry_widgets:
            if column_index == 3: # need to skip over type's column
                column_index += 1
            for row_index in range(7, self.num_flows + 7):
                entry_widget[row_index - 7].grid(row = row_index, column = column_index)
            column_index += 1

        # Drop-Down Type Menus
        for row_index, type_menu in enumerate(self.type_menus):
            type_menu.grid(row = row_index + 7, column = 3)


if __name__ == "__main__":
    class FakeAddProj():
        def __init__(self):
            attr_dict = {"name":"Project1", "num_invest":0, "num_flows":5, "rand_data":False, 
                "mult":False, "inflation":False, "taxes":False, "uncertainty":False, 
                "depreciation":"None", "distribution":"Triangular", "estimate":"Mean"}
            for attr in attr_dict:
                setattr(self, attr, attr_dict[attr])

    fake_proj = FakeAddProj()
    param_detail = ParamDetail(fake_proj)
    param_detail.pack(fill='both', expand=True)
    param_detail.mainloop() # i'm not sure why this works...