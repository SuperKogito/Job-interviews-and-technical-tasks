# python
# -*- coding: utf-8 -*-
"""
- Created on: 16.07.2019
- Author:     Ayoub Malek
"""
import sys
import datetime


class ExceptionsHandler:
    """
    Handle all exceptions caused by incorrect commands.

    Attributes:
        args  (dict)             : dictionray of command arguments.
        data  (pandas.DataFrame) : loaded data from csv.
        supported_actions (list) : list of supported actions.
        exception         (dict) : dictionary of the exception descriptions.
    """
    def __init__(self, args, data):
        self.args = args
        self.data = data
        self.supported_actions = ["max", "min", "avg", "cnt"]
        self.exception = {"MissingArgumentException"          : "MissingArgumentException: a required argument is missing",
                          "ActionException"                   : "ActionException: given action is not supported",
                          "MeasurementValueException"         : "MeasurementValueException: no such measurement name in data",
                          "DeviceIdException"                 : "DeviceIdException: no such device id in data",
                          "TimeStampException"                : "TimeStampException: end timestamp must be after start timestamp",
                          "IncorrectTimeStampFormatException" : "IncorrectTimeStampFormatException: timestamp with unexpected format" }

    def check_args(self):
        """
        Check parsed command arguments based on agent's wave file and username.
        """
        self.check_action()
        self.check_measurement_name()
        if self.args["device_id"]       != None : self.check_device_id()
        if self.args["start_timestamp"] != None : self.validate_timestamp(self.args["start_timestamp"])
        if self.args["end_timestamp"]   != None : self.validate_timestamp(self.args["end_timestamp"])
        if self.args["start_timestamp"] != None and self.args["end_timestamp"] != None : self.check_timestamp()

    def check_action(self):
        """
        Check parsed action argument and raise exception if the action is not supported or if no action is provided.
        """
        if self.args["action"] == None                       : self.raise_exception("MissingArgumentException")
        if self.args["action"] not in self.supported_actions : self.raise_exception("ActionException")

    def check_measurement_name(self):
        """
        Check parsed measurement name argument and raise error if no such measurement name in data.
        """
        measurement_names = self.data["measurement_name"].values
        if self.args["measurement_name"] == None                  : self.raise_exception("MissingArgumentException")
        if self.args["measurement_name"] not in measurement_names : self.raise_exception("MeasurementValueException")

    def check_device_id(self):
        """
        Check parsed device id argument and raise exception if there is no such id in data.
        """
        device_ids = self.data["device_id"].values
        if self.args["device_id"] not in device_ids: self.raise_exception("DeviceIdException")

    def check_timestamp(self):
        """
        Check parsed timestamp arguments and raise exception in case of wrong format or wrong chronological order.
        """
        # check if timestamps format
        start_timestamp = self.validate_timestamp(self.args["start_timestamp"])
        end_timestamp   = self.validate_timestamp(self.args["end_timestamp"])
        # check if timestamps order
        if start_timestamp > end_timestamp : self.raise_exception("TimeStampException")

    def validate_timestamp(self, timestamp):
        """
        Validate the timestamp format otherwise raise in exception.

        Args:
            timestamp (str) : timestamp argument as a string.

        Returns:
            (datetime.datetime)  : parsed datetime object using the datetime library.
        """
        try              : return datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError: self.raise_exception("IncorrectTimeStampFormatException")

    def raise_exception(self, exception_key):
        """
        Raise exception by printing the exception description and exiting.

        Args:
            exception_key (str) : exception key associated with the exception's description in the eceptions dictionary.
        """
        print(self.exception[exception_key])
        sys.exit(0)
