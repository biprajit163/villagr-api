# Import Libraries:
import numpy as np
import pandas as pd

# Functions for Identifying How far a Customer's Patronage Supports Pandemic Business Recovery:

def zip_ranker(num):
    if num < 0.25:
        num = 'Village Friend: Making a Difference in this Zip'
        return num
    elif num >= 0.25 and num < 0.5:
        num = 'Village Benefactor: You\'re Making a Lasting Impact in this Zip'
        return num
    elif num >= 0.5 and num < 0.75:
        num = 'Village Patron: Your Impact is Going a Long Way in this Zip'
        return num
    elif num >= 0.75:
        num = 'Village Champ: Highest and Lasting Impact from Your Support in this Zip'
        return num
    else:
        num = 'Village Friend: Making a Difference in this Zip'
        return num
    
def type_ranker(num):
    if num < 0.25:
        num = 'Friend of the Business: Making a Difference for this Type'
        return num
    elif num >= 0.25 and num < 0.5:
        num = 'One of the Regulars: You\'re Making a Lasting Impact for this Type'
        return num
    elif num >= 0.5 and num < 0.75:
        num = 'Planting Roots: Your Impact is Going a Long Way for this Type'
        return num
    elif num >= 0.75:
        num = 'Business Partner: Highest and Lasting Impact from Your Support for this Type'
        return num
    else:
        num = 'Friend of the Business: Making a Difference for this Type'
        return num
    
def city_ranker(num):
    if num < 0.25:
        num = 'Friend of the City: Making a Difference in the Community'
        return num
    elif num >= 0.25 and num < 0.5:
        num = 'Locally Known: You\'re Making a Lasting Impact in the Community'
        return num
    elif num >= 0.5 and num < 0.75:
        num = 'Home Grown: Your Impact is Going a Long Way in the Community'
        return num
    elif num >= 0.75:
        num = 'Key to the City: Highest and Lasting Impact in the Community'
        return num
    else:
        num = 'Friend of the City: Making a Difference in the Community'
        return num
    
def full_loan_ranker(num):
    if num < 0.25:
        num = 'Village Friend: Making a Big Difference'
        return num
    elif num >= 0.25 and num < 0.5:
        num = 'Village Benefactor: Your Making a Lasting Impact'
        return num
    elif num >= 0.5 and num < 0.75:
        num = 'Village Patron: Your Impact is Going a Long Way in this Zip'
        return num
    elif num >= 0.75:
        num = 'Village Champ: Highest and Lasting Impact from Your Support'
        return num
    else:
        num = 'Village Friend: Making a Big Difference'
        return num

def title_maker(name):
    name = name.title().strip()
    return name

# Local data stored as pickle file after web retrieval:
df = pd.read_pickle('./database_resources/data/full_raw_data.pkl')

# select relevant features:
df = df[['AWARDEEORRECIPIENTLEGALENTITYNAME','LEGALENTITYADDRLINE1','LEGALENTITYCITYNAME',
         'LEGALENTITYSTATECD','LEGALENTITYZIP5','LEGALENTITYZIPLAST4','LEGALENTITYCONGRESSIONALDISTRICT',
        'BUSINESSTYPES','FACEVALUEOFDIRECTLOANORLOANGUARANTEE','ORIGINALLOANSUBSIDYCOST']].copy()

df.dropna(inplace=True)

# rename columns:
col_names = {'AWARDEEORRECIPIENTLEGALENTITYNAME':'business_name',
            'LEGALENTITYADDRLINE1':'street_address',
             'LEGALENTITYCITYNAME':'city',
             'LEGALENTITYSTATECD':'state',
            'LEGALENTITYZIP5':'zip_code_first5',
            'LEGALENTITYZIPLAST4':'zip_code_last4',
            'LEGALENTITYCONGRESSIONALDISTRICT':'congressional_district',
            'BUSINESSTYPES':'business_type',
            'FACEVALUEOFDIRECTLOANORLOANGUARANTEE':'loan_amount',
            'ORIGINALLOANSUBSIDYCOST':'loan_net_proceeds_UNSURE'}

df.rename(columns=col_names,inplace=True)

# Alternate DataFrame with selection of States:
df_states = df[(df['state'] == 'DC') | (df['state'] == 'IL') | (df['state'] == 'ID') | (df['state'] == 'PA') | (df['state'] == 'NJ') | (df['state'] == 'OH') | (df['state'] == 'MI')].copy()

df.reset_index(inplace=True)
df_states.reset_index(inplace=True)
df.drop(columns='index',inplace=True)
df_states.drop(columns='index',inplace=True)

# Virginia Option
# df_va = df[df['state'] == 'VA'].copy()
# df.reset_index(inplace=True)
# df_va.reset_index(inplace=True)
# df_states.reset_index(inplace=True)
# df_va.drop(columns=['index'],inplace=True)

df['zip_code_first5'] = df['zip_code_first5'].astype(str)
df['full_address'] = df['street_address'] + ', ' + df['city'] + ', ' + df['state'] + ' ' + df['zip_code_first5'] + ' USA'

df_new = df_states.sort_values('state').reset_index().copy()
df.reset_index(inplace=True)
df_new.reset_index(inplace=True)
df.drop(columns=['level_0','index'],inplace=True)
df_new.drop(columns='index',inplace=True)

df['business_name'] = df['business_name'].map(title_maker)
df['street_address'] = df['street_address'].map(title_maker)
df['city'] = df['city'].map(title_maker)
df['full_address'] = df['full_address'].map(title_maker)

df_new['zip_code_first5'] = df_new['zip_code_first5'].astype(str)
df_new['full_address'] = df_new['street_address'] + ', ' + df_new['city'] + ', ' + df_new['state'] + ' ' + df_new['zip_code_first5'] + ' USA'
df_new['business_name'] = df_new['business_name'].map(title_maker)
df_new['street_address'] = df_new['street_address'].map(title_maker)
df_new['city'] = df_new['city'].map(title_maker)
df_new['full_address'] = df_new['full_address'].map(title_maker)

df['loan_size_rank_by_state'] = df['loan_amount'].rank(pct=True)
df['loan_amount_by_zip_percentile'] = df.groupby('zip_code_first5')[['loan_amount']].rank(pct=True)
df['loan_amount_by_type_percentile'] = df.groupby('business_type')[['loan_amount']].rank(pct=True)
df['loan_amount_by_city_percentile'] = df.groupby('city')[['loan_amount']].rank(pct=True)

df['zipcode_urgency'] = df['loan_amount_by_zip_percentile'].apply(zip_ranker)
df['type_urgency'] = df['loan_amount_by_type_percentile'].apply(type_ranker)
df['city_urgency'] = df['loan_amount_by_city_percentile'].apply(city_ranker)
df['loan_size_urgency'] = df['loan_size_rank_by_state'].apply(full_loan_ranker)

df_new['loan_size_rank_by_state'] = df_new['loan_amount'].rank(pct=True)
df_new['loan_amount_by_zip_percentile'] = df_new.groupby('zip_code_first5')[['loan_amount']].rank(pct=True)
df_new['loan_amount_by_type_percentile'] = df_new.groupby('business_type')[['loan_amount']].rank(pct=True)
df_new['loan_amount_by_city_percentile'] = df_new.groupby('city')[['loan_amount']].rank(pct=True)

df_new['zipcode_urgency'] = df_new['loan_amount_by_zip_percentile'].apply(zip_ranker)
df_new['type_urgency'] = df_new['loan_amount_by_type_percentile'].apply(type_ranker)
df_new['city_urgency'] = df_new['loan_amount_by_city_percentile'].apply(city_ranker)
df_new['loan_size_urgency'] = df_new['loan_size_rank_by_state'].apply(full_loan_ranker)

df_vadc = pd.concat([df_va,df_new]).drop_duplicates()

# Export for geocoding:
# df_vadc.to_json('./database_resources/data/alldata_va_dc.json',orient='records')
# df_vadc.to_pickle('./database_resources/data/alldata_va_dc.pkl',orient='records')