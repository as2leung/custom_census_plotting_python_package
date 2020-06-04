import pandas as pd
import seaborn as sns
from IPython.core.display import display, HTML
from copy import copy
import numpy as np


#Function 1 -  control totals function that aggregates survey values nationally, regionally and provincially. The totals are all returned in one table with 
#a "GEO" column indicating the level of geography

# 1) df_input: input data frame with Geography field and then column variables from survey
# 2) geo_field: DA code field/phhd code field

def control_totals(df_input,geo_field='CODE'):
    
    if df_input[geo_field].dtype =='int64':
        df_input[geo_field] = df_input[geo_field].astype(str)
    
    if 'PR' not in df_input.columns:
        df_input["PR"]=df_input.CODE.str[:2]
    
    if 'Region' not in df_input.columns:
        df_input["Region"]=df_input.CODE.str[:1]
    
    full = list(df_input)
    nat_cols = [e for e in full if e not in (geo_field,"Region","PR")]
    pr_cols = [e for e in full if e not in (geo_field,"Region")]
    reg_cols = [e for e in full if e not in (geo_field,"PR")]
    
    
    #nat_tot
    natdf = df_input[nat_cols].sum().reset_index()
    natdf.columns=['vars','values']
    natdf2 = pd.pivot_table(natdf,values='values', columns=['vars'], aggfunc=np.sum).reset_index().rename_axis(None, axis=1)
    natdf2.rename(columns={'index':'GEO'}, inplace=True)
    natdf2["GEO"]= natdf2["GEO"]=1
    
    #region totals
    region_tot = df_input[reg_cols].groupby(["Region"]).sum().reset_index()
    region_tot.rename(columns={'Region':'GEO'}, inplace=True)
    
    #provincial totals
    
    pr_tot  = df_input[pr_cols].groupby(["PR"]).sum().reset_index()
    pr_tot.rename(columns={'PR':'GEO'}, inplace=True)    
    
    final_df = pd.concat([natdf2,region_tot,pr_tot],axis=0, sort=True).reset_index()
    
    nat_cols.insert(0,"GEO")
    
    final_df = final_df[nat_cols]
    return final_df


#Function 2 -  Control totals from function 1 are used as an input to create relative values which are the variable divided by a universe denominator
# specified by the user. The parameters are as follows:

# 1) df_agg: The dataframe ouputted from function 1
# 2) universe: The variable name which has thhe universe denominator
# 3) abs_col_name: Column which to use as the numerators
# 4) rel_col_name: Name for new column housing 

def relative_values(df_agg, universe, abs_col_name, rel_col_name):
    nat = df_agg.iloc[:1]
    reg = df_agg.iloc[1:7]
    
    nat.drop(columns="GEO", inplace = True)
    nat = nat.melt()
    uni_val = nat.loc[nat["variable"]=="{}".format(universe),["value"]].values[0][0]
    nat["{}".format(rel_col_name)]= nat["value"].apply(lambda x: x/uni_val)
    nat.rename(columns={'value':abs_col_name}, inplace=True)
    
    #regional
    
    reg.rename(columns={'GEO':'Region'}, inplace=True)
    reg = reg.melt(id_vars=['Region'])
    reg_tot={}
    for i in range(1,len(reg.Region.drop_duplicates())+1):
        reg_tot[str(i)] = reg.loc[(reg['Region']==str(i))&(reg["variable"]==universe),["value"]].values[0][0]

    reg_tot

    reg["Universe"]= reg.Region.map(reg_tot)

    reg[rel_col_name] = reg["value"]/reg["Universe"]

    reg.drop(columns=["Universe"],inplace=True)

    reg.rename(columns={'value':abs_col_name}, inplace =True)

    
    return nat, reg


#Function 2a - for 1 to 5 geographies
def relative_values2(df_agg, universe, abs_col_name, rel_col_name):
    nat = df_agg.iloc[:1]
    reg = df_agg.iloc[1:6]
    
    nat.drop(columns="GEO", inplace = True)
    nat = nat.melt()
    uni_val = nat.loc[nat["variable"]=="{}".format(universe),["value"]].values[0][0]
    nat["{}".format(rel_col_name)]= nat["value"].apply(lambda x: x/uni_val)
    nat.rename(columns={'value':abs_col_name}, inplace=True)
    
    #regional
    
    reg.rename(columns={'GEO':'Region'}, inplace=True)
    reg = reg.melt(id_vars=['Region'])
    reg_tot={}
    for i in range(1,len(reg.Region.drop_duplicates())+1):
        reg_tot[str(i)] = reg.loc[(reg['Region']==str(i))&(reg["variable"]==universe),["value"]].values[0][0]

    reg_tot

    reg["Universe"]= reg.Region.map(reg_tot)

    reg[rel_col_name] = reg["value"]/reg["Universe"]

    reg.drop(columns=["Universe"],inplace=True)

    reg.rename(columns={'value':abs_col_name}, inplace =True)

    
    return nat, reg


# Function 3 -  control totals version using a dask dataframe
def ddcontrol_totals(df_input,geo_field='CODE'):

    
    if df_input[geo_field].dtype =='int64':
        df_input[geo_field] = df_input[geo_field].astype(str)
    
    if 'PR' not in df_input.columns:
        df_input["PR"]=df_input.CODE.str[:2]
    
    if 'Region' not in df_input.columns:
        df_input["Region"]=df_input.CODE.str[:1]
    
    full = list(df_input.columns.values)
    nat_cols = [e for e in full if e not in (geo_field,"Region","PR")]
    pr_cols = [e for e in full if e not in (geo_field,"Region")]
    reg_cols = [e for e in full if e not in (geo_field,"PR")]
    
    
    #nat_tot
    natdf = df_input[nat_cols].sum().reset_index().compute()
    natdf.columns=['vars','values']
    natdf2 = pd.pivot_table(natdf,values='values', columns=['vars'], aggfunc=np.sum).reset_index().rename_axis(None, axis=1)
  
    natdf2.rename(columns={'index':'GEO'}, inplace=True)
    natdf2["GEO"]= natdf2["GEO"]=1
    
        
    #region totals
    region_tot = df_input[reg_cols].groupby(["Region"]).sum().reset_index().compute()
    region_tot.rename(columns={'Region':'GEO'}, inplace=True)
    
    #provincial totals
    
    pr_tot  = df_input[pr_cols].groupby(["PR"]).sum().reset_index().compute()
    pr_tot.rename(columns={'PR':'GEO'}, inplace=True)    
    
    final_df = pd.concat([natdf2,region_tot,pr_tot],axis=0, sort=True).reset_index()
    
    nat_cols.insert(0,"GEO")
    
    final_df = final_df[nat_cols]
    return final_df
