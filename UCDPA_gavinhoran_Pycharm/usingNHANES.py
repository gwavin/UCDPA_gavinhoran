#So I used pip install nhanes to install the handler for the NHANes data set. And the code below to load it up.
# but it is just rammed with data in which I am not interested. I suppose 

import pandas as pd
from nhanes.load import load_NHANES_data, load_NHANES_metadata

data_df = load_NHANES_data(year='2017-2018')
metadata_df = load_NHANES_metadata(year='2017-2018')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data_df)