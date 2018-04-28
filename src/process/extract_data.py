#!/usr/bin/env python
# # -*- coding: utf-8 -*-
""" This module will have functions related to processing and extracting data from dfs.

Vijay Daultani
"""

# python native modules
from __future__ import print_function
import numpy
import sys


def single_metric(data_df, metric, task, own=True):
    """Function description.
    Parameters
    ----------
    data_df: pandas dataframe
      pandas dataframe consisting of the complete data.
    metric: string
      string representing the metric for which to extract the data.
    task: integer
      task number on that dataset for which to extract the data.
    own: boolean
      boolean variable specifying if extrat only methods proposed in paper.
    Returns
    -------
    methods: numpy array
      numpy array withthe names of the method.
    years: numpy array
      numpy array with the years each method was proposed.
    perf: numpy array
      numpy array with the performance of method on given input metric.
    """
    if (own == True):
        extracted_df = data_df.loc[data_df["PROPOSED"] == 1]
    else:
        extracted_df = data_df

    # filter based on task
    if (task != sys.maxint):
        extracted_df = extracted_df.loc[extracted_df["TASK"] == task]

    # sort the extracted_df based on year
    extracted_df = extracted_df.sort_values(by="YEAR")

    methods = extracted_df["METHOD"].values
    years = extracted_df["YEAR"].values
    perf = extracted_df[metric].values

    # change methods which string having unicode to ascii
    methods = [
        unicode(txt, "utf-8").encode("ascii", errors="ignore")
        for txt in methods
    ]
    return methods, years, perf


def unique_tasks(data_df):
    """Function to return all unique tasks in given input df.
    Parameters
    ----------
    data_df: pandas dataframe
      pandas dataframe of which all unique tasks need to be extracted.
    Returns
    -------
    tasks_list: list
      list of integers with all unique tasks in input data_df.
    """
    # check if column 'TASK' exist in the dataframe
    all_unique_tasks = list(
        set(data_df[data_df["TASK"].notnull()]["TASK"].tolist()))
    return all_unique_tasks
