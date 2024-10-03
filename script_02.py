import json
import pandas as pd
data = json.load(open('by-gametype.json'))
df = pd.json_normalize(data, sep='_')
data_flat = df.to_dict(orient='records')[0]
df = pd.DataFrame(data_flat["items"])

def flatten(d):
    res = []  # type:list  # Result list
    if isinstance(d, dict):
        for key, val in d.items():
            res.extend(flatten(val))
    elif isinstance(d, list):
        for val in d:
            res.extend(flatten(val))
    elif isinstance(d, (float, str, int)):
        res = [d]  # type: #List[float] or List[str] or List[int]
    else:
        raise TypeError("Undefined type for flatten: %s" % type(data))
    return res

print(flatten(df))
print()