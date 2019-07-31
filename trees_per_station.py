#takes trees csv and outputs dictionaries of radio station specific details

#import pandas as pd
import pandas as pd

#import numpy as np
import numpy as np

#read in csv
df_data = pd.read_csv('trees.csv')

#get list of radio stations
list_stations = df_data['radio'].unique()

#dataframe to store results with columns stations and relevant dicts
df_results = pd.DataFrame()
df_results['station'] = []
df_results['trees_per_area'] = []
df_results['trees_per_thousand'] = []

#loop through stations and assign values to dictionaries
for station in list_stations:
    #get results per station
    df_station_results = df_data.loc[df_data['radio'] == station]
    #create dictionaries
    dict_area = dict(zip(df_station_results.area,
                          df_station_results.new_trees_thousands))
    dict_area_pop = dict(zip(df_station_results.area,
                                  df_station_results.tree_per_thousand))
    #new temporary df to hold results in format of dicts in columns
    df_edit = pd.DataFrame()
    df_edit['station'] = [station]
    df_edit['trees_per_area'] = [dict_area]
    df_edit['trees_per_thousand'] = [dict_area_pop]
    #append to final output table
    df_results = df_results.append(df_edit)

#reset index to number rows for Arria
df_results.reset_index(inplace=True)

#drop old index column
df_results.drop(['index'], axis=1, inplace=True)

#output to csv
df_results.to_csv('trees_per_station_area.csv', index=True)
