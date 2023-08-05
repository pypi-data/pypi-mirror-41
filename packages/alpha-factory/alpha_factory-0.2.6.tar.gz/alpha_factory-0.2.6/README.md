This programme is to automatically generate alpha factors and filter relatively good factors with back-testing methods

Dependencies
------------

- python >= 3.5
- pandas >= 0.22.0
- numpy >= 1.14.0
- RNWS >= 0.1.1
- numba >= 0.38.0
- single_factor_model>=0.3.0
- empyrical
- alphalens

Sample
------

# load packages and read in data

```python
from alpha_factory import generator_class,get_memory_use_pct,clean
from RNWS import read
import numpy as np
import pandas as pd
start=20180101
end=20180331
factor_path='.'
frame_path='.'

df=pd.read_csv(frame_path+'/frames.csv')

# read in data
re=read.read_df('./re',file_pattern='re',start=start,end=end)
cap=read.read_df('./cap',file_pattern='cap',header=0,dat_col='cap',start=start,end=end)
open_price,close,vwap,adj,high,low,volume,sus=read.read_df('./mkt_data',file_pattern='mkt',start=start,end=end,header=0,dat_col=['open','close','vwap','adjfactor','high','low','volume','sus'])
ind1,ind2,ind3=read.read_df('./ind',file_pattern='ind',start=start,end=end,header=0,dat_col=['level1','level2','level3'])
inx_weight=read.read_df('./ZZ800_weight','Stk_ZZ800',start=start,end=end,header=None,inx_col=1,dat_col=3)
```
Note:``frames`` contains columns as: `df_name,equation,dependency,type`,
where `type` includes `df,cap,group`.
In this case ``frames.csv`` have `df_name`: `re,cap,open_price,close,vwap,high,low,volume,ind1,ind2,ind3`

# start to generate 

``` python
parms={'re':close.mul(adj).pct_change()
       ,'cap':cap
       ,'open_price':open_price
       ,'close':close
       ,'vwap':vwap
       ,'high':high
       ,'low':low
       ,'volume':volume
       ,'ind1':ind1
       ,'ind2':ind2
       ,'ind3':ind3}

with generator_class(df,factor_path,**parms) as gen:
    gc.generator(batch_size=3,name_start='a')
    gc.generator(batch_size=3,name_start='a')
    gc.output_df(path=frame_path+'/frames_new.csv')
```

# continue to generate with existing frames and factors
```python
with generator_class(df,factor_path,**parms) as gc:
    gc.reload_df(path=frame_path+'/frames_new.csv')
    gc.reload_factors()
    clean()
    for i in range(5):
        gc.generator(batch_size=2,name_start='a')
        print('step %d memory usage:\t %.1f%% \n'%(i,get_memory_use_pct()))
        if get_memory_use_pct()>80:
            break
    gc.output_df(path=frame_path+'/frames_new2.csv')
```

# backtesting with stratified sampling approach and ic-ir meansure after generation
```python
data_box_param={'ind':ind1
            ,'price':vwap*adjfactor
            ,'sus':sus
            ,'ind_weight':inx_weight
            ,'path':'./databox'
            }

back_test_param={'sharpe_ratio_thresh':3
                 ,'n':5
                 ,'out_path':'.'
                 ,'back_end':'loky'
                 ,'n_jobs':6
                 ,'detail_root_path':None
                 ,'double_side_cost':0.003
                 ,'rf':0.03
                 }

icir_param={'ir_thresh':1
            ,'out_path':'.'
            ,'back_end':'loky'
            ,'n_jobs':6
            }

with generator_class(df,factor_path,**parms) as gen: 
    for i in range(5):
        gen.generator(batch_size=2,name_start='a')
        gen.output_df(path=frame_path+'/frames_new.csv')
        gen.getOrCreate_databox(**data_box_param)
        gen.back_test(**back_test_param)
        gen.icir(**icir_param)
        clean()
        if get_memory_use_pct()>90:
            print('Memory exceeded')
            break
```

# generate script of factors
```python
from alpha_factory import write_file
import pandas as pd
df2=pd.read_csv(frame_path+'/frames_new.csv')
write_file(df2,'script.py')
```

# find a factor
```python
from alpha_factory.utilise import get_factor_path
factor_name='a0'
path=get_factor_path(factor_path,factor_name)
```
