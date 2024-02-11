import os
from src.AIDRP.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from src.AIDRP.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up
        
    
    def drop_columns(self,data):

        ## Drop the value which is not relevant for the model

        data.drop(index=[30506, 75551, 82573],inplace=True)
        data.drop_duplicates(subset='patient_nbr',keep='first',inplace=True)
        data.drop(columns=['weight','citoglipton','examide','payer_code','medical_specialty','encounter_id','patient_nbr','repaglinide',
                            'nateglinide','chlorpropamide','acetohexamide','tolbutamide', 
                            'acarbose','miglitol','troglitazone', 'tolazamide','examide',
                            'glyburide-metformin','glipizide-metformin',
                            'glimepiride-pioglitazone','metformin-rosiglitazone','metformin-pioglitazone'],inplace=True)
         
    def diag_cluster(self,col,data):

                            # all three diag features have more than 700 unqie we are grouping them based on ICD-9 codes
                            diag_list=[]

                            for x in data[col]:
                                # If the value in the 'col' column contains 'V' or 'E', it is assigned a cluster value of 18.
                                if 'V' in x or 'E' in x: 
                                    diag_list.append(18)
                                    continue
                                # The following conditions assign cluster values based on specific ranges of float values.
                                elif 1 <= float(x) <= 139:
                                    diag_list.append(1)
                                elif 140 <= float(x) <= 239:
                                    diag_list.append(2)
                                elif 240 <= float(x) <= 279:
                                    diag_list.append(3)
                                elif 280 <= float(x) <= 289:
                                    diag_list.append(4)
                                elif 290 <= float(x) <= 319:
                                    diag_list.append(5)
                                elif 320 <= float(x) <= 389:
                                    diag_list.append(6)
                                elif 390 <= float(x) <= 459:
                                    diag_list.append(7)
                                elif 460 <= float(x) <= 519:
                                    diag_list.append(8)
                                elif 520 <= float(x) <= 579:
                                    diag_list.append(9)
                                elif 580 <= float(x) <= 629:
                                    diag_list.append(10)
                                elif 630 <= float(x) <= 679:
                                    diag_list.append(11)
                                elif 680 <= float(x) <= 709:
                                    diag_list.append(12)
                                elif 710 <= float(x) <= 739:
                                    diag_list.append(13)
                                elif 740 <= float(x) <= 759:
                                    diag_list.append(14)
                                elif 760 <= float(x) <= 779:
                                    diag_list.append(15)
                                elif 780 <= float(x) <= 799:
                                    diag_list.append(16)
                                elif 800 <= float(x) <= 999:
                                    diag_list.append(17)


                            return diag_list
    
    def feature_enginnerings(self,data):


        #feature engineering
        # replace any occurrences of '?' in the 'race' column with 'Other'.
        data['race'] = data['race'].apply(lambda x: 'Other' if x == '?' else x)

        index=[]
        index=list(data[data['diag_1']=='?'].index)
        index.extend(data[data['diag_2']=='?'].index)
        index.extend(data[data['diag_3']=='?'].index)
        data.drop(index=index,inplace=True)


        data['admission_type_id']=data['admission_type_id'].apply(lambda x : 5 if x in (6,8) else x)
        data['admission_type_id']=data['admission_type_id'].apply(lambda x : 1 if x == 4 else 2 if x==7 else x )


        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 1 if x in (6,8) else x)
        #Uncategorized/Unknown: 18, 25, 26, 12
        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 18 if x in (25,26,12) else x)
        #Expired:11, 19, 20, 21
        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 11 if x in (19,20,21) else x)
        #Hospice:13, 14
        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 13 if x ==14 else x)
        # Discharged/Transferred to Hospital: 2, 9, 10, 23, 27, 28, 29
        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 2 if x in ( 9, 10, 23, 27, 28, 29) else x)
        #Discharged/Transferred to Care Facility: 3, 4, 5, 15, 24
        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 3 if x in ( 4, 5, 15, 24) else x)
        #Discharged to Outpatient Services:16, 17
        data['discharge_disposition_id']=data['discharge_disposition_id'].apply(lambda x : 16 if x ==17 else x)


        # Unknown/Invalid: 9, 15, 17, 20, 21
        data['admission_source_id']= data['admission_source_id'].apply(lambda x : 9 if x in (15, 17, 20, 21) else x)
        # Physician/Clinic Referral:1, 2, 3
        data['admission_source_id']= data['admission_source_id'].apply(lambda x : 1 if x in (2,3) else x)
        #Transfer from Hospital: 4, 10, 22
        data['admission_source_id']= data['admission_source_id'].apply(lambda x : 4 if x in (10,22) else x)
        #Transfer from Facility:5, 6, 18, 19, 25, 26
        data['admission_source_id']= data['admission_source_id'].apply(lambda x : 5 if x in (6, 18, 19, 25, 26) else x)
        #Delivery:11, 12, 13, 14
        data['admission_source_id']= data['admission_source_id'].apply(lambda x : 11 if x in (12, 13, 14) else x)

        data['change']=data['change'].apply(lambda x: 'Yes' if x=='Ch' else x)
        data['change']=data['change'].apply(lambda x : 0 if x=='No' else 1)

        data['gender']=data['gender'].apply(lambda x: 0 if x=='Female' else 1)

     
        data['diabetesMed']=data['diabetesMed'].apply(lambda x : 0 if x=='No' else 1)
        data['readmitted']=data['readmitted'].apply(lambda x : 1 if x=='<30' else 0)

        medicines =['insulin', 'metformin', 'glipizide' ,'glyburide' ,'rosiglitazone', 'pioglitazone' ,'glimepiride']
        for med in medicines:
            data[med]=data[med].apply(lambda x: 0 if x=='Down' else 1 if x=='No' else 2 if x=='Steady' else 3)


        mgs=data['max_glu_serum'].dropna().values
        a1=data['A1Cresult'].dropna().values
        data['max_glu_serum']=data['max_glu_serum'].apply(lambda x: random.choice(mgs) if pd.isna(x) else x)
        data['A1Cresult']=data['A1Cresult'].apply(lambda x: random.choice(a1) if pd.isna(x) else x)

        mapping_dict = {"Norm": 1, ">7": 2, ">8": 2.5}

        # Apply the mapping to the 'max_glu_serum' column
        data['A1Cresult'] = data['A1Cresult'].map(mapping_dict)
        

        mapping_dict = {"Norm": 1, ">200": 1.5, ">300": 2.5}

        # Apply the mapping to the 'max_glu_serum' column
        data['max_glu_serum'] = data['max_glu_serum'].map(mapping_dict)

        data['diag_1']=self.diag_cluster('diag_1',data)
        data['diag_2']=self.diag_cluster('diag_2',data)
        data['diag_3']=self.diag_cluster('diag_3',data)
        
        #replace age range with 1 to 10
        age_ranges = ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)','[60-70)', '[70-80)', '[80-90)', '[90-100)']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # The function iterates through the age_ranges and replaces each occurrence in the 'feature' with the corresponding numerical value.
        for i, age_range in enumerate(age_ranges):
            data['age'] = data['age'].replace(age_range, values[i])

        

        encoder=LabelEncoder()
        data['race']=encoder.fit_transform(data['race'])  

    def preprocessing(self):
        data= pd.read_csv(self.config.data_path)
       

        self.drop_columns(data)

        self.feature_enginnerings(data)

       # Performing a merge (cross join) on the common key
      
        X = data[['num_lab_procedures', 'num_medications', 'diag_3', 'diag_1', 'age',
            'diag_2', 'time_in_hospital', 'number_diagnoses', 'num_procedures',
            'admission_source_id', 'race', 'admission_type_id',
            'discharge_disposition_id', 'insulin', 'diabetesMed', 'change',
            'metformin', 'glipizide', 'number_outpatient', 'glyburide', 'pioglitazone', 'number_inpatient',
            'number_emergency','max_glu_serum', 'A1Cresult']]
        y = data['readmitted']

        sm = SMOTE(sampling_strategy='minority', random_state=42, n_jobs=-1)


        X_res, y_res = sm.fit_resample(X, y)
       # Convert X_res to DataFrame if it's not already
        X_res['readmitted']=y_res
        data=X_res

        # we have found that there are many entries of some users in dataset it will make our ML algorithm biased so removing them.
        train,test = train_test_split(data)
        # train.to_csv(self.config.root_dir,"train.csv",index=False)
        # test.to_csv(self.config.root_dir,"test.csv",index=False)
    

      # Parent Directory path (use raw string to avoid escape characters)
        #parent_dir = r"C:\DataScience\Projects\folder\AIDRP-AI_Driven_Diabetes_Readmission_Prevention\artifacts\data_transformation"

        # Create the directory for data transformation if it doesn't exist
        #directory_path = os.path.join(parent_dir, 'data_transformation')
        #os.makedirs(directory_path, exist_ok=True)

        train.to_csv(self.config.root_dir, 'train.csv', index=False)
        test.to_csv(self.config.root_dir, 'test.csv', index=False)

        logger.info("Split data into training and test sets")

     

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)


