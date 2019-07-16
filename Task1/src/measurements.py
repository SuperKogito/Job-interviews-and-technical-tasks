# python
# -*- coding: utf-8 -*-
"""
- Created on: 13.07.2019
- Author:     Ayoub Malek
"""
from Parser import Parser
from Selector import Selector
from ExceptionsHandler import ExceptionsHandler


if __name__ == "__main__":
    # parse arguments and
    parser   = Parser()
    # for debugging: print(parser.args)
    # load data
    parser.data  = parser.load_data(file_name = 'data.csv')
    # check if command is correct
    exceptions_handler = ExceptionsHandler(parser.args, parser.data)
    exceptions_handler.check_args()
    # select data based on command
    selector = Selector(parser.args, parser.data)
    # for debugging: print(selector.data)
    # excute action on selected data
    parser.excute_action(selector, parser.data)
