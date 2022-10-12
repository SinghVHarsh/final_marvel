def filter_func(df,column,filt):
    temp_list=filt.split()
    num_list=[]
    for i in temp_list:
        if i.isdigit()==True:
            num_list.append(i)

    if ('greater' in filt):
        df_new=df.loc[df[column]>=int(num_list[0]),['id','name']]
    else:
        df_new=df.loc[df[column]<=int(num_list[0]),['id','name']]
        
    return df_new

