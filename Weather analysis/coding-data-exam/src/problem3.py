import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
def get_dataframe(file_name):
    columns=['station','year','maximum_temp','minimu_temp','precipitation']
    file_path = os.path.join('..',"answers",file_name)
    data = open(file_path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    return dataframe[(dataframe['precipitation']!='-9999') & 
                     (dataframe['maximum_temp']!='-9999') & 
                     (dataframe['minimu_temp']!="-9999")]
    
df = get_dataframe('YearlyAverages.out')
df['maximum_temp']=map(float,df['maximum_temp'].values)
df['minimu_temp']=map(float,df['minimu_temp'].values)
df['precipitation']=map(float,df['precipitation'].values)
max_temp = df['maximum_temp'].max()
min_temp = df['minimu_temp'].min() 
total_per = df['precipitation'].max()
data_maximum_temp = df[df['maximum_temp']==max_temp]
data_minimu_temp = df[df['minimu_temp']==min_temp]
data_total_per = df[df['precipitation'] == total_per]
data_maximum_temp = data_maximum_temp.append(data_minimu_temp,ignore_index=True)
data_maximum_temp = data_maximum_temp.append(data_total_per,ignore_index=True)
result = data_maximum_temp.groupby('year').count()
result[['maximum_temp','minimu_temp','precipitation']].plot(kind="bar",stacked=True)
plt.savefig(os.path.join('..','answers','YearHistogram.png'))
plt.show()
file_data = []
for year in result.index:
	max_count = result['maximum_temp'].ix[year]
	min_count = result['minimu_temp'].ix[year]
	totalpre_count = result['precipitation'].ix[year]
	file_data.append("{0}\t{1}\t{2}\t{3}\n".format(year,max_count,min_count,totalpre_count))
f=open(os.path.join('..','answers','YearHistogram.out'),'w')
f.writelines(file_data)
f.close()
                                                                                             