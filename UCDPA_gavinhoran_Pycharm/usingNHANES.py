# So I used pip install nhanes to install the handler for the NHANes data set. And the code below to load it up.
# but it is just rammed with data in which I am not interested.

import pandas as pd
from nhanes.load import load_NHANES_data, load_NHANES_metadata

from UCDPA_gavinhoran_Pycharm.functionFile import csv_time_namer

data_df = load_NHANES_data(year='2017-2018')
metadata_df = load_NHANES_metadata(year='2017-2018')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data_df)


csvToDownload = pd.DataFrame(data_df)
#this produces a small but beautiful dataframe, containing my target for the next program!
csvToDownload.to_csv(csv_time_namer('NHANESdata'))