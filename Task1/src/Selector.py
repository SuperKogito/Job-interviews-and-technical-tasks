# python
# -*- coding: utf-8 -*-
"""
- Created on: 16.07.2019
- Author:     Ayoub Malek
"""
import warnings


class Selector:
    """
    Select data rows based on parsed arguments.

    Attributes:
        args (dict)             : dictionray of command arguments.
        data (pandas.DataFrame) : loaded data from csv.
    """
    def __init__(self, args, data):
        self.args = args
        self.data = data
        self.select_data()

    def select_data(self):
        """
        Select data rows based on user commnd arguments.
        """
        # Suppress UserWarning: Boolean Series key will be reindexed to match DataFrame index.
        warnings.filterwarnings("ignore")
        # filter data
        self.data = self.data[self.data["measurement_name"] == self.args["measurement_name"]]
        if self.args["device_id"]      : self.data = self.data[self.data["device_id"] == self.args["device_id"]]
        if self.args["start_timestamp"]: self.data = self.data[self.data["timestamp"] >= self.args["start_timestamp"]]
        if self.args["end_timestamp"]  : self.data = self.data[self.data["timestamp"] <= self.args["end_timestamp"]]

    def get_max(self):
        """
        Get and print the maximum value of the selected data.
        """
        print(self.data["measurement_value"].max())

    def get_min(self):
        """
        Get and print the minimum value of the selected data.
        """
        print(self.data["measurement_value"].min())

    def get_avg(self):
        """
        Get and print the average value of the selected data.
        """
        print(self.data["measurement_value"].mean())

    def get_cnt(self):
        """
        Get and print count of selected data rows.
        """
        print(self.data.count())
