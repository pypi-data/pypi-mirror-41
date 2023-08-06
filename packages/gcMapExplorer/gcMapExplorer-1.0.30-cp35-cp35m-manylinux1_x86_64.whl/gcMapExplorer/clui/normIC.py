#!/usr/bin/env python3
#
# Author: Rajendra Kumar
#
# This file is part of gcMapExplorer
# Copyright (C) 2016-2017  Rajendra Kumar, Ludvig Lizana, Per Stenberg
#
# gcMapExplorer is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gcMapExplorer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gcMapExplorer.  If not, see <http://www.gnu.org/licenses/>.
#
#=============================================================================

import os
import sys
import re
import argparse

import gcMapExplorer.lib as gmlib

from gcMapExplorer.config import getConfig

# get configuration
config = getConfig()

description = \
""" Normalization by Iterative Correction method
===============================================================

This method normalize the raw contact map by removing biases from experimental procedure.
This is an method of matrix balancing, however, in the normalized, sum of rows
and columns are NOT equal to one.

For more details, see this publication: http://dx.doi.org/10.1038/nmeth.2148


Please cite:
Imakaev et al. (2012), Iterative correction of Hi-C data reveals hallmarks of chromosome organization.
Nature Methods 9, 999–1003 (2012). http://dx.doi.org/10.1038/nmeth.2148

================================================================
"""

inputFileHelp = \
""" Input ccmap or gcmap file.

"""

inputFileFormatHelp = \
""" Input format: 'ccmap' or 'gcmap'.

"""


outputFileHelp = \
""" Output ccmap or gcmap file.

When input file is ccmap, output file can be gcmap. However, when a input file
is gcmap, output file will be only in gcmap.

"""

outputFileFormatHelp = \
""" Input format: 'ccmap' or 'gcmap'.

When input file is ccmap, output file can be gcmap. However, when a input file
is gcmap, output file will be only in gcmap.

"""

vminHelp = \
""" Minimum threshold value for normalization.
If contact frequency is less than or equal to this threshold value,
this value is discarded during normalization.

"""

vmaxHelp = \
""" Maximum threshold value for normalization.
If contact frequency is greater than or equal to this threshold value,
this value is discarded during normalization.

"""

tolHelp = \
""" Tolerance for matrix balancing.
Smaller tolerance increases accuracy in sums of rows and columns.
Tolerance value. The relative increment in the results before declaring
convergence.

"""

iterationHelp = \
""" Number of iteration to stop the normalization.

"""

percentile_threshold_no_data_help = \
""" It can be used to filter the map, where rows/columns with largest numbers
of missing data can be discarded. Its value should be between 1 and 100.
This options discard the rows and columns which are above this percentile.
For example: if this value is 99, those rows or columns will be discarded which
contains larger than number of zeros (missing data) at 99 percentile.

To calculate percentile, all blank rows are removed, then in all rows, number
of zeros are counted. Afterwards, number of zeros at input percentile is
obtained. In next step, if a row contain number of zeros larger than this
percentile value, the whole row and column is assigned to have missing data.
This percentile indicates highest numbers of zeros (missing data) in given
rows/columns.

"""

threshold_data_occup_help = \
""" It can be used to filter the map, where rows/columns with largest numbers
of missing data can be discarded.This ratio is:
  (number of bins with data) / (total number of bins in the given row/column)

For example: if -tdo = 0.8, then all rows containing more than 20%% of
missing data will be discarded.

"""

citation = \
"""
Please Cite
===========
Imakaev et al. (2012), Iterative correction of Hi-C data reveals hallmarks of chromosome organization.
Nature Methods 9, 999–1003. http://dx.doi.org/10.1038/nmeth.2148

"""


def main():

    # Construct command line arguments and parsed it
    parser, args = parseArguments()

    # check input file exist
    if args.inputFile is not None:
        checkFileExist(args.inputFile, parser)
    else:
        msg = 'No input file!!!'
        showErrorAndExit(parser, msg)

    args.inputFile = os.path.normpath(args.inputFile)

    # check input file format provided
    if args.inputFileFormat is None:
        msg = 'No input file format given !!!'
        showErrorAndExit(parser, msg)

    # check output file provided
    if args.outputFile is None:
        msg = 'No output file name given !!!'
        showErrorAndExit(parser, msg)

    args.outputFile = os.path.normpath(args.outputFile)

    # check output file format provided
    if args.outputFileFormat is None:
        msg = 'No output file format given !!!'
        showErrorAndExit(parser, msg)

    if args.outputFileFormat == 'ccmap' and args.inputFileFormat == 'gcmap':
        msg = 'With gcmap input format, output format should be gcmap format.'
        showErrorAndExit(parser, msg)

    if args.percentile_threshold_no_data is not None and args.threshold_data_occup is not None:
        msg = 'Both Percentile and Fraction filters cannot be used simultaneously!!'
        showErrorAndExit(parser, msg)

    if args.outputFileFormat == 'ccmap' and args.inputFileFormat == 'ccmap':
        gmlib.normalizer.normalizeCCMapByIC(args.inputFile, tol=args.tol, iteration=args.iteration,
                                            outFile=args.outputFile, vmin=args.vmin, vmax=args.vmax,
                                            percentile_threshold_no_data=args.percentile_threshold_no_data,
                                            threshold_data_occup=args.threshold_data_occup,
                                            workDir=args.workDir)

    if args.outputFileFormat == 'gcmap' and args.inputFileFormat == 'ccmap':
        norm_ccmap = gmlib.normalizer.normalizeCCMapByIC(args.inputFile, tol=args.tol,  iteration=args.iteration,
                                            vmin=args.vmin, vmax=args.vmax,
                                            percentile_threshold_no_data=args.percentile_threshold_no_data,
                                            threshold_data_occup=args.threshold_data_occup,
                                            workDir=args.workDir)
        gmlib.gcmap.addCCMap2GCMap(norm_ccmap, args.outputFile, compression=args.compression)


    if args.outputFileFormat == 'gcmap' and args.inputFileFormat == 'gcmap':
        gmlib.normalizer.normalizeGCMapByIC(args.inputFile, args.outputFile,
                                            tol=args.tol,  iteration=args.iteration,
                                            vmin=args.vmin, vmax=args.vmax,
                                            percentile_threshold_no_data=args.percentile_threshold_no_data,
                                            threshold_data_occup=args.threshold_data_occup,
                                            workDir=args.workDir)

    print(citation)

def parseArguments():
    parser = argparse.ArgumentParser(
                prog='gcMapExplorer normIC',
                description=description,
                formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', action='store',
                        metavar='input.gcmap',
                        dest='inputFile', help=inputFileHelp)

    parser.add_argument('-fi', '--format-input', action='store',
                        metavar='gcmap',
                        choices=['gcmap', 'ccmap', 'hicmap'],
                        dest='inputFileFormat', help=inputFileFormatHelp)

    parser.add_argument('-o', '--output', action='store',
                        metavar='output.gcmap',
                        dest='outputFile', help=outputFileHelp)

    parser.add_argument('-fo', '--format-output', action='store',
                        metavar='gcmap',
                        choices=['gcmap', 'ccmap'],
                        dest='outputFileFormat', help=outputFileFormatHelp)

    parser.add_argument('-t', '--tolerance', action='store',
                        dest='tol', metavar=1e-4,
                        type = float, default=1e-4,
                        help=tolHelp)

    parser.add_argument('-vmax', '--maximum-value', action='store',
                        dest='vmax', type=float, metavar=None,
                        help=vminHelp)

    parser.add_argument('-vmin', '--minimum-value', action='store',
                        dest='vmin', metavar=None, type=float,
                        help=vmaxHelp)

    parser.add_argument('-c', '--iteration', action='store',
                        dest='iteration', metavar=500,
                        type = int, default=500,
                        help=iterationHelp)

    parser.add_argument('-ptnd', '--percentile-threshold-no-data', action='store',
                        dest='percentile_threshold_no_data', metavar=99,
                        type = float,
                        help=percentile_threshold_no_data_help)

    parser.add_argument('-tdo', '--threshold-data-occupancy', action='store',
                        dest='threshold_data_occup', metavar=0.8,
                        type = float,
                        help=threshold_data_occup_help)

    parser.add_argument('-cmeth', '--compression-method', action='store',
                        dest='compression', metavar='lzf',
                        choices=['lzf', 'gzip'], default='lzf',
                        help='Data compression method for output gcmap file.\n')

    parser.add_argument('-wd', '--work-dir', action='store', dest='workDir',
                        default=config['Dirs']['WorkingDirectory'],
                        metavar=config['Dirs']['WorkingDirectory'],
                        help='Directory where temporary files will be stored.')

    idx = sys.argv.index("normIC")+1
    args = parser.parse_args(args=sys.argv[idx:])

    return parser, args


def checkFileExist(filename, parser):
    if not os.path.isfile(filename):
        parser.print_help()
        print("\n===== ERROR =======")
        print("File: {0} does not exist !!!\n".format(filename))
        print("See Usage Above!!!")
        sys.exit(-1)


def showErrorAndExit(parser, message):
    parser.print_help()
    print("\n===== ERROR =======")
    print(message)
    print("See Usage Above!!!")
    sys.exit(-1)
