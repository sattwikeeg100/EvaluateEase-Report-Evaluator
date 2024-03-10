import streamlit as st
from model import evaluation_score

st.title('Report Evaluation System') 

with open('customstyle.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


def evaluation_project():
    name = st.text_input('Name of the author:')
    topic = st.text_input('Report Topic:')
    doc2 = st.text_input('Enter your report (in text format):', ' ')
    score = evaluation_score(doc2)
    grade = ''

    if score>=0.7:
        grade='A'
    elif score>=0.5:
        grade='B'
    elif score>=0.3:
        grade='C'
    else:
        grade='F'
        
    # Display the customized message 
    st.divider()
    st.write("**RESULT**")
    st.write('Your score is ', score.item(),"\t\t",'You have achieved',grade,'grade.')
    
if __name__ == '__main__':
    try:
        evaluation_project()
    
    except:
        st.write("Enter your document to see the result.")
    
    