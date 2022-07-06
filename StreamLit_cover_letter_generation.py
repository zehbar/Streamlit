import streamlit as st

st.header("Cover Letter Generator")

desired_position = st.text_input("enter desired position")
desired_company = st.text_input("enter desired company")
strengths_and_skills = st.text_input("enter skills as strengths")
work_exp = st.text_input("enter work experience in years")
previous_work = st.text_input("enter previous work")
education = st.text_input("enter education")

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=f"\nDear [Mr./Ms./Mx.] [Hiring Manager’s Last Name],\n\nThe first paragraph should contain a self-introduction. Write who you are, where your expertise lies, where you found the job posting (or who referred you), and why you want to apply.\n\nThe second paragraph should respond directly to the job description. Describe how your relevant experiences, skills, and abilities help you meet the company’s needs. To make that easier, you can (and should) literally include words and phrases from the job description here.\n\n-You can also include a bulleted list of your accomplishments\n-Make sure you quantify (add numbers to) these bullet points\n-A cover letter with numbers is 100% better than one without\n\nTo go the extra mile, research the company and try to find out what they are doing — and why — given the current state of their industry. Explain how you can fit into that framework, and help push the company forward and achieve any goals you suspect they have.\n\nThe final paragraph is the “call to action” portion of your cover letter. Inform the hiring manager that you’d love to get interviewed. Give them your contact information. Tell them you’ll reach out again next week if you don’t hear back. Thank them for their time.\n\nSincerely,\n\n[Your Full Name]\n\nInformation: \nwork experience - {work_exp} years\njob role - {desired_position}\ncompany - {desired_company}\nprevious company - {previous_work}\neducation - {education}\nskills- {strengths_and_skills}\n\nwrite a cover letter using above information:",
  temperature=0.45,
  max_tokens=3082,
  top_p=1,
  frequency_penalty=0.2,
  presence_penalty=0.7
)



if st.button("generate"):
  st.success(response['choices'][0]['text'])
