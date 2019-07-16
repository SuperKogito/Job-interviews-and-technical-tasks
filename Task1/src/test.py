# python
# -*- coding: utf-8 -*-
"""
- Created on: 15.07.2019
- Author:     Ayoub Malek
"""
import subprocess

def excute_command(desc, command):
    """
    Excute/test python measurements.py script.
    """
    process = subprocess.Popen(command, 
                               universal_newlines = True, 
                               shell              = True,
                               stdout             = subprocess.PIPE, 
                               stderr             = subprocess.PIPE)
    output, error = process.communicate()
    # format and print output
    print(str(desc))    
    print("------------------------------------------------------------------------------------------------------------------------------------")
    for output_line in output.split("\n"):
        print(output_line)


if __name__ == "__main__":
    # test the the help argument
    excute_command("Hep argument", "python measurements.py -h")
    
    # test actions
    for action in ["max", "min", "avg", "cnt"]:
        print("====================================================================================================================================")
        print("============================================== Testing %s =========================================================================" % action)
        print("====================================================================================================================================")
        # define command and its description
        base_command      = "python3 measurements.py " + action + " --measurement_name temperature"
        base_command_desc = "Correct command: action & measurment name" 
        # test correct commands
        excute_command(base_command_desc , base_command )
        excute_command(base_command_desc + "& device id",                                   base_command + " --device_id 0ea7f78a-d224-4d3a-a014-001a0794e746")
        excute_command(base_command_desc + "& device id & start timestamp",                 base_command + " --device_id 0ea7f78a-d224-4d3a-a014-001a0794e746 --start_timestamp \"2019-05-30 12:00:55.438\"")
        excute_command(base_command_desc + "& device id & end timestamp",                   base_command + " --device_id 0ea7f78a-d224-4d3a-a014-001a0794e746 --end_timestamp \"2019-05-30 12:00:55.438\"")
        excute_command(base_command_desc + "& device id & start timestamp & end timestamp", base_command + " --device_id 0ea7f78a-d224-4d3a-a014-001a0794e746 --start_timestamp \"2019-05-30 12:00:55.438\" --end_timestamp \"2019-05-31 12:00:55.438\"")
        # test faulty commands
        excute_command("ActionException test",                   "python3 measurements.py mean")
        excute_command("MissingArgumentException test",          "python3 measurements.py " + action)
        excute_command("MeasurementValueException test",         "python3 measurements.py " + action + " --measurement_name anything")
        excute_command("DeviceIdException test",                 "python3 measurements.py " + action + " --measurement_name wind --device_id 0ea7f78a-d224-4d3a-a014-0794e746")
        excute_command("TimeStampException test",                "python3 measurements.py " + action + " --measurement_name wind --start_timestamp \"30-05-2019 12:00:55.438\"")
        excute_command("TimeStampException test",                "python3 measurements.py " + action + " --measurement_name wind --end_timestamp \"2019-05-34 12:00:55.438\"")
        excute_command("IncorrectTimeStampFormatException test", "python3 measurements.py " + action + " --measurement_name wind --device_id 0ea7f78a-d224-4d3a-a014-001a0794e746 --measurement_name wind --start_timestamp \"2019-05-31 12:00:55.438\" --end_timestamp \"2019-04-30 12:00:55.438\"")
