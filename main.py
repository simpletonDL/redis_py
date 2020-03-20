import pandas as pd

cpu1 = pd.read_csv('results/time_info_cpu1.csv')
cpu4 = pd.read_csv('results/time_info_cpu4.csv')

res: pd.DataFrame = pd.merge(cpu1, cpu4, how='outer', on=['graph', 'grammar', 'constrol_sum'])

# for _, raw in res.iterrows():
#     print()
res.sort_values(['grammar', 'graph'], inplace=True)
print(res)
res.to_csv('common_result.csv', index=False,
           columns=['graph', 'grammar', 'constrol_sum', 'time_cpu1', 'time_cpu4_index', 'time_cpu4_total'])
