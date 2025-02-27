
from tensorflow.keras.models import load_model
from streamlit_option_menu import option_menu
import streamlit as st
import numpy as np
import pdfplumber
import pickle
# from linker import bigboi


heart_disease_model = pickle.load(open(r'heartdisease.pkl','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Chronic Kidney Disease Prediction'],
                          icons=['activity','heart','person','envelope'],
                          default_index=0)
    

name1 = ""
name2 = ""
diseases = []

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    st.write("Sample blood report can be downloaded from: https://github.com/Shreyas95Katti/Analysis-Diagnosis-and-Encryption-of-Blood-Work-Using-Machine-Learning-and-Block-Chain/blob/main/Blood_report.pdf")


    def main():
    
    
        st.title('Prediction')

        invoice_pdf = st.file_uploader("Choose a file",type='pdf')
        if invoice_pdf is not None:
        

            with pdfplumber.open(invoice_pdf) as pdf:
                page1 = pdf.pages[0]
                text1 = page1.extract_text()
                page2 = pdf.pages[1]
                text2 = page2.extract_text()

            lines1 = text1.split('\n')
            lines2 = text2.split("\n")

            for i in range(len(lines2)):
                lines1.append(lines2[i])

            def ocr(lines, columns):
                value = []
                for j in columns:
                    for i in lines:
                        if j == 'age':
                            if j in i:
                                i = i.split(" ")
                                value.append(float(i[4]))
                                
                        elif j == 'sex':
                            if j in i:
                                i = i.split(" ")
                                value.append(float(0) if i[6] == 'M' else float(1))
                        else:
                            i = i.split(' ')
                            if j == i[0]:
                                value.append(float(i[1]))
                return value
                
            columns1 = ['pregnancies', 'glucose', 'bloodpressure', 'skinthickness', 'insulin', 'BMI', 'diabetespredictionfunction', 'age']
            val = ocr(lines1, columns1)
            print(val)

            for i in range(len(val)):
                st.metric(label=columns1[i], value=val[i])
            for i in range(len(val)):
                columns1[i]=val[i]
            print(columns1)

        if st.button(label="Diabetes Test Result"):
            pred=model.predict(np.array([val]))
            print(pred[0][0])
            if pred[0][0] > 0.5 :
                st.error("The Person is Diabetic")
                diseases.append("Diabetic")
            else:
                st.success("The Person is non-diabetic")
            


    if __name__== "__main__" :
        model= load_model("model.h5")
        main()
    
    
# Heart Disease Prediction Page


if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    st.write("Sample blood report can be downloaded from: https://github.com/Shreyas95Katti/Analysis-Diagnosis-and-Encryption-of-Blood-Work-Using-Machine-Learning-and-Block-Chain/blob/main/Blood_report.pdf")
    st.title('Prediction')
    invoice_pdf = st.file_uploader("Choose a file",type='pdf')
    if invoice_pdf is not None:
        

        with pdfplumber.open(invoice_pdf) as pdf:
            page1 = pdf.pages[0]
            text1 = page1.extract_text()
            page2 = pdf.pages[1]
            text2 = page2.extract_text()

        lines3 = text1.split('\n')
        lines4 = text2.split("\n")

        for i in range(len(lines4)):
            lines3.append(lines4[i])

        def ocr(lines, columns):
            value = []
            for j in columns:
                for i in lines:
                    if j == 'age':
                        if j in i:
                            i = i.split(" ")
                            value.append(float(i[4]))
                            
                    elif j == 'sex':
                        if j in i:
                            i = i.split(" ")
                            value.append(float(0) if i[6] == 'M' else float(1))
                    else:
                        i = i.split(' ')
                        if j == i[0]:
                            value.append(float(i[1]))
            return value

        columns2 = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang','oldpeak','slope','ca','thal']
        val = ocr(lines3, columns2)
        print(val)

        for i in range(len(val)):
            st.metric(label=columns2[i], value=val[i])
        for i in range(len(val)):
            columns2[i]=val[i]
        # print(columns)
         
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([val])                          
        
        if (heart_prediction[0] == 1):
            st.error("The person has heart disease")
            diseases.append("HeartDisease")
        #   heart_diagnosis = 'The person is having heart disease'
        else:
        #   heart_diagnosis = 'The person does not have any heart disease'
          st.success('The person does not have any heart disease')
        
    # st.success(heart_diagnosis)


# KIDNEY DISEASE

if (selected == 'Chronic Kidney Disease Prediction'):
    
#     # page title
    st.title('Chronic Kidney Disease Prediction')
    st.write("Sample blood report can be downloaded from: https://github.com/Shreyas95Katti/Analysis-Diagnosis-and-Encryption-of-Blood-Work-Using-Machine-Learning-and-Block-Chain/blob/main/Blood_report.pdf")
    def main():
    
    
        st.title('Prediction')
        name = ""
        invoice_pdf = st.file_uploader("Choose a file",type='pdf')
        if invoice_pdf is not None:
        

            with pdfplumber.open(invoice_pdf) as pdf:
                page1 = pdf.pages[0]
                text1 = page1.extract_text()
                page2 = pdf.pages[1]
                text2 = page2.extract_text()

            lines = text1.split('\n')
            lines2 = text2.split("\n")

            for i in range(len(lines2)):
                lines.append(lines2[i])

            def ocr(lines, columns):
                x = lines[4].split()
                name = x[1] + x[2]
                print(type(name1))
                print(type(name2))
                value = []
                for j in columns:
                    for i in lines:
                        if j == 'age':
                            if j in i:
                                i = i.split(" ")
                                value.append(float(i[4]))
                                
                        elif j == 'sex':
                            if j in i:
                                i = i.split(" ")
                                value.append(float(0) if i[6] == 'M' else float(1))
                        else:
                            i = i.split(' ')
                            if j == i[0]:
                                value.append(float(i[1]))
                return value #, name
            columns = ['sg', 'al', 'sc', 'hemo', 'pcv', 'wc', 'rc', 'htn']
            val = ocr(lines, columns)
            print(val)
            for i in range(len(val)):
                st.metric(label=columns[i], value=val[i])
            for i in range(len(val)):
                columns[i]=val[i]
            print(columns)
        
        

        if st.button(label="Chronic Kidney Disease Test Result"):
            pred=model.predict(np.array([val]))
            # print(pred[0][0])
            if pred[0][0] == 1 :
                st.success("The person does not have any kidney disorder")
                
            else:
                st.error("The person has kidney disorder")
                diseases.append("ChronicKidneyDisease")

                    
          


    if __name__== "__main__" :
        model= load_model("ckdmodel.h5")
        name = ""
        main()
        # bigboi(name)
