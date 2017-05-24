import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def get_dataframe(file_name):
    columns=['station','year','maximum_temp','minimu_temp','precipitation']
    file_path = os.path.join('..',"answers",file_name)
    data = open(file_path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    dataframe = dataframe[(dataframe['precipitation']!=-9999) & 
                     (dataframe['maximum_temp']!=-9999) & 
                     (dataframe['minimu_temp']!=-9999)]
    dataframe['maximum_temp']=map(float,dataframe['maximum_temp'].values)
    dataframe['minimu_temp']=map(float,dataframe['minimu_temp'].values)
    dataframe['precipitation']=map(float,dataframe['precipitation'].values)
    dataframe['sq_maximum_temp'] = dataframe['maximum_temp']**2
    dataframe['sq_minimu_temp'] = dataframe['minimu_temp']**2
    dataframe['sq_precipitation'] = dataframe['precipitation']**2
    dataframe['p_maximum_temp_minimu_temp'] = dataframe['maximum_temp']*dataframe['minimu_temp']
    dataframe['p_minimu_temp_precipitation'] = dataframe['minimu_temp']*dataframe['precipitation']
    dataframe['p_maximum_temp_precipitation'] = dataframe['maximum_temp']*dataframe['precipitation']
    return dataframe
    
df = get_dataframe('YearlyAverages.out')
df_group_year_sum = df.groupby("year").sum()
N = df.groupby("year").count()['maximum_temp']
sum_max_tmp= df_group_year_sum['maximum_temp']
sum_min_tmp = df_group_year_sum['minimu_temp']
sum_pre = df_group_year_sum['precipitation']
sum_p_max_min=df_group_year_sum['p_maximum_temp_minimu_temp']
sum_p_min_pre=df_group_year_sum['p_minimu_temp_precipitation']
sum_p_max_pre=df_group_year_sum['p_maximum_temp_precipitation']
sum_sq_max=df_group_year_sum['sq_maximum_temp']
sum_sq_min=df_group_year_sum['sq_minimu_temp']
sum_sq_pre=df_group_year_sum['sq_precipitation']
max_min_factor = []
min_pre_factor = []
max_pre_factor = []
for year in df_group_year_sum.index:
    fact_numerator = (N*sum_p_max_min.ix[year])-(sum_max_tmp.ix[year]*sum_min_tmp.ix[year])
    fact_denominator = np.sqrt(((N*sum_sq_max.ix[year])-(sum_max_tmp.ix[year]**2))*((N*sum_sq_min.ix[year])-(sum_min_tmp.ix[year]**2)))
    max_min_factor.append({year:"%.2f"%(fact_numerator/fact_denominator)})
    fact_numerator = (N*sum_p_min_pre.ix[year])-(sum_min_tmp.ix[year]*sum_pre.ix[year])
    fact_denominator = np.sqrt(((N*sum_sq_min.ix[year])-(sum_min_tmp.ix[year]**2))*((N*sum_sq_pre.ix[year])-(sum_pre.ix[year]**2)))
    min_pre_factor.append({year:"%.2f"%(fact_numerator/fact_denominator)})
    fact_numerator = (N*sum_p_max_pre.ix[year])-(sum_max_tmp.ix[year]*sum_pre.ix[year])
    fact_denominator = np.sqrt(((N*sum_sq_max.ix[year])-(sum_max_tmp.ix[year]**2))*((N*sum_sq_pre.ix[year])-(sum_pre.ix[year]**2)))
    max_pre_factor.append({year:"%.2f"%(fact_numerator/fact_denominator)})
f=open(os.path.join('..','answers','Correlations.out'),'w')
f.write("year\tmax_min_factor\tmin_pre_factor\tmax_pre_factor\n")
for year,max_min,min_pre,max_pre in zip(df_group_year_sum.index,max_min_factor,min_pre_factor,max_pre_factor):
    f.write("{0}\t{1}\t{2}\t{3}\n".format(year,max_min[year],min_pre[year],max_pre[year]))
f.close()


                                                                                             