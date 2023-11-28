import openai
import streamlit as st
from streamlit_pills import pills
import Constants

openai.api_key = Constants.API_KEY

st.subheader("AI Assistant : Ask Me Anything")
selected = pills("", ["NO Streaming", "Streaming"], ["😊", "😎"])

user_input = st.text_input("You ", placeholder = "Ask me a question here...", key="input")


if st.button("Submit", type="primary"):
    st.markdown("____")
    res_box = st.empty()

    if selected == "Streaming":
        report = []
        for resp in openai.chat.completions.create(  model = 'gpt-3.5-turbo-1106',
                                                     messages=[{"role": "system", "content": "You are very knowledgeable in sports, dating life, tips, and fun facts. Answer the following questions in a concise way, please write at least 4 sentences."},
                                                               {"role": "user", "content": f'{user_input}'}],
                                                    
                                                    max_tokens= 1024,
                                                    temperature = 0.5,
                                                    stream = True):
            
      
            content = resp.choices[0].delta.content
            if content is not None:  # Add this check
                report.append(content)
                current_output = "".join(report).strip().replace("\n", "")
                res_box.markdown(f'*{current_output}*')
    
    else:

        completions = openai.chat.completions.create(model = 'gpt-3.5-turbo-1106',
                                                     messages=[{"role": "system", "content": "You are very knowledgeable in sports, dating life, tips, and fun facts. Answer the following questions in a concise way, limit it to no more than 4 sentences."},
                                                               {"role": "user", "content": f'{user_input}'}],
                                                    
                                                    max_tokens= 500,
                                                    temperature = 0.5,
                                                    stream = False )

        result = completions.choices[0].message.content
        res_box.write(result)