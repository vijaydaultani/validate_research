#!/usr/bin/env python
# # -*- coding: utf-8 -*-
""" Module to convert google sheet to numpy arrays.

Vijay Daultani
"""

import numpy
import csv
import pandas


def csv_to_panda(input_file):
    """Function to return Function description.
    Parameters
    ----------
    input_file: string
      path of the input_file.
    Returns
    -------
    columns: list of string
      list of column names extracted from first line of file.
    data: numpy 2D array
      numpy 2D array loading complete file other than first row.
    """
    # read csv file into a pandas df
    df = pandas.read_csv(input_file, delimiter=",", header=0)
    return df


'''
    print df
    # get names of the columns other than first column name
    methods = df.ix[:,0].tolist()
    # read rest of the data frame other than first column 
    data = df.iloc[:, 0:len(df.columns)]
    # translate into numpy array
    data = data.values
    # transpose the numpy array
    #data = numpy.transpose(data)
    return columns, methods, data
'''
