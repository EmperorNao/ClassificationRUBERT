import pandas as pd

df = pd.read_excel("Razmechennaya_vygruzka.xlsx")
old_info = pd.read_csv('All_good_data(lemmatization).csv')
del df['Unnamed: 0']
del df['Unnamed: 0.1']
del old_info['Unnamed: 0']
del old_info['Unnamed: 0.1']
new_data_razm = pd.DataFrame()
for i in range(0, len(df)):

    row = old_info[old_info['entity_id'] == df['entity_id'].loc[i]]
    new_data_razm = new_data_razm.append(row)

new_data_razm = new_data_razm.reset_index()
new_data_razm['Lie'] = df['Lie']
new_data_razm.to_excel('Razmetka_ready.xlsx')

