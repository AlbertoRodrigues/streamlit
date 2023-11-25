import streamlit as st
from streamlit_chat import message
from plotnine.data import mpg
from plotnine import *
from PIL import Image
import os

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)


fig = (ggplot(mpg, aes(x='displ', y='hwy'))
    + geom_point()
   + labs(x='displacement', y='horsepower')
)
fig.save("plot.png")

#arr = np.random.normal(1, 1, size=100)
#fig, ax = plt.subplots()
#ax.hist(arr, bins=20)
#plt.savefig("plot.png")



st.header("Streamlit Chat - Demo")
st.markdown("[Github](https://github.com/ai-yash/st-chat)")


if 'Graph' not in st.session_state:
    st.session_state['Graph'] = []
if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

message("Olá! Como posso te ajudar?") 

response = "plt"


#container for the chat history
response_container = st.container()
#container for the user's text input
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        
        user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
        submit_button = st.form_submit_button(label='Send')
        
    if submit_button and user_input:
        output = "Gráfico gerado com sucesso!"
        
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        if 'plt' in response:
            st.session_state['Graph'].append(Image.open(r"C:\Users\alber\OneDrive\Desktop\projetos\streamlit\plot.png"))
            response = "Chart is shown below"
        else:
            st.session_state['Graph'].append("no image")
            response = response

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i))
            try:
                st.image(st.session_state['Graph'][i], width = 800)
            except Exception as e:
                st.write(e)
                st.write("A imagem não foi gerada")
