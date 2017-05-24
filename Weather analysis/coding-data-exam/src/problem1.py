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
    return dataframe
result = []
for wf in os.listdir(os.path.join('..','wx_data')):
    df = get_dataframe(wf)
    count = df[(df['precipitation']=='-9999') & (df['maximum_temp']!='-9999') & (df['minimu_temp']!="-9999")].count()['date']
    result.append("{0}\t{1}".format(wf,count))
    result.sort()
data_required = "\n".join(result)
output_path = os.path.join('..','answers','MissingPrcpData.out')
f=open(output_path,'w')
f.write(data_required)
f.close()
