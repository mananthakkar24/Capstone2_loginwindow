import pandas as pd
file_location = "https://api.covid19india.org/csv/latest/state_wise.csv"
file_data = pd.read_csv(file_location)
mh = file_data.loc[file_data['State'] == "Maharashtra"]
dl = file_data.loc[file_data['State'] == "Delhi"]
rj = file_data.loc[file_data['State'] == "Rajasthan"]
kt = file_data.loc[file_data['State'] == "Karnataka"]
tn = file_data.loc[file_data['State'] == "Tamil Nadu"]
up = file_data.loc[file_data['State'] == "Uttar Pradesh"]

mh1 = mh['Active'].values.tolist()
dl1 = dl['Active'].values.tolist()
rj1 = rj['Active'].values.tolist()
kt1 = kt['Active'].values.tolist()
tn1 = tn['Active'].values.tolist()
up1 = up['Active'].values.tolist()

d2 = file_data['State'].values.tolist()
print(d2)