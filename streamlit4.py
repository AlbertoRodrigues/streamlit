import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)


st.header("Streamlit Chat - Demo")
st.markdown("[Github](https://github.com/ai-yash/st-chat)")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 

message("Olá! Como posso te ajudar?") 
#message("Hello bot!", is_user=True) 


user_input = get_text()

if user_input:
 
    st.session_state.past.append(user_input)
    st.session_state.generated.append("Olá!")
    
    
if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
        