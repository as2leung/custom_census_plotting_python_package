
# %% GLOBAL PACKAGE IMPORTS
###############################################################################
import pandas as pd
import time as time
import seaborn as sns
from matplotlib import pyplot as plt
import csv
from scipy import stats
import copy
import random as random
import matplotlib as mpl
import numpy as np
#%matplotlib inline
###############################################################################


# Function 1 - Create Scatterplots with 2 tables(dataframes) by providing one list of variables - same variable from each dataframe is used. Parameters are as follows:

# 1) lists: a list of variables that will be used for both dataframes
# 2) df_new: dataframe 1 - ideally a table from current year
# 3) df_old: dataframe 2 - ideally a table from previous year
# 4) Normalized: As a percentage distribution or non-normalized
# 5) Placements: Grouped bar plots, Split vertical facet, Line plot
# 6) Sample Size: Specify number of geography units to use




def one_df_scatter_cont3(lists,df_new,df_old, join_field, normalized=True, linear_trend=False):

    """ This is a module level function for generating Scatterplots from 2 tables(dataframes)
    by providing one list of variables. The same variables from each dataframe are plot against each other
    the most common use case to plot one vintage of var A against itself in another vintage (i.e. DS2018 vs DS2019)

    The length of the list corresponds to the number of scatterplots that will be generated


    Args:


    lists (:obj:`list` of :obj:`str`): a list of variables that will be used for plotting from both dataframes
    df_new (:obj:`str`): Name of dataframe 1 - ideally a table from current year
    df_old (:obj:`str`): Name of dataframe 2 - ideally a table from previous year
    normalized (:obj:`str`): String parameter to specify the output values as a percentage distribution or non-normalized (raw values)
    linear_trend (:obj:`str`): String parameter to specify
    

    Returns:


    """


    test=1
    try:
        var1 = lists[0]
        
    except:
        test=0
        print('we out')
        return False
    
    try:
        var2 = lists[0][1]
        
    except:
        test=0
        print('we out still')
        
    else:
        
        combined = df_new.merge(df_old, how='inner', left_on='{}'.format(join_field), right_on='{}'.format(join_field), suffixes=("_new","_old"))
        return combined
            
    finally:
        
        if normalized==True:
            if linear_trend==True:
                print('Add linear trend')

                for pairs in range(len(lists)):
                    x = lists[pairs]+"_new"
                    y = lists[pairs]+"_old"
                    combined[x] = combined[x]/combined[x].sum()*100
                    combined[y] = combined[y]/combined[y].sum()*100
                    f,ax = plt.subplots(figsize=(15,6))
                    r2 = stats.pearsonr(combined[x],combined[y])[0]**2
                    r2= r2.round(2)
                    r2a = stats.pearsonr(combined[x],combined[y])[1]
                    r2a = r2a.round(2)
                    sns.scatterplot(x=x,y=y,data = combined, ax=ax)#, ax=ax[pairs][1])
                    sns.regplot(x=x,y=y,data = combined,scatter_kws={'alpha':0.03})
                    #set title
                    print("\n\n\n\n")
                    plt.suptitle('Scatter of {} vs {}'.format(x,y),fontsize=18, ha='center')
                    plt.title('R-Squared: {}, P-value: {}'.format(r2, r2a),ha='center')
                    plt.show()

            else:

                print('No linear trend')
                for pairs in range(len(lists)):
                    x = lists[pairs]+"_new"
                    y = lists[pairs]+"_old"
                    combined[x] = combined[x]/combined[x].sum()*100
                    combined[y] = combined[y]/combined[y].sum()*100
                    f,ax = plt.subplots(figsize=(15,6))
                    r2 = stats.pearsonr(combined[x],combined[y])[0]**2
                    r2= r2.round(2)
                    r2a = stats.pearsonr(combined[x],combined[y])[1]
                    r2a = r2a.round(2)
                    sns.scatterplot(x=x,y=y,data = combined, ax=ax)#, ax=ax[pairs][1])
                    #sns.regplot(x=x,y=y,data = combined,scatter_kws={'alpha':0.03})
                    #set title
                    print("\n\n\n\n")
                    plt.suptitle('Scatter of {} vs {}'.format(x,y),fontsize=18, ha='center')
                    plt.title('R-Squared: {}, P-value: {}'.format(r2, r2a),ha='center')
                    plt.show()
        else:
            if linear_trend==True:
                print('Add linear trend')

                for pairs in range(len(lists)):
                    x = lists[pairs]+"_new"
                    y = lists[pairs]+"_old"
                    f,ax = plt.subplots(figsize=(15,6))
                    r2 = stats.pearsonr(combined[x],combined[y])[0]**2
                    r2= r2.round(2)
                    r2a = stats.pearsonr(combined[x],combined[y])[1]
                    r2a= r2a.round(2)
                    sns.scatterplot(x=x,y=y,data = combined, ax=ax)#, ax=ax[pairs][1])
                    sns.regplot(x=x,y=y,data = combined,scatter_kws={'alpha':0.03})
                    #set title
                    print("\n\n\n\n")
                    plt.suptitle('Scatter of {} vs {}'.format(x,y),fontsize=18, ha='center')
                    plt.title('R-Squared: {}, P-value: {}'.format(r2, r2a),ha='center')
                    plt.show()

            else:

                print('No linear trend')
                for pairs in range(len(lists)):
                    x = lists[pairs]+"_new"
                    y = lists[pairs]+"_old"
                    f,ax = plt.subplots(figsize=(15,6))
                    r2 = stats.pearsonr(combined[x],combined[y])[0]**2
                    r2= r2.round(2)
                    r2a = stats.pearsonr(combined[x],combined[y])[1]
                    r2a= r2a.round(2)
                    sns.scatterplot(x=x,y=y,data = combined, ax=ax)#, ax=ax[pairs][1])
                    #sns.regplot(x=x,y=y,data = combined,scatter_kws={'alpha':0.03})
                    #set title
                    print("\n\n\n\n")
                    plt.suptitle('Scatter of {} vs {}'.format(x,y),fontsize=18, ha='center')
                    plt.title('R-Squared: {}, P-value: {}'.format(r2, r2a),ha='center')
                    plt.show()
            
            

## Function 2 - Plotting function for distribution variables for two data frames. The variables from the two dataframes need to match as no list is requested
#from the user. This function takes a sample of geographies for comparison. There are also options for:

# 1) df_new: dataframe 1 - ideally a table from current year
# 2) df_old: dataframe 2 - ideally a table from previous year
# 3) Difference: Compute the difference in values between the variable in df_new and df_old. Can be normalized as well.
# 4) Normalized: As a percentage distribution or non-normalized
# 5) Placements: Grouped bar plots, Split vertical facet, Line plot
# 6) Sample Size: Specify number of geography units to use



def distrib_plot_v2(df_new,df_old,join_field, difference = False, normalized = False,
                 placement='grouped', sample_size=10):
    test=1
#     try:
#         var1 = lists[0]
        
#     except:
#         test=0
#         print('we out')
#         return False
    
#     try:
#         var2 = lists[0][1]
        
#     except:
#         test=0
#         print('we out still')
        
#     else:
        
    combined = df_new.merge(df_old, how='inner', left_on='{}'.format(join_field), right_on='{}'.format(join_field), suffixes=("_new","_old"))
    combined['CODE'] = combined['CODE'].astype(str)

            
#     finally:

    ######
    if normalized == False:
        
                      
        if difference == True:
            vars = list(df_old)
            vars.remove("CODE")
            vars

            df_diff = pd.DataFrame(df_old["CODE"])

            for var in vars:
                df_diff["diff_"+var] = df_new[var]-df_old[var]

            df_diff.dropna(inplace = True )
            df_diff['CODE'] = df_diff['CODE'].astype(str)

            Geo_list = list(combined.CODE)
            sub_set=[i for i in random.sample(Geo_list,sample_size)]
            final_df = df_diff[df_diff['CODE'].isin(sub_set)]
            sub_set.sort()
            #print(sub_set)
            display(final_df)



            for s in sub_set:

                final_df_t = pd.melt(final_df,id_vars=['CODE'])

                final_df_t = final_df_t[final_df_t['CODE']==s]
                print(final_df_t)

                g = sns.catplot(x="variable", y="value", data=final_df_t,height=10, kind="bar", palette="muted", aspect =1.3)

                g.set_xticklabels(rotation=30)

                ax = plt.gca()
                
                plt.title('{}'.format(s),ha='center')

                for p in ax.patches:
                    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), 
                            fontsize=10, color='black', ha='center', va='bottom')
                plt.show()
                
        else:
                             
            Geo_list = list(combined.CODE)
            sub_set=[i for i in random.sample(Geo_list,sample_size)]
            final_df = combined[combined['CODE'].isin(sub_set)]
            sub_set.sort()
            #print(sub_set)

            for s in sub_set:


                final_df_t = pd.melt(final_df,id_vars=['CODE'])

                final_df_t = final_df_t[final_df_t['CODE']==s]


                final_df_t['Flag']= final_df_t['variable'].apply(lambda x: x.split("_")[1])
                final_df_t['variable']= final_df_t['variable'].apply(lambda x: x.split("_")[0])

                


        

                display(final_df_t)


                if placement == "grouped":
                    g = sns.catplot(x="variable", y="value", hue="Flag", data=final_df_t, 
                                height=10, kind="bar", palette="muted", aspect =1.3)

                    ax = plt.gca()
                    
                    plt.title('{}'.format(s),ha='center')

                    for p in ax.patches:
                        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), 
                                fontsize=10, color='black', ha='center', va='bottom')
                    
                    plt.show()

                elif placement == "split":

                    g = sns.FacetGrid(final_df_t, row = "Flag", size=10, aspect=1.3)
                    g.map(sns.barplot, "variable", "value")

                    ax = plt.gca()
                    
                    plt.title('{}'.format(s),ha='center')

                    for p in ax.patches:
                        ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), 
                                fontsize=10, color='black', ha='center', va='bottom')
                    
                    plt.show()

                elif placement == "series":
                    plt.figure(figsize=(15,16)) 

                    g = sns.pointplot(x="variable", y="value", hue="Flag", data=final_df_t,
                                    height=10, kind="bar", palette="muted", aspect =1.3)


                    ax = plt.gca()
                    
                    plt.title('{}'.format(s),ha='center')

                    plt.show()

    elif normalized == True:


        if difference == True:
            vars = list(df_old)
            vars.remove("CODE")
            vars

            df_diff = pd.DataFrame(df_old["CODE"])

            for var in vars:
                df_diff["diff_"+var] = (df_new[var]-df_old[var])/df_new[var]*100

            df_diff.dropna(inplace = True )
            df_diff['CODE'] = df_diff['CODE'].astype(str)

            Geo_list = list(combined.CODE)
            sub_set=[i for i in random.sample(Geo_list,sample_size)]
            final_df = df_diff[df_diff['CODE'].isin(sub_set)]
            sub_set.sort()
            #(sub_set)
            display(final_df)



            for s in sub_set:

                final_df_t = pd.melt(final_df,id_vars=['CODE'])

                final_df_t = final_df_t[final_df_t['CODE']==s]
                print(final_df_t)

                g = sns.catplot(x="variable", y="value", data=final_df_t,height=10, kind="bar", palette="muted", aspect =1.3)

                g.set_xticklabels(rotation=30)

                ax = plt.gca()

                for p in ax.patches:
                    ax.text(p.get_x() + p.get_width()/2., p.get_height(), '%d' % int(p.get_height()), 
                            fontsize=10, color='black', ha='center', va='bottom')
                
                plt.show()

        else:

            Geo_list = list(combined.CODE)
            sub_set=[i for i in random.sample(Geo_list,2)]
            final_df = combined[combined['CODE'].isin(sub_set)]
            sub_set.sort()
            #print(sub_set)

            for s in sub_set:


                final_df_t = pd.melt(final_df,id_vars=['CODE'])

                final_df_t = final_df_t[final_df_t['CODE']==s]


                final_df_t['Flag']= final_df_t['variable'].apply(lambda x: x.split("_")[1])
                final_df_t['variable']= final_df_t['variable'].apply(lambda x: x.split("_")[0])
                
                             
                
                final_df_t = final_df_t.assign(normalized=final_df_t.value.div(final_df_t.Flag.map(final_df_t.groupby('Flag').value.sum()))*100)
                display(final_df_t)

                if placement == "grouped":

                    g = sns.catplot(x="variable", y="normalized", hue="Flag", data=final_df_t,
                                height=10, kind="bar", palette="muted", aspect =1.3)

                    ax = plt.gca()
                    
                    plt.title('{}'.format(s),ha='center')

                    for p in ax.patches:
                        for p in ax.patches:
                             ax.annotate(round(p.get_height(),3), (p.get_x() * 1.005, p.get_height() * 1.005), rotation=90 )
                    
                    plt.show()

                elif placement == "split":

                    g = sns.FacetGrid(final_df_t, row = "Flag", size=10, aspect=1.3)
                    g.map(sns.barplot, "variable", "normalized")

                    ax = plt.gca()
                    
                    plt.title('{}'.format(s),ha='center')

                    for p in ax.patches:
                        for p in ax.patches:
                             ax.annotate(round(p.get_height(),3), (p.get_x() * 1.005, p.get_height() * 1.005))
                    
                    plt.show()

                elif placement == "series":
                    plt.figure(figsize=(15,16)) 

                    g = sns.pointplot(x="variable", y="normalized", hue="Flag", data=final_df_t,
                                    height=10, kind="bar", palette="muted", aspect =1.3)


                    ax = plt.gca()
                    plt.title('{}'.format(s),ha='center')
                    
                    plt.show()

 


    
        
## Function 3 - Box plot and histogram function for two data frames with one list of variables provided. The same variables are used in each dataframe. Outliers are set to "False" by default
# as this allows a better view of the bulk of the values. The parameters are as follows:

# 1) lists: a list of variables that will be used for both dataframes
# 2) df_new: dataframe 1 - ideally a table from current year
# 3) df_old: dataframe 2 - ideally a table from previous year
# 4) join_field: The field on which the dataframes are joined - ideally the geography field. A list can be provided for joins based on multiple columns.
# 5) show_outliers: Outliers are omitted by default so that plots are zoomed to the bulk of the data. Can be turned on by providing "True" as an input value.


def box_n_hist_v2(lists,df_new,df_old,join_field, show_outliers=False):
    test=1
    try:
        var1 = lists[0]
        
    except:
        test=0
        print('we out')
        return False
    
    try:
        var2 = lists[0][1]
        
    except:
        test=0
        print('we out still')
        
    else:
        
        combined = df_new.merge(df_old, how='inner', left_on='{}'.format(join_field), right_on='{}'.format(join_field), suffixes=("_new","_old"))
        
            
    finally:
          
        display(combined)
        
        for pairs in range(len(lists)):
            x = lists[pairs]+"_new"
            y = lists[pairs]+"_old"
            final_df = combined[[join_field,x,y]]
            final_df_t = final_df.melt(id_vars=[join_field])
            #print(final_df_t)
            
            f,ax = plt.subplots(figsize=(15,6))
            sns.boxplot(x='variable', y='value', data = final_df_t, showfliers= show_outliers, ax=ax)#, ax=ax[pairs][1])
            
            plt.title('Boxplost of {} and {}'.format(x, y),ha='center')
            
            g = sns.FacetGrid(final_df_t, hue="variable", height=10, aspect=1.3)
#             g.map(plt.hist, "value", histtype='barstacked', stacked=True);
#             plt.legend();
            
            g.map(sns.distplot, "value", kde=False, norm_hist=False)
        
            plt.title('Histograms of {} and {}'.format(x, y),ha='center')
            plt.legend();
            
#             sns.distplot(final_df[x])
#             sns.distplot(final_df[y])
        
            plt.show()




### Function 4 - This function accepts distribution data that is normalized (tranposed). The function accepts the following parameters:

# 1) df - the dataframe with distributional data in normalized/transposed fromat
# 2) X - axis: The categorical breaks for the distribution (i.e. years, age groups, etc)
# 3) Y - axis: Numerical Values for plotting
# 4) Normalized: Plotting the values as percentages
# 5) Placement: Grouped bar plot, split vertical facet and line series can be specified
# 6) Subset: If there is an additional geography column where units can be sampled from, subset can be set to any string or value (i.e. 'yes')
## this enables a user input prompt that requests the numbers of sample units to take and then the fieldname from which to sample from.

def one_df_distrib_v2(df, x_axis, y_axis, series, normalized = True, placement="grouped", subset=None):
    
    if subset is not None:
        user_one = input ("Enter sample size number: ")
        sample_size = int(user_one)
        print("Sample size selected is: ", sample_size)
        
        user_two = input ("Enter field name for sampling (i.e. Geography field) with no qoutations: ")
        subset_field = user_two
        print("Field selected is: ", subset_field)
        
        Geo_list = list(df[subset_field])
        geo_set = set(Geo_list)
        final_list = list(geo_set)
        #print(geo_set)
        
        sub_set=[i for i in random.sample(final_list,sample_size)]
        final_df = df[df[subset_field].isin(sub_set)]
        sub_set.sort()
        display(sub_set)

        for s in sub_set:
            df = final_df[final_df[subset_field]==s]
            #print(df)

            if df[x_axis].dtype == object:

                if normalized == True:

                    df = df.assign(normalized = df[y_axis].div(df[series].map(df.groupby([series])[y_axis].sum())))
                    display(df)

                    if placement == 'grouped':

                        g = sns.catplot(x=x_axis, y="normalized", hue=series , data=df,
                                        height=10, kind="bar", palette="muted", aspect =1.3)

                        ax = plt.gca()
                        plt.show()
                        print("yess sirr")


                    elif placement == "series":
                        print("nah bruh")
                        plt.figure(figsize=(15,16)) 

                        g = sns.pointplot(x=x_axis, y="normalized", hue=series, data=df,
                                             palette="muted")
                        plt.show()

                elif normalized == False:


                    if placement == 'grouped':

                        g = sns.catplot(x=x_axis, y=y_axis, hue=series , data=df,
                                        height=10, kind="bar", palette="muted", aspect =1.3)

                        ax = plt.gca()
                        plt.show()
                        print("yess sirr")


                    elif placement == "series":
                        print("nah bruh")
                        plt.figure(figsize=(15,16)) 

                        g = sns.pointplot(x=x_axis, y=y_axis, hue=series, data=df,
                                             palette="muted")
                        plt.show()


            elif df[x_axis].dtype == int or float:

                if normalized == True:

                    df = df.assign(normalized = df[y_axis].div(df[series].map(df.groupby([series])[y_axis].sum())))
                    display(df.head())

                    if placement == 'grouped':
                        print("bars on bars")

                        g = sns.catplot(x=x_axis, y="normalized", hue=series, data=df, legend=False,
                                        height=10, kind="bar", palette="muted", aspect =1.3)

                        ax = plt.gca()
                        plt.show()


                    elif placement == "series":
                        print("lineplots for days")
                        plt.figure(figsize=(15,16)) 

                        g = sns.lineplot(x=x_axis, y="normalized",hue=series, data=df, legend=False)

                        plt.show()

                elif normalized == False:

                    if placement == 'grouped':
                        print("bars on bars")

                        g = sns.catplot(x=x_axis, y=y_axis, hue=series, data=df,
                                        height=10, kind="bar", palette="muted", aspect =1.3)

                        ax = plt.gca()
                        plt.show()


                    elif placement == "series":
                        print("lineplots for days")
                        plt.figure(figsize=(15,16)) 

                        g = sns.lineplot(x=x_axis, y=y_axis,hue=series, data=df, legend=False)

                        plt.show()


    else:

        if df[x_axis].dtype == object:

                if normalized == True:

                    df = df.assign(normalized = df[y_axis].div(df[series].map(df.groupby([series])[y_axis].sum())))
                    display(df.head())

                    if placement == 'grouped':

                        g = sns.catplot(x=x_axis, y="normalized", hue=series , data=df,
                                        height=10, kind="bar", palette="muted", aspect =1.3)

                        ax = plt.gca()
                        plt.show()
                        print("yess sirr")


                    elif placement == "series":
                        print("nah bruh")
                        plt.figure(figsize=(15,16)) 

                        g = sns.pointplot(x=x_axis, y="normalized", hue=series, data=df,
                                             palette="muted")
                        plt.show()

                elif normalized == False:


                    if placement == 'grouped':

                        g = sns.catplot(x=x_axis, y=y_axis, hue=series , data=df,
                                        height=10, kind="bar", palette="muted", aspect =1.3)

                        ax = plt.gca()
                        plt.show()
                        print("yess sirr")


                    elif placement == "series":
                        print("nah bruh")
                        plt.figure(figsize=(15,16)) 

                        g = sns.pointplot(x=x_axis, y=y_axis, hue=series, data=df,
                                             palette="muted")
                        plt.show()


        elif df[x_axis].dtype == int or float:

            if normalized == True:

                df = df.assign(normalized = df[y_axis].div(df[series].map(df.groupby([series])[y_axis].sum())))
                display(df.head())

                if placement == 'grouped':
                    print("bars on bars")

                    g = sns.catplot(x=x_axis, y="normalized", hue=series, data=df, legend=False,
                                    height=10, kind="bar", palette="muted", aspect =1.3)

                    ax = plt.gca()
                    plt.show()


                elif placement == "series":
                    print("lineplots for days")
                    plt.figure(figsize=(15,16)) 

                    g = sns.lineplot(x=x_axis, y="normalized",hue=series, data=df, legend=False)

                    plt.show()

            elif normalized == False:

                if placement == 'grouped':
                    print("bars on bars")

                    g = sns.catplot(x=x_axis, y=y_axis, hue=series, data=df,
                                    height=10, kind="bar", palette="muted", aspect =1.3)

                    ax = plt.gca()
                    plt.show()


                elif placement == "series":
                    print("lineplots for days")
                    plt.figure(figsize=(15,16)) 

                    g = sns.lineplot(x=x_axis, y=y_axis,hue=series, data=df, legend=False)

                    plt.show()

    

### Function 5 - this is alternate version of function 4 that eliminated normalization but provides pct diff, abs diff and cumulative values:

def one_df_distrib_v3(df, x_axis, y_axis, series, placement="grouped",output="raw", universe="", subset=None):
    
    pd.options.mode.chained_assignment = None
    if not universe =="":
        df = df[~(df[x_axis]==universe)]
                 
    #abs diff
    t = df.loc[:,[series,y_axis]].groupby(series).apply(lambda x: x.diff()).loc[:,y_axis]
    df['diff'] = t

    #percent diff
    df["pct_diff"]= df.groupby(series)[y_axis].apply(lambda x: x.diff()/x)


    #cumulative sum function by group
    df["cumulative"] = df.groupby(series)[y_axis].cumsum()
    
    
    allFigures=[]
    
    if subset is not None:
        user_one = input ("Enter sample size number: ")
        sample_size = int(user_one)
        print("Sample size selected is: ", sample_size)
        
        user_two = input ("Enter field name for sampling (i.e. Geography field) with no qoutations: ")
        subset_field = user_two
        print("Field selected is: ", subset_field)
        
        Geo_list = list(df[subset_field])
        geo_set = set(Geo_list)
        final_list = list(geo_set)
        #print(geo_set)
        
        sub_set=[i for i in random.sample(final_list,sample_size)]
        final_df = df[df[subset_field].isin(sub_set)]
        sub_set.sort()
        display(sub_set)

        for s in sub_set:
            df = final_df[final_df[subset_field]==s]
            #print(df)
        
              
   
            if df[x_axis].dtype == object:

                #create interval labels
                df["interval"]=df.groupby(series)[x_axis].transform(lambda x: x.shift(1) + "-" + x)
                display(df.head(15),df.tail(15))
                print(s,series,y_axis)

                if placement == "grouped":

                    if output== "raw":

                        g = sns.catplot(x=x_axis, y=y_axis, hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Raw Values - Bar Plot")



                    elif output == "abs_diff":

                        df = df.loc[~(df["interval"].isna()),]

                        g = sns.catplot(x="interval", y="diff", hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Absolute Difference Values - Bar Plot")



                    elif output == "pct_diff":

                        df = df[~(df["interval"].isna())]

                        g = sns.catplot(x="interval", y="pct_diff", hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Percentage Difference Values - Bar Plot")

                    elif output == "cumulative":

                        g = sns.catplot(x=x_axis, y="cumulative", hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Cumulative Values - Bar Plot")

                elif placement == "series":


                    if output== "raw":

                        print("Raw Values - lineplots")
                        plt.figure(figsize=(15,16)) 

                        g = sns.pointplot(x=x_axis, y=y_axis, hue=series, data=df,
                                             palette="muted")
                        plt.xticks(rotation=30)

                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()




                    elif output == "abs_diff":

                        print("Absolute Differences - lineplots")
                        plt.figure(figsize=(15,16))

                        df = df.loc[~(df["interval"].isna()),] 

                        g = sns.pointplot(x="interval", y="diff", hue=series, data=df,
                                             palette="muted")

                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()


                    elif output == "pct_diff":

                        print("Percentage Differences - lineplots")
                        plt.figure(figsize=(15,16))

                        df = df[~(df["interval"].isna())] 

                        g = sns.pointplot(x="interval", y="pct_diff", hue=series, data=df,
                                             palette="muted")

                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()



                    elif output == "cumulative":

                        print("Cumulative Values - lineplots")
                        plt.figure(figsize=(15,16)) 

                        g = sns.pointplot(x=x_axis, y="cumulative", hue=series, data=df,
                                             palette="muted")

                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()



            elif df[x_axis].dtype == int or float:

                #create interval labels
                df["interval"]=df.groupby(series)[x_axis].transform(lambda x: x.shift(1).astype(str) + "-" + x.astype(str))

                display(df.head(15))


                if placement == "grouped":

                    if output== "raw":

                        g = sns.catplot(x=x_axis, y=y_axis, hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Raw Values - Bar Plot")



                    elif output == "abs_diff":

                        df = df[~(df["interval"].isna())]

                        g = sns.catplot(x="interval", y="diff", hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Absolute Difference Values - Bar Plot")



                    elif output == "pct_diff":

                        df = df[~(df["interval"].isna())]

                        g = sns.catplot(x="interval", y="pct_diff", hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Percentage Difference Values - Bar Plot")

                    elif output == "cumulative":

                        g = sns.catplot(x=x_axis, y="cumulative", hue=series , data=df,
                        height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                        ax = plt.gca()


                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
                        print("Cumulative Values - Bar Plot")

                elif placement == "series":


                    if output== "raw":

                        dash_styles = [
                       (4, 1.5),
                       (1, 1),
                       (3, 1, 1.5, 1),
                       (5, 1, 1, 1),
                       (5, 1, 2, 1, 2, 1),
                       (2, 2, 3, 1.5),
                       (1, 2.5, 3, 1.2)]


                        plt.style.use('seaborn-whitegrid')

                        print("Raw Values - lineplots")
                        fig = plt.figure(figsize=(15,11)) 
                        fig.set_canvas(plt.gcf().canvas)

                        paper_rc = {'lines.linewidth': 5, 'lines.markersize': 10}
                        sns.set_context("talk", rc = paper_rc, font_scale=.95)
                        #sns.set_style("whitegrid")

                        g = sns.lineplot(x=x_axis, y=y_axis, hue=series, dashes=dash_styles, data=df)


                        plt.ylabel('Population')

                        plt.xticks(rotation=45)

                        plt.ylim((0, df[y_axis].max()*1.30))

                        plt.title('Cohort Component Model Solutions - {}:{}'.format(subset_field,s), y=1.25, ha='center')

                        
                        ax = plt.gca()

                        ax.xaxis.grid(False)

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2).texts[0].set_text("Solutions")

                        plt.ticklabel_format(style='plain', axis='y')

                        plt.xticks(np.arange(df[x_axis].min(), df[x_axis].max()+1,1))

                        print(np.arange(df[x_axis].min(), df[x_axis].max()+1,1))

                        plt.tight_layout()

                        plt.show()

                        allFigures.append(fig)

                        
                        



                    elif output == "abs_diff":

                        print("Absolute Differences - lineplots")
                        plt.figure(figsize=(15,16))

                        df = df[~(df["interval"].isna())] 

                        g = sns.lineplot(x="interval", y="diff",hue=series, data=df)


                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()


                    elif output == "pct_diff":

                        print("Percentage Differences - lineplots")
                        plt.figure(figsize=(15,16))

                        df = df[~(df["interval"].isna())]

                        g = sns.lineplot(x="interval", y="pct_diff",hue=series, data=df) 


                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()



                    elif output == "cumulative":

                        print("Cumulative Values - lineplots")
                        plt.figure(figsize=(15,16))


                        g = sns.lineplot(x=x_axis, y="cumulative",hue=series, data=df) 


                        ax = plt.gca()

                        #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                        ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                        mode="expand", borderaxespad=0, ncol=2)

                        plt.show()
    
        #return allFigures

    else:
        
        if df[x_axis].dtype == object:
        
            #create interval labels
            df["interval"]=df.groupby(series)[x_axis].transform(lambda x: x.shift(1) + "-" + x)
            display(df)
            print(series,y_axis)

            if placement == "grouped":

                if output== "raw":

                    g = sns.catplot(x=x_axis, y=y_axis, hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Raw Values - Bar Plot")



                elif output == "abs_diff":

                    df = df.loc[~(df["interval"].isna()),]

                    g = sns.catplot(x="interval", y="diff", hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Absolute Difference Values - Bar Plot")



                elif output == "pct_diff":

                    df = df[~(df["interval"].isna())]

                    g = sns.catplot(x="interval", y="pct_diff", hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Percentage Difference Values - Bar Plot")

                elif output == "cumulative":

                    g = sns.catplot(x=x_axis, y="cumulative", hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Cumulative Values - Bar Plot")

            elif placement == "series":


                if output== "raw":

                    print("Raw Values - lineplots")
                    plt.figure(figsize=(15,16)) 

                    g = sns.pointplot(x=x_axis, y=y_axis, hue=series, data=df,
                                         palette="muted")

                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()




                elif output == "abs_diff":

                    print("Absolute Differences - lineplots")
                    plt.figure(figsize=(15,16))

                    df = df.loc[~(df["interval"].isna()),] 

                    g = sns.pointplot(x="interval", y="diff", hue=series, data=df,
                                         palette="muted")

                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()


                elif output == "pct_diff":

                    print("Percentage Differences - lineplots")
                    plt.figure(figsize=(15,16))

                    df = df[~(df["interval"].isna())] 

                    g = sns.pointplot(x="interval", y="pct_diff", hue=series, data=df,
                                         palette="muted")

                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()



                elif output == "cumulative":

                    print("Cumulative Values - lineplots")
                    plt.figure(figsize=(15,16)) 

                    g = sns.pointplot(x=x_axis, y="cumulative", hue=series, data=df,
                                         palette="muted")

                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()

               

        elif df[x_axis].dtype == int or float:

            #create interval labels
            df["interval"]=df.groupby(series)[x_axis].transform(lambda x: x.shift(1).astype(str) + "-" + x.astype(str))

            display(df.head(15))


            if placement == "grouped":

                if output== "raw":

                    g = sns.catplot(x=x_axis, y=y_axis, hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Raw Values - Bar Plot")



                elif output == "abs_diff":

                    df = df[~(df["interval"].isna())]

                    g = sns.catplot(x="interval", y="diff", hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Absolute Difference Values - Bar Plot")



                elif output == "pct_diff":

                    df = df[~(df["interval"].isna())]

                    g = sns.catplot(x="interval", y="pct_diff", hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Percentage Difference Values - Bar Plot")

                elif output == "cumulative":

                    g = sns.catplot(x=x_axis, y="cumulative", hue=series , data=df,
                    height=10, kind="bar", palette="muted", aspect =1.3, legend=False)

                    ax = plt.gca()


                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()
                    print("Cumulative Values - Bar Plot")

            elif placement == "series":


                if output== "raw":

                    print("Raw Values - lineplots")
                    plt.figure(figsize=(15,16)) 

                    g = sns.lineplot(x=x_axis, y=y_axis,hue=series, data=df)

                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()




                elif output == "abs_diff":

                    print("Absolute Differences - lineplots")
                    plt.figure(figsize=(15,16))

                    df = df[~(df["interval"].isna())] 

                    g = sns.lineplot(x="interval", y="diff",hue=series, data=df)


                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()


                elif output == "pct_diff":

                    print("Percentage Differences - lineplots")
                    plt.figure(figsize=(15,16))

                    df = df[~(df["interval"].isna())]

                    g = sns.lineplot(x="interval", y="pct_diff",hue=series, data=df) 


                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()



                elif output == "cumulative":

                    print("Cumulative Values - lineplots")
                    plt.figure(figsize=(15,16))


                    g = sns.lineplot(x=x_axis, y="cumulative",hue=series, data=df) 


                    ax = plt.gca()

                    #x.legend(loc='lower left' , mode="expand", bbox_to_anchor=(1.05,0.5))
                    ax.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",
                    mode="expand", borderaxespad=0, ncol=2)

                    plt.show()