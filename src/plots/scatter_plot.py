#!/usr/bin/env python
# # -*- coding: utf-8 -*-
""" Module for implementing all the functions related to plotting graphs.

Vijay Daultani
"""
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt

# 3rd party modules
from adjustText import adjust_text


def single_dataset(dataset, metric, methods, years, perfs, figure_name, task):
    """Function for plotting scatter plot of single dataset.
    Parameters
    ----------
    dataset: string
      name of the dataset for evaluation.
    task: string
      name or number of task for the dataset.
    metric: string
      name of the evaluation metric for performance.
    methods: numpy array of strings
      numpy 1D array of strings where each string represents one method name.
    years: numpy array of int
      numpy 1D array of int where each int value represents the year method was proposed in.
      This will be dimension x of plot.
    perfs: numpy array of float
      numpy 1D array of int where each float value represents the performance of method,
      at same index in method array proposed in year at same index in years array.
    figure_name: string
      title to be assigned to the graph
    Returns
    -------
    plot: matplotlib figure
      matplotlib figure.
    """
    p1 = plt.plot(years, perfs, color="blue", marker="o")
    texts = []
    for x, y, z in zip(years, perfs, methods):
        texts.append(plt.text(x, y, z))
    plt.xlabel("years")
    plt.ylabel(metric)
    plt.title(figure_name)
    adjust_text(
        texts,
        only_move="y",
        arrowprops=dict(arrowstyle="->", color="r", lw=0.5))
    fig = plt.gcf()
    fig.tight_layout()
    return fig
    """
    # below code generate overlapping nodes in scatter plot
    fig, ax = plt.subplots()
    ax.scatter(years, perfs, marker='o')

    for i, txt in enumerate(methods):
        ax.annotate(
            unicode(txt, "utf-8").encode("ascii", errors="ignore"), (years[i],
                                                                     perfs[i]))

    #plt.plot(years, perfs, 'or-')
    plt.title(figure_name)
    plt.ylabel(metric)
    plt.xlabel("year")

    # get figure and  define layout
    #fig = plt.gcf()
    fig.tight_layout()
    return fig
    """
