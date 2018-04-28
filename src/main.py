#!/usr/bin/env python
# # -*- coding: utf-8 -*-
""" Main file working as a wrapper for all the implemented packages in repo.

Vijay Daultani
"""

# python native modules
from __future__ import print_function
import os
import sys
import time
import yaml
import argparse
import matplotlib
import matplotlib.pyplot as plt

# 3rd party modules
import progressbar

# modules from current implementation
from plots import scatter_plot
from helpers import load_data
from process import extract_data
from process import join_data


# instantiate the parser
def create_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Arguments for the wrapper application")
    parser.add_argument(
        "--dpi",
        "-dpi",
        dest="dpi",
        type=int,
        help="dpi settings for resolution of savefig")
    parser.add_argument(
        "--input",
        "-i",
        dest="input_path",
        help="Input file path for a single dataset.")
    parser.add_argument(
        "--out_dir", "-o_t", dest="out_dir", help="Output file path template.")
    parser.add_argument(
        "--metadata_file_path",
        "-md_f_p",
        dest="metadata_file_path",
        help="Paper citations and meta data file path for NLP Task")
    parser.add_argument(
        "--datasets_config_file_path",
        "-d_c_f_p",
        dest="datasets_config_file_path",
        help="Yaml configuration file for datasets and task")
    return parser


def main():
    """Main function of the program.
    """
    # create parser and parse args
    parser = create_parser()
    args = parser.parse_args()

    # output
    out_dir = args.out_dir
    in_dir = args.input_path
    dpi = args.dpi
    metadata_file_path = args.metadata_file_path
    datasets_config = yaml.load(open(args.datasets_config_file_path))

    # parse datasets
    for dataset, config in datasets_config.iteritems():
        input_file = os.path.join(in_dir, dataset + ".csv")
        print("\nprocessing input file {}\n".format(input_file))
        # print("configuration {}".format(config))

        # load the data
        data_df = load_data.csv_to_panda(input_file)
        meta_df = load_data.csv_to_panda(metadata_file_path)

        # for each metric
        metrics = config["metric"]
        for metric in metrics:
            # get joined dataframe with year info for each paper
            joined_df = join_data.data_inner_meta(data_df, meta_df)

            if "tasks" in config.keys():
                tasks = config["tasks"]
            else:
                tasks = [sys.maxint]

            for task in tasks:
                # extract data
                methods, years, perf = extract_data.single_metric(
                    joined_df, metric, task, own=True)

                # create output path
                if (task != sys.maxint):
                    figure_name = dataset + "-" + str(task) + "-" + metric
                else:
                    figure_name = dataset + "-" + metric
                out_file_name = figure_name + ".png"
                out_file_path = os.path.join(out_dir, out_file_name)

                # get figure
                fig = scatter_plot.single_dataset(
                    dataset, metric, methods, years, perf, figure_name, task)
                fig.savefig(out_file_path, dpi=dpi)
                plt.close()
                print("wrote plot file at {}".format(out_file_path))
    return


if __name__ == "__main__":
    main()
