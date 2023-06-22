import hashlib
import requests
import datetime
import pandas as pd
pub_key=input('Enter the API or public key : ')
priv_key =input('Enter the private key : ')
namestarting=input('Enter the namestarting : ')   
column_name=input('enter the column name on which you want to apply the condition : ')
condition=input('enter the condition : ')
timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
from python_package import activity_3,activity_4
df_final=activity_4.filter_func(activity_3.my_function(pub_key,activity_3.hash_params(timestamp,priv_key,pub_key),timestamp,namestarting),column_name,condition)
print(df_final)
#I have editted the file after previous commit
