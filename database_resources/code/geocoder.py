from geopy.geocoders import ArcGIS

df = pd.read_pickle('./database_resources/data/alldata_va_dc.pkl')

# Initiate Geocoding:
# Geocoder instance = 1 row per second:
arcgis = ArcGIS(timeout=1)

def geocoder(address):
    return arcgis.geocode(address)[-1]

# Geocoding Utility: adjust range parameters for writing 500 row pkl files with the 500 row window on DataFrame:

for i in range(2500,500_000,500):
    print('working -->')
    dfcode = df.iloc[i:i+500].copy()
    dfcode['lat_long'] = dfcode['full_address'].map(geocoder)
    dfcode.to_pickle(f'./database_resources/data/{i}_row_count_geocoded_STATES.pkl')
    print(f'{i} done: next batch of 500 -->')

# Read in geocded for final export to remote Database:
# arrange for loop for concatenation of separate files, f string etc.

# df_3501 = pd.read_pickle('./database_resources/data/full_3501_row_count_geocoded_va.pkl')
# df_4000 = pd.read_pickle('./database_resources/data/4000_row_count_geocoded_va.pkl')
# df_4500 = pd.read_pickle('./database_resources/data/4500_row_count_geocoded_va.pkl')
# df_5000 = pd.read_pickle('./database_resources/data/5000_row_count_geocoded_va.pkl')
# df_5500 = pd.read_pickle('./database_resources/data/5500_row_count_geocoded_va.pkl')
# df_6000 = pd.read_pickle('./database_resources/data/6000_row_count_geocoded_va.pkl')
# df_6500 = pd.read_pickle('./database_resources/data/6500_row_count_geocoded_va.pkl')
# df_7000 = pd.read_pickle('./database_resources/data/7000_row_count_geocoded_va.pkl')
# df_7500 = pd.read_pickle('./database_resources/data/7500_row_count_geocoded_va.pkl')
# df_8000 = pd.read_pickle('./database_resources/data/8000_row_count_geocoded_va.pkl')
# df_8500 = pd.read_pickle('./database_resources/data/8500_row_count_geocoded_va.pkl')
# df_9000 = pd.read_pickle('./database_resources/data/9000_row_count_geocoded_va.pkl')

# df_0 = pd.read_pickle('./database_resources/data/0_row_count_geocoded_STATES.pkl')
# df_500 = pd.read_pickle('./database_resources/data/500_row_count_geocoded_STATES.pkl')
# df_1000 = pd.read_pickle('./database_resources/data/1000_row_count_geocoded_STATES.pkl')
# df_1500 = pd.read_pickle('./database_resources/data/1500_row_count_geocoded_STATES.pkl')
# df_2000 = pd.read_pickle('./database_resources/data/2000_row_count_geocoded_STATES.pkl')

# df_new = pd.concat([df_0,df_500,df_1000,df_1500,df_2000])
# df = pd.concat([df_3501,df_4000,df_4500,df_5000,df_5500,df_6000,df_6500,df_7000,df_7500,df_8000,df_8500,df_9000])

# df_new.to_pickle('./database_resources/data/2500_row_count_geocoded_DC.pkl')
# df.to_json('./database_resources/data/loan_data_TEST.json',orient='records')