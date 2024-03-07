import streamlit as st
import openai
import time
import os
from openai import OpenAI


# Retrieve the API key from the environment variable
api_key = os.environ.get("OPENAI_API_KEY")
api_key = os.environ.get("HUGGINGFACE_API_KEY")


#added by PaulB to increase the UX by showing inside the tab for easy access/ notice among many open tabs
st.set_page_config(
    page_title="BOT PAUL BISWA",  
    page_icon="♻️",
    layout="wide"
)


#added by PaulB to chnage the default hyoperlink colors
link_color = "#e2dff4"
# Inject CSS using markdown and `unsafe_allow_html`
st.markdown(f"""<style>
a:link {{ color: {link_color}; }}
a[href="https://labs.openai.com/"] {{ color: {link_color}; }}
a[href="https://platform.openai.com/docs/models/dall-e"] {{ color: {link_color}; }}
</style>""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        @import 'https://fonts.googleapis.com/css2?family=Orbitron&display=swap';
        .pixel-font {
            font-family: 'Orbitron', sans-serif;
            font-size: 32px;
            margin-bottom: 1rem;
        }
    </style>
""",
    unsafe_allow_html=True,
)
st.markdown(
        """<div class="pixel-font">::  Smart Waste Bot  ::</div>
    """,
        unsafe_allow_html=True,
    )
st.markdown("###### Interactive Chat - by SuperNova *Paul*")
#st.text("Interactive Chat - by SuperNova Paul")
st.header(" :wastebasket:  Your 24/7 Assistant on Circular Design   :recycle: ")
st.markdown("###### Please type in the Input Field at the bottom any Queries related to Domestic Waste Disposal Guidance and Community Waste Management Recommendations!")


# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-0125"


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):st.markdown(message["content"])
    #{"role": "system", "content": "You are a waste management and disposal expert."}

#####st.write("This is inside the container")
# Accept user input
if prompt := st.chat_input("Give me some tips for Recycling Recommender System?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.write("**You:**")
        st.markdown(prompt)



# Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        st.write("**Your Waste Bot:** ")
        time.sleep(0.03)
        response = st.write_stream(stream)
        
    st.session_state.messages.append({"role": "assistant", "content": response})



