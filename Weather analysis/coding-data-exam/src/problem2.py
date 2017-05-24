import datetime
import os
import pandas as pd
def get_dataframe(file_name):
    columns=['date','maximum_temp','minimu_temp','precipitation']
    file_path = os.path.join('..',"wx_data",file_name)
    data = open(file_path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    return dataframe[(dataframe['precipitation']!='-9999') & 
                     (dataframe['maximum_temp']!='-9999') & 
                     (dataframe['minimu_temp']!="-9999")]
    
result = []
for wf in os.listdir(os.path.join('..','wx_data')):
    df = get_dataframe(wf)
    df['date'] = map(lambda x:datetime.datetime.fromtimestamp(float(x)),df['date'])
    df['year'] = map(lambda x:df['date'].ix[x].year,df.index)
    df['maximum_temp']=map(float,df['maximum_temp'].values)
    df['minimu_temp']=map(float,df['minimu_temp'].values)
    df['precipitation']=map(float,df['precipitation'].values)
    mean = df.groupby('year').mean()
    total = df.groupby('year').sum()
    maximutemp_mean  = mean['maximum_temp']
    minimutemp_mean = mean['minimu_temp']
    total_precipitation = total['precipitation']
    result.append("{0}\t{1}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(wf,
                                                              total_precipitation.index[0],
                                                              maximutemp_mean.values[0],
                                                              minimutemp_mean.values[0],
                                                             total_precipitation.values[0]))
                                                                                                                                            
result = map(lambda x:x+"\n",result)
f=open(os.path.join('..','answers','YearlyAverages.out'),'w')
f.writelines(result)
f.close()