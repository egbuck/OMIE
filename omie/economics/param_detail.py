import tkinter as tk

class ParamDetail(tk.Frame):

    def __init__(self, Proj):
        super().__init__()
        attr_list = ["num_invest", "num_flows", "rand_data", 
            "mult", "inflation", "taxes", "uncertainty", 
            "depreciation", "distribution", "estimate"]
        for attr in attr_list:
            setattr(self, attr, getattr(Proj, attr))
        self.type_choices = ["Single", "Uniform", "Gradient"]

        # Table Title & Headers
        self.table_title = tk.Label(self, text = "Cash Flow Data - Amounts Negative for Expenditures and Positive for Revenues")
        self.table_headers = [
            tk.Label(self, text = "Index"),
            tk.Label(self, text = "Description"),
            tk.Label(self, text = "Amount($)"),
            tk.Label(self, text = "Type"),
            tk.Label(self, text = "Start"),
            tk.Label(self, text = "End"),
            tk.Label(self, text = "Parameter"),
            tk.Label(self, text = "Factor"),
            tk.Label(self, text = "CF. NPW($)")
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
        # Table Title & Headers
        self.table_title.grid(row = 0, column = 0, columnspan = 7)
        for col_index, header in enumerate(self.table_headers):
            header.grid(row = 1, column = col_index)

        # Index Labels
        for row_index, index_num in enumerate(self.indexes):
            index_num.grid(row = row_index + 2, column = 0)

        # Entry Widgets
        column_index = 1
        for entry_widget in self.entry_widgets:
            if column_index == 3: # need to skip over type's column
                column_index += 1
            for row_index in range(2, self.num_flows + 2):
                entry_widget[row_index - 2].grid(row = row_index, column = column_index)
            column_index += 1

        # Drop-Down Type Menus
        for row_index, type_menu in enumerate(self.type_menus):
            type_menu.grid(row = row_index + 2, column = 3)


if __name__ == "__main__":
    class FakeAddProj():
        def __init__(self):
            attr_dict = {"num_invest":0, "num_flows":5, "rand_data":False, 
                "mult":False, "inflation":False, "taxes":False, "uncertainty":False, 
                "depreciation":"None", "distribution":"Triangular", "estimate":"Mean"}
            for attr in attr_dict:
                setattr(self, attr, attr_dict[attr])

    fake_proj = FakeAddProj()
    param_detail = ParamDetail(fake_proj)
    param_detail.pack(fill='both', expand=True)
    param_detail.mainloop() # i'm not sure why this works...