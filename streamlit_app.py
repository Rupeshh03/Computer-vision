import streamlit as st
import pickle 

# loading the saved models
heart_disease_model=pickle.load(open('C:/Users/rupes/Streamlet/heart_disease_model.sav','rb'))
st.title('Welcome to Heart disease Prediction using ML') 

col1, col2, col3=st.columns(3)

with col1:
    age=st.number_input('Age' , min_value=0, max_value=100, step=1)

with col2:
    sex=st.number_input('Sex' , min_value=0, max_value=1, step=1)

with col3:
    cp=st.number_input('Chest Pain types' , min_value=0, max_value=100, step=1)        

with col1:
    trestbps=st.number_input('Resting Blood Pressure' ,min_value=0, max_value=300, step=1)

with col2:
    chol=st.number_input('Serum Cholestroral in mg/dl' , min_value=0, max_value=300, step=1)

with col3:
    fbs=st.number_input('Floating Blood Sugar > 120mg/dl' ,min_value=0, max_value=100, step=1)

with col1:
    restecg=st.number_input('Resting Electrocardiographic results',min_value=0, max_value=100, step=1)

with col2:
    thalach=st.number_input('Maximum Heart Rate achieved'  ,min_value=0, max_value=300, step=1)

with col3:
    exang=st.number_input('Exercise Induced Angina' ,min_value=0, max_value=100, step=1)

with col1:
    oldpeak=st.number_input('ST depression induced by exercise' ,step=0.01)

with col2:
    slope=st.number_input('Slope of the peak exercise ST segment' ,min_value=0, max_value=100, step=1)

with col3:
    ca=st.number_input('Major vessels colored by flourosopy' ,min_value=0, max_value=100, step=1)

with col1:
    thal=st.number_input('thal:0 = normal; 1= fixed defects; 2= reversable defect' ,min_value=0, max_value=100, step=1)


heart_diagnosis = ''; 

#Creating a button for Prediction

if st.button('Heart Disease Test Result'):
   print([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
   heart_prediction =heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
   heart_prediction = [float(x) for x in heart_prediction]
   if(heart_prediction[0]==1):
       heart_diagnosis = 'The person is having heart disease'
   else:
      heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)