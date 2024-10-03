import json
import pandas as pd
data = json.load(open('by-gametype.json'))
df = pd.json_normalize(data, sep='_')
data_flat = df.to_dict(orient='records')[0]
df = pd.DataFrame(data_flat["items"])

for r in df['results']:
    print(r[0]['resultsJson'])