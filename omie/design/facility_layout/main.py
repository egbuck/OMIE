# Imports
import pandas as pd

class FacilityLayout(object):

    def __init__(
            self,
            problem_name = "Production",
            layout_data = {
                "num_depts":10,
                "num_fixed":0,
                "dimension":"m",
                "rand_prob":True
            }):
        self.problem_name = problem_name
        # Set layout_data attributes
        for attr in layout_data:
            setattr(self, attr, layout_data[attr])
        self.add_params()

    def add_params(self, **kwargs):
        """Add necessary parameters to the Facility Layout"""
        dist_meas = self.layout_data["dimension"]
        if self.rand_prob:
            self.create_rand_params()
        else:
            if len(kwargs) != 6:
                raise TypeError(f"add_params() needs 6 or 0 kwargs, {len(kwargs)} provided.")
            for key, value in kwargs.items():
                setattr(self, key, value)

    def create_rand_params(self):
        """Create random data for params in facility layout"""
        dist_meas = self.layout_data["dimension"]
        dept_names = [f"Dept. {x}" for x in range(1, self.layout_data["num_depts"] + 1)]
        self.facility_info = pd.Series(
            [1, 10, 10],
            index = [
                f"Scale-{dist_meas}/unit",
                f"Length-{dist_meas}",
                f"Width-{dist_meas}"
            ])
        self.dept_info = pd.DataFrame({
            "Name": [f"D {x}" for x in e(1, len(dept_names) + 1)],
            "F/V": ["V" for _ in dept_names],
            "Area": [100 // len(dept_names) for _ in dept_names]
            }, index = dept_names)
        self.flow_matrix = pd.DataFrame()
        self.cost_matrix = pd.DataFrame()
        if self.layout_data["num_fixed"] > 0:
            self.fixed_points = pd.DataFrame()
            self.fixed_point_costs = pd.DataFrame()

    def solve(self, solution_method, initial_solution, dist_metric,
        plant_width, plant_length, dept_width):
        pass