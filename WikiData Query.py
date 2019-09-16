#import dependencies
import pandas as pd
import re
import numpy as np

# ## Get Wikidata Data and save to df

# #### Saving the publication Date
# insightful information on np datetime format
# https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
# - pandas datetime format pd.to_datetime is based on the np datetime64[ns] format which encodes dates from [ 1678 AD, 2262 AD]
# - it might be possible to use a different np datetime format with another base in order to save dates with a broader range
# - e.g.  h	Hour	± 1.0e15 years	[1.0e15 BC, 1.0e15 AD]
# - np.datetime64('2015-07-04 12:59:59.50', 'ns')

import requests

# Start Wikidata SPARQL Query
url = "https://query.wikidata.org/sparql"
query = """

SELECT ?book ?bookLabel ?publicationDate ?author ?authorLabel

WHERE
{
  {?book wdt:P31 wd:Q571 } UNION {?book wdt:P31 wd:Q7725634} UNION {?book wdt:P31 wd:Q8261} UNION {?book wdt:P31 wd:Q47461344}.
  ?book wdt:P577 ?publicationDate . 
  ?book wdt:P50 ?author .  

  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""
r = requests.get(url, params = {"format": "json", "query": query})
print(r)

data = r.json()

from collections import OrderedDict

countries = []
for item in data['results']['bindings']:
    countries.append(OrderedDict({
        'book': item['bookLabel']['value'],
        'publicationDate': item['publicationDate']['value'],
        'author': item['authorLabel']['value'] 
            if 'author' in item else None}))

df_wd = pd.DataFrame(countries)
df_wd = df_wd.astype({'book':str,'publicationDate': str, 'author': str})


#delete rows with non date values 
patternDel = 't\d*'
filter = df_wd['publicationDate'].str.contains(patternDel)
df_wd = df_wd[~filter]

#publicationdate to datetime format
array = np.array(df_wd["publicationDate"], dtype='datetime64[D]')
#convert to string for pandas handling
time_str = array.astype(str).tolist()
df_wd.publicationDate = time_str



#save wikidata data to csv
df_wd.to_csv("TARGET_DIRECTORY/WikiData_Query.csv")

