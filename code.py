# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(mapper={'Total':'Total_Medals'},axis=1,inplace=True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter'))
better_event = data['Better_Event'].value_counts(
    ascending=False).index[0]
print(data['Better_Event'].head())
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
lastRow = len(top_countries)-1
top_countries.drop(index=lastRow,inplace=True)

def top_ten(df,col):
    country_list = list(df.nlargest(n=10,columns=col)['Country_Name'])
    return country_list
top_10_summer,top_10_winter,top_10=top_ten(top_countries,'Total_Summer'),top_ten(top_countries,'Total_Winter'),top_ten(top_countries,'Total_Medals')
common=[]
for country in top_10:
    if (country in top_10_summer) and (country in top_10_winter):
        common.append(country)
print(common)




# --------------
#Code starts here
import matplotlib.pyplot as plt
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

fig, (ax1,ax2,ax3)=plt.subplots(3,1,figsize=(14,21))
fig.tight_layout(pad=3.0)
plt.setp(ax1.get_xticklabels(), rotation=30)
plt.setp(ax2.get_xticklabels(), rotation=30)
plt.setp(ax3.get_xticklabels(), rotation=30)
summer_df.plot(x='Country_Name',y='Total_Summer',kind='bar',ax=ax1)
ax1.set_title('Total Summer Medals')
ax1.set_xlabel('Country Name')
ax1.set_ylabel('Medals count')
winter_df.plot(x='Country_Name',y='Total_Winter',kind='bar',ax=ax2)
ax2.set_title('Total Winter Medals')
ax2.set_xlabel('Country Name')
ax2.set_ylabel('Medals count')
top_df.plot(x='Country_Name',y='Total_Medals',kind='bar',ax=ax3)
ax3.set_title('Total Medals')
ax3.set_xlabel('Country Name')
ax3.set_ylabel('Medals count')


# --------------
#Code starts here
summer_df['Golden_Ratio']= summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].values[0]

winter_df['Golden_Ratio']= winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].values[0]

top_df['Golden_Ratio']= top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'].values[0]

print(summer_max_ratio,summer_country_gold)
print(winter_max_ratio,winter_country_gold)
print(top_max_ratio,top_country_gold)





# --------------
#Code starts here
data_1 = data.drop(index=len(data)-1)
data_1['Total_Points'] = 3*data_1['Gold_Total']+2*data_1['Silver_Total']+data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points']==most_points]['Country_Name'].values[0]
print(most_points,best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


