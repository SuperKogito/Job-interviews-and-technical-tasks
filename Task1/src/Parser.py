# python
# -*- coding: utf-8 -*-
"""
- Created on: 16.07.2019
- Author:     Ayoub Malek
"""
import argparse
import pandas as pd


class Parser:
    """
    Parse and make sense of the command arguments.

    Attributes:
        parser                     : argparser object.
        args    (dict)             : dictionray of command arguments.
        data    (pandas.DataFrame) : loaded data from csv.
    """
    def __init__(self):
        # define argsparser
        self.parser = argparse.ArgumentParser()
        self.args   = self.add_arguments()
        self.data   = ""

    def excute_action(self, selector, data):
        """
        Excute action based on the provided argument.

        Args:
            selector                : selector object to handle data filtering and selection.
            data (pandas.DataFrame) : loaded data from csv.
        """
        # select and excute the parsed action
        if   self.args["action"] == "max": selector.get_max()
        elif self.args["action"] == "min": selector.get_min()
        elif self.args["action"] == "avg": selector.get_avg()
        elif self.args["action"] == "cnt": selector.get_cnt()

    def load_data(self, file_name):
        """
        Load data from csv.

        Args:
            file_name (str) : file name/path to csv file containing the data.

        Returns:
            (pandas.DataFrame) : loaded data from csv.
        """
        # init file name and column names
        column_names = ["device_id", "timestamp", "measurement_name", "measurement_value"]
        # load and parse data
        data = pd.read_csv(file_name, sep = ",", names = column_names)
        data["timestamp"] = pd.to_datetime(data["timestamp"])
        return data

    def add_arguments(self):
        """
        Add/parse arguments.
        """
        self.parser.add_argument('action',             help = 'action name')
        self.parser.add_argument('--device_id',        help = 'script shows only result for this one device (optional)')
        self.parser.add_argument('--measurement_name', help = 'show only result for one measurement type')
        self.parser.add_argument('--start_timestamp',  help = 'only count measurements that is younger than TIMESTAMP (optional)')
        self.parser.add_argument('--end_timestamp',    help = 'only count measurements that is older than TIMESTAMP (optional)')
        return vars(self.parser.parse_args())
