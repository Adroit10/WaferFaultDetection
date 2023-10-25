import os 
import sys
import numpy as np
import dill
from pymongo import MongoClient
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from src.exception import CustomException

def collection_as_dataframe(collection_name,db_name):
    try:
        mongo_client=MongoClient(os.getenv())
        collection=mongo_client[db_name][collection_name]
        df=pd.DataFrame(list(collection.find()))

        if "_id" in df.columns.to_list():
            df=df.drop(columns=['_id'],axis=1)
        df.replace({'na':np.nan},inplace=True)

        return df
    
    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_path,obj):
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)