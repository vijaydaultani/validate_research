#!/usr/bin/env python
# # -*- coding: utf-8 -*-
""" Module to join data from single dataset and meta data sheet.

Vijay Daultani
"""

import numpy
import csv
import pandas


def data_inner_meta(data_df, meta_df):
    """Function to join dataset df and metadata df.
    Parameters
    ----------
    data_df: pandas dataframe
      pandas dataframe corresponding to given dataset.
    meta_df: pandas dataframe
      pandas dataframe corresponding to metadata i.e. citations sheet.
    Returns
    -------
    joined_df: pandas dataframe
      pandas dataframe after joining both data_df and meta_df based on "PAPER NUMBER"
    """
    # read csv file into a pandas df
    joined_df = pandas.merge(data_df, meta_df, on="PAPER NUMBER")
    return joined_df
