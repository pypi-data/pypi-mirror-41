#!/usr/bin/env python

""" Broad collection of utility functions and constants.

.. codeauthor:: Raymond Ehlers <raymond.ehlers@cern.ch>, Yale University
"""

import logging
import numpy as np

from pachyderm import histogram

# Setup logger
logger = logging.getLogger(__name__)

# Small value - epsilon
# For use to offset from bin edges when finding bins for use with SetRange()
# NOTE: sys.float_info.epsilon is too small in some cases and thus should be avoided
epsilon = 1e-5

###################
# Utility functions
###################
def moving_average(arr: np.ndarray, n: int = 3) -> np.ndarray:
    """ Calculate the moving overage over an array.

    Algorithm from: https://stackoverflow.com/a/14314054

    Args:
        arr (np.ndarray): Array over which to calculate the moving average.
        n (int): Number of elements over which to calculate the moving average. Default: 3
    Returns:
        np.ndarray: Moving average calculated over n.
    """
    ret = np.cumsum(arr, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def get_array_for_fit(observables: dict, track_pt_bin: int, jet_pt_bin: int) -> histogram.Histogram1D:
    """ Get a Histogram1D associated with the selected jet and track pt bins.

    This is often used to retrieve data for fitting.

    Args:
        observables (dict): The observables from which the hist should be retrieved.
        track_pt_bin (int): Track pt bin of the desired hist.
        jet_ptbin (int): Jet pt bin of the desired hist.
    Returns:
        Histogram1D: Converted TH1 or uproot histogram.
    Raises:
        ValueError: If the requested observable couldn't be found.
    """
    for name, observable in observables.items():
        if observable.track_pt_bin == track_pt_bin and observable.jet_pt_bin == jet_pt_bin:
            return histogram.Histogram1D.from_existing_hist(observable.hist)

    raise ValueError("Cannot find fit with jet pt bin {jet_pt_bin} and track pt bin {track_pt_bin}")
