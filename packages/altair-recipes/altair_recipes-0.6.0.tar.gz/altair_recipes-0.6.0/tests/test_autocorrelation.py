import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
import numpy as np
import pandas as pd


#' <h2>Autocorrelation</h2>


@viz_reg_test
def test_autocorrelation():
    data = pd.DataFrame(dict(x=np.random.uniform(size=100)))
    return ar.autocorrelation(data, column="x", max_lag=15)


show_test(test_autocorrelation)
