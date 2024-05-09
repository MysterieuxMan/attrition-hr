import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

import streamlit as st

# %pip install category_encoder
from category_encoders import OneHotEncoder

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.pipeline import make_pipeline


df = pd.read_csv('employee_data.csv')
df = df.dropna()

department_mapping = {'Human Resources': 0, 'Research & Development': 1, 'Sales': 2}
df['Department'] = df['Department'].map(department_mapping)

business_travel_mapping = {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2}
df['BusinessTravel'] = df['BusinessTravel'].map(business_travel_mapping)

eduation_mapping = {'Other': 0, 'Medical': 1, 'Life Sciences': 2, 'Marketing': 3, 'Technical Degree': 4, 'Human Resources': 5}
df['EducationField'] = df['EducationField'].map(eduation_mapping)

gender_mapping = {'Male': 0, 'Female': 1}
df['Gender'] = df['Gender'].map(gender_mapping)

MaritalStatus_Mapping = {'Married': 0, 'Single': 1, 'Divorced': 2}
df['MaritalStatus'] = df['MaritalStatus'].map(MaritalStatus_Mapping)

overTime_mapping = {'No': 0, 'Yes': 1}
df['Attrition'] = df['Attrition'].map(overTime_mapping)

encoder = LabelEncoder()
df['JobRole'] = encoder.fit_transform(df['JobRole'])

data =df.copy()
data["Attrition"]= data["Attrition"].replace({"Yes":1,
"No": 0})

X = data.drop(columns=['Attrition','HourlyRate','MonthlyRate',
                       'NumCompaniesWorked','PercentSalaryHike','YearsSinceLastPromotion',
                      'JobInvolvement','Education','Gender','YearsAtCompany','PerformanceRating','YearsWithCurrManager'], axis=1)
y = data.Attrition

x_train  , x_test , y_train, y_test  =  train_test_split (X ,y ,test_size  =  0.2 , random_state  =  0)

oversampler = SMOTE(random_state = 0)
smote_train, smote_target  =  oversampler.fit_resample(x_train,y_train)

x_train, x_test, y_train, y_test  =  train_test_split(X, y, test_size  =  0.2, random_state  =  42)

random_forest  =  make_pipeline(
    OneHotEncoder(use_cat_names=True),
    StandardScaler(),
    RandomForestClassifier())

random_forest  =  random_forest.fit(smote_train , smote_target)
def make_prediction(age, businesstravel,dailyrate,department,distanceFromHome,
                    educationfield,environmentsatisfaction,
                    joblevel,jobrole,jobsatisfaction,maritalstatus,
                    monthlyincome,relationshipsatisfaction,
                    stockoptionlevel,totalworkingyears,trainingtimeslastyear,
                    worklifebalance,yearsincurrentrole
                   ):

    data={
        'Age':age,
        'BusinessTravel':businesstravel,
        'DailyRate':dailyrate,
        'Department':department,
        'DistanceFromHome' :distanceFromHome,
        'EducationField':educationfield,
        'EnvironmentSatisfaction':environmentsatisfaction,
        'JobLevel':joblevel,
        'JobRole':jobrole,
        'JobSatisfaction':jobsatisfaction,
        'MaritalStatus':maritalstatus,
        'MonthlyIncome':monthlyincome,
        'RelationshipSatisfaction':relationshipsatisfaction,
        'StockOptionLevel':stockoptionlevel,
        'TotalWorkingYears':totalworkingyears,
        'TrainingTimesLastYear':trainingtimeslastyear,
        'WorkLifeBalance':worklifebalance,
        'YearsInCurrentRole':yearsincurrentrole
    }

    
    df=pd.DataFrame(data,index=[0])
    prediction = random_forest.predict_proba(df)[:, 1][0]

    if prediction > 0.4:
        Risk ="Strong"
        bg_color = "rgba(255, 0, 0, 0.2)" 
    elif prediction > 0.2:
        Risk = "Medium"
        bg_color = "rgba(255, 255, 0, 0.2)" 
    else:
        Risk ="Weak" 
        bg_color = "rgba(0, 128, 0, 0.2)"    

    result = f"<div style='background-color: {bg_color}; padding: 10px; border-radius: 5px; color: white;'>This employee has a <span style='color: white;'>{Risk}</span> Risk to quit with Probability = {round(prediction, 5)}.</div>"
    st.markdown(result, unsafe_allow_html=True)
    return f"{Risk}"

business_travel_map = {"Non-Travel": 0, "Travel_Frequently": 1, "Travel_Rarely": 2}
department_map = {"Human Resources": 0, "Research & Development": 1, "Sales": 2}
education_field_map = {"Human Resources": 0, "Medical": 1, "Marketing": 2, "Technical Degree": 3, "Other": 4, "Life Sciences": 5}
job_role_map = {"Research Director": 0, "Manufacturing Director": 1, "Research Scientist": 2, "Sales Executive": 3, "Human Resources": 4, "Healthcare Representative": 5, "Sales Representative": 6, "Manager": 7, "Laboratory Technician": 8}
marital_status_map = {"Divorced": 0, "Married": 1, "Single": 2}

def main():
    st.title("Employee Attrition Prediction")

    age = st.slider("Age", min_value= int(x_train['Age'].min()), max_value=int(x_train['Age'].max()), value=int(x_train['Age'].min()), step=1)
    businesstravel = st.selectbox("Business Travel", options=list(business_travel_map.keys()), format_func=lambda x: x)
    dailyrate = st.slider("Daily Rate", min_value=int(x_train['DailyRate'].min()), max_value=int(x_train['DailyRate'].max()), value=int(x_train['DailyRate'].min()), step=10)
    department = st.selectbox("Department", options=list(department_map.keys()), format_func=lambda x: x)
    distanceFromHome = st.slider("Distance From Home", min_value=int(x_train['DistanceFromHome'].min()), max_value=int(x_train['DistanceFromHome'].max()), value=int(x_train['DistanceFromHome'].min()), step=1)
    educationfield = st.selectbox("Education Field", options=list(education_field_map.keys()), format_func=lambda x: x)
    environmentsatisfaction = st.slider("Environment Satisfaction", min_value=int(x_train['EnvironmentSatisfaction'].min()), max_value=int(x_train['EnvironmentSatisfaction'].max()), value=int(x_train['EnvironmentSatisfaction'].min()), step=1)
    joblevel = st.slider("Job Level", min_value=int(x_train['JobLevel'].min()), max_value=int(x_train['JobLevel'].max()), value=int(x_train['JobLevel'].min()), step=1)
    jobrole = st.selectbox("Job Role", options=list(job_role_map.keys()), format_func=lambda x: x)
    jobsatisfaction = st.slider("Job Satisfaction", min_value=int(x_train['JobSatisfaction'].min()), max_value=int(x_train['JobSatisfaction'].max()), value=int(x_train['JobSatisfaction'].min()), step=1)
    maritalstatus = st.selectbox("Marital Status", options=list(marital_status_map.keys()), format_func=lambda x: x)
    monthlyincome = st.slider("Monthly Income", min_value=int(x_train['MonthlyIncome'].min()), max_value=int(x_train['MonthlyIncome'].max()), value=int(x_train['MonthlyIncome'].min()), step=100)
    relationshipsatisfaction = st.slider("Relationship Satisfaction", min_value=int(x_train['RelationshipSatisfaction'].min()), max_value=int(x_train['RelationshipSatisfaction'].max()), value=int(x_train['RelationshipSatisfaction'].min()), step=1)
    stockoptionlevel = st.slider("Stock Option Level", min_value=int(x_train['TotalWorkingYears'].min()), max_value=int(x_train['TotalWorkingYears'].max()), value=int(x_train['TotalWorkingYears'].min()), step=1)
    totalworkingyears = st.slider("Total Working Years", min_value=int(x_train['TotalWorkingYears'].min()), max_value=int(x_train['TotalWorkingYears'].max()), value=int(x_train['TotalWorkingYears'].min()), step=1)
    trainingtimeslastyear = st.slider("Training Times Last Year", min_value=int(x_train['TrainingTimesLastYear'].min()), max_value=int(x_train['TrainingTimesLastYear'].max()), value=int(x_train['TrainingTimesLastYear'].min()), step=1)
    worklifebalance = st.slider("Work Life Balance", min_value=int(x_train['WorkLifeBalance'].min()), max_value=int(x_train['WorkLifeBalance'].max()), value=int(x_train['WorkLifeBalance'].min()), step=1)
    yearsincurrentrole = st.slider("Years In Current Role", min_value=int(x_train['WorkLifeBalance'].min()), max_value=int(x_train['YearsInCurrentRole'].max()), value=int(x_train['YearsInCurrentRole'].min()), step=1)

    businesstravel_num = business_travel_map[businesstravel]
    department_num = department_map[department]
    educationfield_num = education_field_map[educationfield]
    jobrole_num = job_role_map[jobrole]
    maritalstatus_num = marital_status_map[maritalstatus]

    if st.button("Predict"):
        result = make_prediction(age, businesstravel_num, dailyrate, department_num, distanceFromHome,
                                 educationfield_num, environmentsatisfaction,
                                 joblevel, jobrole_num, jobsatisfaction, maritalstatus_num,
                                 monthlyincome, relationshipsatisfaction,
                                 stockoptionlevel, totalworkingyears, trainingtimeslastyear,
                                 worklifebalance, yearsincurrentrole)
        st.success(result)

if __name__ == "__main__":
    main()
