import streamlit as st
import numpy as np
from src.AIDRP.pipeline.prediction import PredictionPipeline

st.set_page_config(
    page_title="AIDRP",
    page_icon="🧑‍⚕️",
    layout="wide")



st.header('Diabetes Readmission Risk Predictor',divider='rainbow')
st.write("Please enter the requested details of the patient, and the model will predict whether the patient has a risk of readmission within 30 days of discharge or not.")

age_dict = {'[0-10)':1, '[10-20)':2, '[20-30)':3, '[30-40)':4, '[40-50)':5, '[50-60)':6,'[60-70)':7, '[70-80)':8, '[80-90)':9, '[90-100)':10}
race_dict = {'AfricanAmerican':0, 'Asian':1, 'Caucasian':2, 'Hispanic':3, 'Other':4}
admission_source_id_dict = {'9, 15, 17, 20, 21':9,'1, 2, 3':1,'4, 10, 22':4,'5, 6, 18, 19, 25, 26':5,'11, 12, 13, 14':11}
admission_type_id_dict ={'1, 4':1,'2, 7':2,'3':3,'4':4,'5, 6, 8':5}
discharge_disposition_id_dict={'1, 6, 8': 1,'2, 9, 10, 23, 27, 28, 29':2,'3, 4, 5, 15, 24':3,'11, 19, 20, 21':11,'12, 18, 25, 26':18,'13, 14':13,'16, 17':16}
change_dict = {'No':0, 'Yes':1}
icd9_codes_dict = {'001-139': 1, '140-239': 2, '240-279': 3, '280-289': 4, '290-319': 5, '320-389': 6, '390-459': 7, '460-519': 8, '520-579': 9, '580-629': 10, '630-679': 11, '680-709': 12, '710-739': 13, '740-759': 14, '760-779': 15, '780-799': 16, '800-999': 17, 'E and V codes': 18}
max_glu_serum_dict = {"Norm": 1, ">200": 1.5, ">300": 2.5}
A1Cresult_dict = {"Norm": 1, ">7": 2, ">8": 2.5}
diabetesMed_dict = {'No':0, 'Yes':1}
medicines_dict = {'No':1, 'Up':3, 'Steady':2, 'Down':0}

with st.form("pred_form",clear_on_submit=True, border=True):

    age = st.selectbox("Age of patient",placeholder="Enter age of patient",options=age_dict.keys())

    race = st.selectbox("Race of patient",placeholder="Enter race of patient",options=race_dict.keys())

    admission_source_id = st.selectbox("Admission source id",placeholder="Enter admission source Integer identifier",options=admission_source_id_dict.keys())

    admission_type_id = st.selectbox("Admission type id", options = admission_type_id_dict.keys())

    discharge_disposition_id = st.selectbox("Discharge disposition id", options=discharge_disposition_id_dict.keys())

    num_lab_procedures = st.number_input("Number of lab procedures",value=None,placeholder="Number of lab tests performed during the encounter")

    num_medications = st.number_input("Number of medications",value=None,placeholder="Enter number of distinct generic names administered during the encounter")

    change = st.selectbox("Is there was a change in diabetic medications",options =change_dict.keys())

    number_diagnoses = st.number_input("Number of diagnoses",value =None, placeholder= "Enter number of diagnoses entered to the system 0%")

    num_procedures = st.number_input("Number of procedures",value =None, placeholder="Enter number of procedures (other than lab tests) performed during the encounter")

    number_outpatient = st.number_input("Number of outpatient visits",value=None,placeholder="Enter number of outpatient visits of the patient in the year preceding the encounter")

    number_inpatient = st.number_input("Number of inpatient visits",value=None,placeholder="Enter number of inpatient visits of the patient in the year preceding the encounter")

    number_emergency = st.number_input("Number of emergency visits",value=None,placeholder="Enter number of emergency visits of the patient in the year preceding the encounter")

    time_in_hospital = st.number_input("Time in hospital",value=None,placeholder="Enter number of days between admission and discharge")

    diag_1 = st.selectbox("Diagnosis 1(primary diagnosis)",options= icd9_codes_dict.keys())

    diag_2 = st.selectbox("Diagnosis 2(Secondary diagnosis)",options= icd9_codes_dict.keys())
    
    diag_3 = st.selectbox("Diagnosis 3(Additional secondary diagnosis)",options= icd9_codes_dict.keys())
    
    max_glu_serum = st.selectbox("Glucose serum test result",options=max_glu_serum_dict.keys())

    A1Cresult = st.selectbox("A1c test result", options = A1Cresult_dict.keys())

    diabetesMed = st.selectbox("Diabetes medications prescribed", options = diabetesMed_dict.keys())

    st.write("Below feature indicates whether the drug was prescribed or there was a change in the dosage")
    
    metformin = st.selectbox("Metformin",options = medicines_dict.keys())

    insulin = st.selectbox("Insulin",options = medicines_dict.keys())

    glipizide = st.selectbox("Glipizide",options = medicines_dict.keys())

    glyburide = st.selectbox("Glyburide",options = medicines_dict.keys())

    pioglitazone = st.selectbox("Pioglitazone",options = medicines_dict.keys())


    submitted = st.form_submit_button("Submit")
if submitted:
       
    st.write("submitted")
#st.write(f'The risk of 30-day readmission is {pred_prob:.2%}')

    data = [age_dict[age], race_dict[race], admission_source_id_dict[admission_source_id], admission_type_id_dict[admission_type_id],

            discharge_disposition_id_dict[discharge_disposition_id], int(num_lab_procedures), int(num_medications), change_dict[change],

            int(number_diagnoses), int(num_procedures), int(number_outpatient), int(number_inpatient), int(number_emergency), int(time_in_hospital), 
            
            icd9_codes_dict[diag_1], icd9_codes_dict[diag_2], icd9_codes_dict[diag_3], max_glu_serum_dict[max_glu_serum], A1Cresult_dict[A1Cresult],

            diabetesMed_dict[diabetesMed], medicines_dict[metformin], medicines_dict[insulin], medicines_dict[glipizide], 
            
            medicines_dict[glyburide], medicines_dict[pioglitazone]]

    data = np.array(data).reshape(1,25)

    obj = PredictionPipeline()
    predicted_value = obj.predict(data)

if predicted_value == 1:
    st.error("There is a chance that the patient will be readmitted within 30 days!", icon="🚨")

elif predicted_value == 0:
     st.success("The patient is safe to discharge", icon="✅")