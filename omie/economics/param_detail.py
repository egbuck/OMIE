import tkinter as tk
import numpy_financial as npf

class ParamDetail(tk.Frame):

    def __init__(self, Proj):
        super().__init__()
        attr_list = ["name", "num_invest", "num_flows", "rand_data",
            "mult", "inflation", "taxes", "uncertainty",
            "depreciation", "distribution", "estimate"]
        for attr in attr_list:
            if attr in ["num_invest", "num_flows"]:
                setattr(self, attr, int(getattr(Proj, attr).get()))
            elif attr == "name":
                setattr(self, attr, getattr(Proj, attr).get())
            else:
                setattr(self, attr, getattr(Proj, attr))
        self.type_choices = ["Single", "Uniform", "Gradient"]

        # Window Title
        self.master.title("Parameters & Analysis")

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

        # Rates Param
        self.rates_header, self.rates_label = \
            tk.Label(self, text = "Rates (%)", font = "Helvetica 9 bold"), \
            tk.Label(self, text = "MARR (/yr)")
        self.rate_percent = tk.Entry(self)

        if self.num_flows > 0:
            self.flow_table_title = tk.Label(self,
                text = ("Cash Flow Data - Amounts Negative for "
                "Expenditures and Positive for Revenues"), font = "Helvetica 9 bold")
            self.create_table(prefix = "flow", num_prefix = self.num_flows)
        if self.num_invest > 0:
            self.invest_table_title = tk.Label(self,
                text = "Investment Data - Amounts Negative for Investments",
                font = "Helvetica 9 bold")
            self.create_table(prefix = "invest", num_prefix = self.num_invest)

        # Compute Rates Button
        self.compute_rates_button = tk.Button(self, text = "Compute Rates",
            command=self.compute_rates, bg = "#00bd21", fg = "#f5fcf6")

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

    def create_table(self, prefix, num_prefix):
        """Create table widgets for invest or flow data entry"""
        # Table Headers
        setattr(self, prefix + "_table_headers", [
            tk.Label(self, text = "Index", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Description", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Amount($)", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Type", font = "Helvetica 8 bold"),
            tk.Label(self, text = "Start", font = "Helvetica 8 bold"),
            tk.Label(self, text = "End", font = "Helvetica 8 bold"),
        ])
        if prefix == "flow":
            getattr(self, prefix + "_table_headers").append(tk.Label(self, text = "Parameter", font = "Helvetica 8 bold"))
        else:
            getattr(self, prefix + "_table_headers").append(tk.Label(self, text = "Salvage", font = "Helvetica 8 bold"))
        # Type Vars, Type Choices, & Index Labels
        setattr(self, prefix + "_types",
            [tk.StringVar(self) for _ in range(1, num_prefix + 1)])
        setattr(self, prefix + "_indexes",
            [tk.Label(self, text = str(x)) for x in range(1, num_prefix + 1)])

        # Entry widgets
        setattr(self, prefix + "_description_ents",
            [tk.Entry(self) for _ in range(1, num_prefix + 1)])
        setattr(self, prefix + "_amount_ents",
            [tk.Entry(self) for _ in range(1, num_prefix + 1)])
        setattr(self, prefix + "_start_ents",
            [tk.Entry(self) for _ in range(1, num_prefix + 1)])
        setattr(self, prefix + "_end_ents",
            [tk.Entry(self) for _ in range(1, num_prefix + 1)])
        setattr(self, prefix + "_parameter_ents",
            [tk.Entry(self) for _ in range(1, num_prefix + 1)])
        setattr(self, prefix + "_entry_widgets", [
            getattr(self, prefix + "_description_ents"),
            getattr(self, prefix + "_amount_ents"),
            getattr(self, prefix + "_start_ents"),
            getattr(self, prefix + "_end_ents"),
            getattr(self, prefix + "_parameter_ents")
        ])
        # Change disabled background color of end and param entries
        for end_ent in getattr(self, prefix + "_end_ents"):
            end_ent.config(disabledbackground = "#808080") # darker gray
        for end_ent in getattr(self, prefix + "_parameter_ents"):
            end_ent.config(disabledbackground = "#808080")

        # Drop-Down Type Menus
        if prefix == "flow":
            setattr(self, prefix + "_type_menus", [tk.OptionMenu(
                self, getattr(self, prefix + "_types")[x], *self.type_choices,
                command = lambda t = getattr(self, prefix + "_types")[x],
                    e = getattr(self, prefix + "_end_ents")[x],
                    p = getattr(self, prefix + "_parameter_ents")[x]: self.check_type(t, e, p)
                ) for x in range(0, num_prefix)
            ])
        else:
            setattr(self, prefix + "_type_menus", [tk.Label(
                self, text = "Investment") for _ in range(0, num_prefix)])

    def place_widgets(self):
        """Place the widgets in their grids"""
        # Project Name Labels
        self.name_header.grid(row = 0, column = 0, sticky = tk.W, columnspan = 2)
        self.name_prefix.grid(row = 1, column = 0, sticky = tk.E)
        self.name_label.grid(row = 1, column = 1, sticky = tk.W)

        # Periods Params - row 0 - 2, column 2-3
        self.period_header.grid(row = 0, column = 3)
        self.life_label.grid(row = 1, column = 2, sticky = tk.E)
        self.life.grid(row = 1, column = 3)
        self.reps_label.grid(row = 2, column = 2, sticky = tk.E)
        self.reps.grid(row = 2, column = 3)

        # Rates params
        self.rates_header.grid(row = 0, column = 5)
        self.rates_label.grid(row = 1, column = 4, sticky = tk.E)
        self.rate_percent.grid(row = 1, column = 5)

        # Compute Rates Button
        self.compute_rates_button.grid(row = 3, column = 5)

        ## Tables
        # Invest Table
        if self.num_invest > 0:
            self.place_table("invest", self.num_invest)
        # Num Flows Table
        if self.num_flows > 0:
            self.place_table("flow", self.num_flows)

    def place_table(self, prefix, num_prefix):
        """Place the table with prefix in grid"""
        # Define row buffer for if invest or flow table
        row_buffer = 0 if prefix == "invest" else 2 + self.num_invest

        # Main Table Title & Headers
        getattr(self, prefix + "_table_title").grid(row = 5 + row_buffer, column = 0, columnspan = 7,
            sticky = tk.W, pady = (15,0))
        for col_index, header in enumerate(getattr(self, prefix + "_table_headers")):
            header.grid(row = 6 + row_buffer, column = col_index)

        # Index Labels
        for row_index, index_num in enumerate(getattr(self, prefix + "_indexes")):
            index_num.grid(row = row_index + 7 + row_buffer, column = 0)

        # Entry Widgets
        column_index = 1
        for entry_widget in getattr(self, prefix + "_entry_widgets"):
            if column_index == 3: # need to skip over type's column
                column_index += 1
            for row_index in range(7, num_prefix + 7):
                entry_widget[row_index - 7].grid(row = row_index + row_buffer, column = column_index)
            column_index += 1

        # Drop-Down Type Menus
        for row_index, type_menu in enumerate(getattr(self, prefix + "_type_menus")):
            type_menu.grid(row = row_index + 7 + row_buffer, column = 3)

    def compute_rates(self):
        """Compute rates for cash flow analysis

        Study Period = Life(yrs) * Repetitions
        NPW = Factor * Amount
        Factor = E_Factor{_Inv}(MARR, Type, Start, End, Param/Salvage)
            {_Inv} if investment, different function otherwise
        Present (Life) = Sum(All NPW)
        Uniform (Life) = -PMT(MARR, Life(yrs), 1) * Present(Life)
        Present (SP) = -PV(MARR, Study Period, 1) * Uniform(Life)
        IRR - Algorithm...
        """
        self.study_period = float(self.life.get()) * float(self.reps.get())

        # NPW & Factor Calcs
        self.invest_factors, self.invest_npws = 0, 0
        if self.num_invest > 0:
            self.invest_factors = [1 for _ in range(self.num_invest)]
            self.invest_npws = [float(x.get()) for x in self.invest_amount_ents]
        self.flow_factors, self.flow_npws = 0, 0
        self.marr = float(self.rate_percent.get()) / 100
        if self.num_flows > 0:
            self.flow_factors = [1/((1+self.marr)**(float(start.get()))) for start in self.flow_start_ents]
            self.flow_npws = [factor * float(amount.get()) for factor, amount in zip(self.flow_factors, self.flow_amount_ents)]

        # present/uniform lifes & present sp
        self.present_life = sum(self.invest_npws) + sum(self.flow_npws)
        #self.uniform_life =
        #self.present_sp =
        # Calculate Internal rate of return
        net_cash_flows = [0] * (self.num_flows + self.num_invest)
        for i in range(self.num_invest):
            start = int(self.invest_start_ents[i].get())
            amount = float(self.invest_amount_ents[i].get())
            net_cash_flows[start] += amount
        for f in range(self.num_flows):
            start = int(self.flow_start_ents[f].get())
            amount = float(self.flow_amount_ents[f].get())
            net_cash_flows[start] += amount
        self.irr = npf.irr(net_cash_flows)
        self.place_rates()

    def place_rates(self):
        """Define & Place labels for showing output of compute_rates"""
        ## Define Labels
        # Table Headers & Labels/Values
        calc_bg_color = "#FFFF99"
        for prefix in ["invest", "flow"]:
            npw_prefix = "Fin. " if prefix == "invest" else "CF. "
            num_prefix = self.num_invest if prefix == "invest" else self.num_flows
            if num_prefix > 0:
                getattr(self, prefix + "_table_headers").extend([
                    tk.Label(self, text = "Factor", font = "Helvetica 8 bold"),
                    tk.Label(self, text = npw_prefix + "NPW ($)", font = "Helvetica 8 bold")
                ])
                setattr(self, prefix + "_factor_labels",
                    [tk.Label(self, text = str(x), bg = calc_bg_color) for x in getattr(self, prefix + "_factors")])
                setattr(self, prefix + "_cf_npw_labels",
                    [tk.Label(self, text = str(x), bg = calc_bg_color) for x in getattr(self, prefix + "_npws")])
        # Study Period, Present (Life) & IRR
        self.study_period_label, self.study_period_widg = \
            tk.Label(self, text = "Study Period", bg = calc_bg_color), tk.Label(self, text = str(self.study_period), bg = calc_bg_color)
        self.present_life_label, self.present_life_widg = \
            tk.Label(self, text = "Present (Life)", bg = calc_bg_color), tk.Label(self, text = str(self.present_life), bg = calc_bg_color)
        self.irr_label, self.irr_widg = \
            tk.Label(self, text = "IRR", bg = calc_bg_color), tk.Label(self, text = str(self.irr), bg = calc_bg_color)

        ## Place Labels in Grids
        self.study_period_label.grid(row = 3, column = 2, sticky = tk.E)
        self.present_life_label.grid(row = 1, column = 6, sticky = tk.E)
        self.irr_label.grid(row = 2, column = 6, sticky = tk.E)
        self.study_period_widg.grid(row = 3, column = 3)
        self.present_life_widg.grid(row = 1, column = 7)
        self.irr_widg.grid(row = 2, column = 7)

        # Table Headers/Values
        for prefix in ["invest", "flow"]:
            row_buffer = 0 if prefix == "invest" else 2 + self.num_invest
            num_prefix = self.num_invest if prefix == "invest" else self.num_flows
            if num_prefix > 0:
                getattr(self, prefix + "_table_headers")[-2].grid(row = 6 + row_buffer, column = 7)
                getattr(self, prefix + "_table_headers")[-1].grid(row = 6 + row_buffer, column = 8)
                for row_index in range(7, num_prefix + 7):
                    getattr(self, prefix + "_factor_labels")[row_index - 7].grid(row = row_index + row_buffer, column = 7)
                    getattr(self, prefix + "_cf_npw_labels")[row_index - 7].grid(row = row_index + row_buffer, column = 8)

if __name__ == "__main__":
    class FakeAddProj():
        def __init__(self):
            attr_dict = {"name":"Project1", "num_invest":2, "num_flows":5, "rand_data":False,
                "mult":False, "inflation":False, "taxes":False, "uncertainty":False,
                "depreciation":"None", "distribution":"Triangular", "estimate":"Mean"}
            for attr in attr_dict:
                setattr(self, attr, attr_dict[attr])

    fake_proj = FakeAddProj()
    param_detail = ParamDetail(fake_proj)
    param_detail.pack(fill='both', expand=True)
    param_detail.mainloop() # i'm not sure why this works...