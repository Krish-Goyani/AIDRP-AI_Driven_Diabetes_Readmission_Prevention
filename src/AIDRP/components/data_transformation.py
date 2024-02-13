# Imports
from src.AIDRP.logging import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import random
from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from src.AIDRP.entity.config_entity import DataTransformationConfig

# Data transformation class
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def data_transformation(self):
        # Read input data 
        data = pd.read_csv(self.config.data_path)

        # Remove specific rows
        data.drop(index=[30506, 75551, 82573], inplace=True) 

        # Remove duplicates
        data.drop_duplicates(subset='patient_nbr', keep='first', inplace=True)

        # Remove unnecessary columns
        unused_columns = ['weight', 'citoglipton', 'examide', 
                        'payer_code', 'medical_specialty', 
                        'encounter_id', 'patient_nbr', 'repaglinide',  
                        'nateglinide', 'chlorpropamide', 'acetohexamide',
                        'tolbutamide','acarbose', 'miglitol', 
                        'troglitazone','tolazamide', 'examide', 
                        'glyburide-metformin', 'glipizide-metformin',
                        'glimepiride-pioglitazone', 'metformin-rosiglitazone',
                        'metformin-pioglitazone']

        data.drop(columns=unused_columns, inplace=True)
                
 

        index=[]
        index=list(data[data['diag_1']=='?'].index)
        index.extend(data[data['diag_2']=='?'].index)
        index.extend(data[data['diag_3']=='?'].index)
        data.drop(index=index,inplace=True)

        # all three diag features have more than 700 unqie we are grouping them based on ICD-9 codes
        diag_cols=['diag_1','diag_2','diag_3']
        for i in diag_cols:
            diag_list=[]
            for x in data[i]:
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


            data[i]=diag_list


        #feature engineering
        # replace any occurrences of '?' in the 'race' column with 'Other'.
        data['race'] = data['race'].apply(lambda x: 'Other' if x == '?' else x)
        

        # grouping similar admission_type_id
        data['admission_type_id']=data['admission_type_id'].apply(lambda x : 5 if x in (6,8) else x)
        data['admission_type_id']=data['admission_type_id'].apply(lambda x : 1 if x == 4 else 2 if x==7 else x )

        # grouping similar discharge_disposition_id
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

        # grouping similar admission_source_id
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


        # Map 'Ch' to 'Yes' in change column
        data['change'] = data['change'].apply(lambda x: 'Yes' if x=='Ch' else x) 

        # Encode change to 0/1
        data['change'] = data['change'].apply(lambda x: 0 if x=='No' else 1)

        # Encode gender to 0/1  
        data['gender'] = data['gender'].apply(lambda x: 0 if x=='Female' else 1)

        # Encode diabetesMed to 0/1
        data['diabetesMed'] = data['diabetesMed'].apply(lambda x: 0 if x=='No' else 1) 

        # Encode readmitted to 0/1
        data['readmitted'] = data['readmitted'].apply(lambda x: 1 if x=='<30' else 0)

        # List of medications 
        medicines = ['insulin', 'metformin', 'glipizide', 'glyburide', 
                    'rosiglitazone', 'pioglitazone', 'glimepiride']
                    
        # Encode medications as 0-3 scale
        for med in medicines:
            data[med] = data[med].apply(lambda x: 0 if x=='Down' 
                                            else 1 if x=='No' 
                                            else 2 if x=='Steady'  
                                            else 3)


        # Impute missing glucose values with random sampling
        glu_vals = data['max_glu_serum'].dropna().values
        data['max_glu_serum'] = data['max_glu_serum'].apply(lambda x: random.choice(glu_vals) if pd.isna(x) else x)

        # Impute missing A1c values with random sampling 
        a1c_vals = data['A1Cresult'].dropna().values
        data['A1Cresult'] = data['A1Cresult'].apply(lambda x: random.choice(a1c_vals) if pd.isna(x) else x)

        # Mapping dictionaries 
        glu_mapping = {"Norm": 1, ">200": 1.5, ">300": 2.5}
        a1c_mapping = {"Norm": 1, ">7": 2, ">8": 2.5}

        # Apply mappings
        data['max_glu_serum'] = data['max_glu_serum'].map(glu_mapping)
        data['A1Cresult'] = data['A1Cresult'].map(a1c_mapping)

        # Age ranges and values
        age_ranges = ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)', '[50-60)', 
                    '[60-70)', '[70-80)', '[80-90)', '[90-100)']
        age_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Replace age ranges with values
        for i, age_range in enumerate(age_ranges):
            data['age'] = data['age'].replace(age_range, age_values[i])

        
        # Encode categorical race column  
        encoder = LabelEncoder()
        data['race'] = encoder.fit_transform(data['race'])  

             
        X = data[['num_lab_procedures', 'num_medications', 'diag_3', 'diag_1', 'age',
            'diag_2', 'time_in_hospital', 'number_diagnoses', 'num_procedures',
            'admission_source_id', 'race', 'admission_type_id',
            'discharge_disposition_id', 'insulin', 'diabetesMed', 'change',
            'metformin', 'glipizide', 'number_outpatient', 'glyburide', 'pioglitazone', 'number_inpatient',
            'number_emergency','max_glu_serum', 'A1Cresult']]
        y = data['readmitted']

        # Resample data to deal with class imbalance
        sm = SMOTE(sampling_strategy='minority', random_state=42)

        X_res, y_res = sm.fit_resample(X, y)

        # Convert X_res to DataFrame if it's not already
        X_res['readmitted']=y_res
        data=X_res

        # Split data into train and test sets
        train, test = train_test_split(data)
        
        # Export preprocessed data
        train.to_csv(Path(Path(self.config.root_dir)/"train.csv"),index = False)
        test.to_csv(Path(Path(self.config.root_dir)/"test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)


                