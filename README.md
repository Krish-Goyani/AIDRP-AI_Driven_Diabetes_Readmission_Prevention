<!-- PROJECT LOGO -->
<br />
<p align="center">
	<img src="https://i.ibb.co/hHrzvNm/logo.jpg" alt="Logo" width="400">
	<h2 align="center">AIDRP</h2>

  <p align="center">
    AI Driven Diabetes Readmission Prevention
    <br />
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Problem-Description">Problem Description </a>
    </li>
    <li>
      <a href="#Solution">Solution</a>
    </li>
    <li>
      <a href="#Users">Users</a>
    </li>
    <li>
      <a href="#Technologies">Technologies</a>
    </li>
    <li>
      <a href="#UN17-Goals-Included">UN17 Goals Included</a>
    </li>
    <li>
      <a href="#Prototype">Protoype</a>
    </li>
    <li>
	    <a href = "#How to Start Project">How to Start Project</a>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Problem Description
First of all let's understand The term "**readmission**”refers to the readmission of a patient to the same department within a certain period due to the same disease after discharge. The vast majority of patients with diabetes mellitus (DM), require repeated hospitalizations due to poor disease control. Many factors have been highlighted as contributors to patient readmission. Common causes include inappropriate or incomplete treatment, relapse, premature discharge.CMS has created many programs to improve the quality of care of patients. One of these programs is called the Hospital Readmission Reduction Program

The 30-day hospital readmission rate following an index hospitalization has become a crucial performance metric utilized by the Centers for Medicare and Medicaid Services (CMS). In 2014, CMS issued record-breaking fines to 2,610 hospitals for excessive rates of patients being readmitted within a short period of time post-discharge. Preventable readmissions lead to increased financial burdens and psychological stress for patients, repeated overutilization of medical resources, and heightened bio waste production. In 2017, the estimated United States healthcare costs related to diagnosed diabetes was approximately $327 billion, of which $237 billion represented direct medical expenditures. Recent projections estimate a 54% increase in diabetes prevalence between 2015 and 2030, which translates to over $622 billion in associated costs. Compared to overall 30-day readmission rates for inpatients, those diagnosed with diabetes have a substantially higher readmission rate ranging from 14.4% to 22.7%. According to 2012 Agency for Healthcare Research and Quality Nationwide Inpatient Sample data, a modest 5% reduction in readmissions would result in significantly fewer annual admissions and an estimated $1.2 billion in cost savings. Undoubtedly, readmissions play a major role in escalating hospital-related costs, especially among elderly diabetes patients. Consequently, diabetes-related readmissions impose a growing economic burden on patients and healthcare finance, while also propagating medical waste and suboptimal resource utilization.




## Solution 
AIDRP is an AI-driven platform that can accurately predict and reduce 30-day hospital readmission rates for diabetes mellitus (DM) patients. The platform is boosted by Gemini API, an AI assistant that answers users' questions regarding diabetes care. By enhancing prediction and prevention of avoidable readmissions, AIDRP can assist hospitals in improving quality of care, reducing costs, and optimizing performance measures. This solution also provides value to DM patients directly. The predictive model is trained on real-world electronic health record (EHR) data from the U.S. Health Facts Medical Database, which contains medical records for 100,244 diabetes patients from 1999 to 2008. It leverages relevant patient health information to identify key drivers of readmissions. Successful implementation of this AI-enabled solution has the potential to significantly enhance outcomes and decrease costs for both diabetes patients and healthcare institutions, reduced medical waste production and provides quality health.


## Users
- Hospital administrators could use the model to identify patients at high risk of readmission and target interventions to reduce those rates. This would help improve hospital performance on readmission metrics.

- Healthcare providers like doctors, nurses, and care coordinators could use the model's predictions to focus additional resources on high risk patients during and after hospitalization. This would aim to improve the quality of care and prevent readmissions.

- Population health management teams at healthcare organizations could use the model to stratify diabetes patient populations by readmission risk. This would allow tailored outreach and care programs to address the needs of different risk groups.

- Healthcare payers like insurance companies could potentially utilize the model to inform care management and transition of care support for their diabetic members. This could reduce their costs related to preventable readmissions.


## Technologies
- Gemini API
- Python
- Streamlit
- Catboost
- Plotly


<!-- GOALS -->
## UN17 Goals Included


<div style="padding:12px; display:flex; gap:30px">
<div>
<div>
<h4>Good Health And Well Being</h4>
<img style="width:300px ; height:300px" src="https://i.ibb.co/xJbZZy6/logo-3.jpg" alt="logo-3">
</div>
	
<h4>Climate Action</h4>
<img style="width:300px ; height:300px"  src="https://i.ibb.co/NYRmypy/logo-2.jpg" alt="logo-2">
</div>


</div>

## Prototype
<div style="display:flex; flex-wrap:wrap; gap:2%; justify-content:center;">
<img style="width:49%; margin-top:10px;" src="./assets/1.png">
<img style="width:49%; margin-top:10px;" src="./assets/2.png">
<img style="width:49%; margin-top:10px;" src="./assets/3.png">
<img style="width:49%; margin-top:10px;" src="./assets/4.png">
<img style="width:49%; margin-top:10px;" src="./assets/5.png">
<img style="width:49%; margin-top:10px;" src="./assets/6.png">
<img style="width:49%; margin-top:10px;" src="./assets/7.png">
</div>

[View the video demonstration](https://youtu.be/apUY99YulMo)

## How to Start Project

Follow these steps to get started with the project:

1. **Clone the Repository:**
   ```bash
   git clone <repository_link>
   ```
2. **Install Anaconda:**
   
   Make sure you have Anaconda installed on your system. If not, you can download and install it from the official website: https://www.anaconda.com/download/
   
4. **Create a Virtual Environment:**
   
   Create a new virtual environment using Python 3.9.6:

   ```bash
   conda create --name your_env_name python=3.9.6 -y
   ```
   Replace your_env_name with the desired name for your virtual environment.
   
   Activate the newly created environment:
   ```bash
   conda activate your_env_name
   ```
5. **Configure API Credentials:**
   Create a .env file in the root directory of the project.Add your Gemini API key to this file like so:
   ```python
   GEMINI_API_KEY = "your_api_key_here"
   ```
   
6. **Install Dependencies:**
   
   Install the project dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
   This command will install all the required packages listed in the requirements.txt file.

7. **Run the Streamlit App:**
   ```bash
   streamlit run AIDRP.py
   ```
   This command will start the Streamlit app.


