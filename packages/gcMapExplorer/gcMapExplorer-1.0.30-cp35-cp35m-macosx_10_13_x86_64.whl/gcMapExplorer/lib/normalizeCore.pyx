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

import numpy as np

from . import util

# This method normalize the raw contact map by removing biases from experimental procedure.
# For more details, see `this publication <http://www.nature.com/nmeth/journal/v9/n10/full/nmeth.2148.html>`_.
#
# Steps are taken from supporting information.
# Below only double-sided (DS) reads only version is implemented, therefore
# terms with SS are not present here. For example Steps 2 and 3 is not present.

def performIterativeCorrection(matrix, tol, iteration):
    count = 0
    contact_count = np.sum(matrix)
    B = np.ones((matrix.shape[0],1), dtype=np.float)   # Step - 0
    prev_B = None

    # Step - 8, Repeat steps 1-7 until variance of dB becomes negligible.
    while True:
        dB = np.sum(matrix, axis=0)                   # Step - 1, Sum over rows
        dB = dB.reshape((matrix.shape[0],1))
        dB = dB/np.mean(dB[dB != 0])                  # Step - 4, Renormalization by mean value
        dB[dB == 0] = 1                               # Step - 5, Set zeros value to one

        # Step - 6, Divide W_ij by dB_i dB_j
        matrix /= dB
        matrix /= dB.T

        B = B *  dB                                   # Step - 7
        B *= np.sqrt(np.sum(matrix) / contact_count)
        matrix *= contact_count / np.sum(matrix)

        if prev_B is not None:
            if np.abs(prev_B - B).sum() < tol or count > iteration:
                break

        count = count + 1
        prev_B = B.copy()

# Vanilla coverage normalization
def performVCNormalization(A, Out=None, sqroot=False, bNoData=None):
    mshape = A.shape

    toReturn = False

    if Out is None:
        Out = np.zeros(A.shape, dtype=A.dtype)
        toReturn = True

    csum = np.sum(A, axis=1)
    for m in range(mshape[0]):
        if bNoData is not None:
            if bNoData[m]:
                continue
        Out[m] = (A[m] / csum[m])[:]

    for m in range(mshape[0]):
        if bNoData is not None:
            if bNoData[m]:
                continue
        Out[:, m] = (Out[:,m] / csum[m])[:]

    if sqroot:
        Out[:] = np.sqrt(Out[:])

    if toReturn:
        return Out

def normalizeByAvgContactByDivision(A, avgContacts, Out=None):
    mshape = A.shape

    toReturn = False

    if Out is None:
        Out = np.zeros(A.shape, dtype=A.dtype)
        toReturn = True

    # Do along diagonal
    for m in range(mshape[0]):

        # do for postive diagonal offset
        idx = util.kth_diag_indices(m, A)
        if avgContacts[m] != 0:
            Out[idx] = A[idx] / avgContacts[m]
        else:
            Out[idx] = A[idx]

        # Do for negative diagonal offset
        del idx
        if m != 0:
            idx = util.kth_diag_indices(m*-1, A)
            if avgContacts[m] != 0:
                Out[idx] = A[idx] / avgContacts[m]
            else:
                Out[idx] = A[idx]
            del idx

    if toReturn:
        return Out

def normalizeByAvgContactBySubtraction(A, avgContacts, Out=None):
    mshape = A.shape

    toReturn = False

    if Out is None:
        Out = np.zeros(A.shape, dtype=A.dtype)
        toReturn = True

    # Do along diagonal
    for m in range(mshape[0]):

        # do for postive diagonal offset
        idx = util.kth_diag_indices(m, A)
        if avgContacts[m] != 0:
            values = A[idx] -  avgContacts[m]
            vidx = np.nonzero( values < 0)
            if vidx[0].shape[0] > 0:
                values[vidx] = np.ones(vidx[0].shape)
            vidx = np.nonzero( A[idx] == 0)
            if vidx[0].shape[0] > 0:
                values[vidx] = np.zeros(vidx[0].shape)

            Out[idx] = values

        else:
            Out[idx] = A[idx]

        # Do for negative diagonal offset
        del idx
        if m != 0:
            idx = util.kth_diag_indices(m*-1, A)
            if avgContacts[m] != 0:
                values = A[idx]  - avgContacts[m]
                vidx = np.nonzero( values < 0)
                if vidx[0].shape[0] > 0:
                    values[vidx] = np.ones(vidx[0].shape)
                vidx = np.nonzero( A[idx] == 0)
                if vidx[0].shape[0] > 0:
                    values[vidx] = np.zeros(vidx[0].shape)

                Out[idx] = values
            else:
                Out[idx] = A[idx]
            del idx

    if toReturn:
        return Out
