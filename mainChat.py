import streamlit as st
import requests
import openai
import time
import os
from openai import OpenAI
from streamlit_pills import pills
#from transformers import pipeline
from streamlit_extras.let_it_rain import rain
#from transformers import AutoTokenizer, AutoModelForCausalLM#


# Retrieve the API key from the environment variable
#openai.api_key = os.environ["OPENAI_API_KEY"]
api_key = os.environ.get("OPENAI_API_KEY")
api_key = os.environ.get("HUGGINGFACE_API_KEY")

#added by PaulB to increase the UX by showing inside the tab for easy access/ notice among many open tabs
st.set_page_config(
    page_title="BOT PAUL BISWA",  
    page_icon="♻️",
    layout="wide"
)

def recycle():
    rain(
        emoji="🐣",
        font_size=37,
        falling_speed=9.1,
        animation_length=0.81,
    )
recycle()

link_color = "#e2dff4"
# Inject CSS using markdown and `unsafe_allow_html`
st.markdown(f"""<style>
a:link {{ color: {link_color}; }}
a[href="https://labs.openai.com/"] {{ color: {link_color}; }}
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
st.markdown("""
<style>
@media only screen and (max-width: 768px) {
  .st-c {  /* Target chat input container */
    margin-bottom: 20px; /* Adjust spacing as needed */
  }
}
</style>
""", unsafe_allow_html=True)

st.markdown(
        """<div class="pixel-font">:::  GREEN ECO Bot  :::</div>
    """,
        unsafe_allow_html=True,
    )
st.markdown("###### Interactive AI Asst. - *Paul Biswa*©️")
st.text("Made in 72 hrs AI Hackathon Challenge")
st.subheader(" 🌍 GenAI powered 24/7 companion on Circular Design & Sustainibility for a greener future  :four_leaf_clover:")
#st.write(" For any domestic or community water management and waste disposal guidance ")


st.markdown("""
<script>
document.querySelector(".st-c")
    .querySelector("input").focus();
document.getElementsByClassName(".st-c")[0].focus();
document.querySelector('.stTextInput > input').focus();
</script>
""", unsafe_allow_html=True)

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-0125"

# Setting the OpenAI API endpoint URL 
fine_tune_url = "https://api.openai.com/v1/models/gpt-3/fine-tune"



#model_id = "CohereForAI/c4ai-command-r-v01"
#tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
#model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
#pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

#messages = [{"role": "user", "content": "Hello, how are you?"}]
#input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

#gen_tokens = model.generate(
    #max_new_tokens=100, 
    #temperature=0.3,)
#gen_text = tokenizer.decode(gen_tokens[0])
fine_tune_data = [
  {"prompt": "Create a guide for reducing food waste in a household:",
   "completion": "Plan meals ahead to reduce overbuying and track expiration dates..."},
  {"prompt": "Develop a training program for waste management personnel on hazardous waste disposal:",
   "completion": "Provide hands-on training on the safe handling and disposal of hazardous materials..."}, 
  {"prompt": "Design a sustainable packaging solution for a food product:",
   "completion": "Using biodegradable materials and minimal packaging..."},
  {"prompt": "Create a step-by-step guide for sorting and recycling household waste:",
   "completion": "Start by separating recyclables from non-recyclables..."},
  {"prompt": "Develop a waste management plan for a small community:",
   "completion": "Conduct waste audits to identify key areas of improvement..."},
  {"prompt": "Write a policy for composting organic waste in a residential setting:",
   "completion": "All food scraps should be collected in designated bins..."},
  {"prompt": "Design a circular economy model for electronic waste recycling:",
   "completion": "Implement a system for collecting, refurbishing, and reselling electronic devices..."},
  {"prompt": "Write a proposal for implementing a community-wide composting program:",
   "completion": "Engage with local businesses and residents to promote the benefits of composting..."},
  {"prompt": "Design a waste collection schedule for a city that maximizes efficiency and reduces emissions:",
   "completion": "Utilize data analytics to optimize collection routes and allocate resources effectively..."},
  {"prompt": "Create a communication strategy to educate the public on the importance of proper waste disposal practices:",
   "completion": "Utilize social media, workshops, and community events to raise awareness and promote responsible waste management..."},
]

# Prepare the fine-tuning request data
data = {
    "training_phrases": fine_tune_data,
}
headers = {}
# Send the fine-tuning request
response = requests.post(fine_tune_url, headers=headers, json=data)

selectedExample = pills("",
            [   'What is Green Eco?', "What is Circular Design?",
                "Water Scarcity: A Family's responsibilities?", 
                "I'm confused about Plastic usage. Help me", "How to  dispose off my sanitary napkins safely?",
                "How Waste Disposal or Water Management is related with Circular Design or Sustainibility Goals?",
                "Where to discard food with fungus or when stale?", "What is Water and Waste Management?",
                "Best practices to conserve natural resources like water",
            ], ["✨","✨","✨","✨","✨","✨","✨","✨","✨"],
            clearable=False,
            index=0,
        )
#st.write( selectedExample+ "  <---  *Copy, paste/ or modify it at the bottom input bar*" )
st.markdown("*Some examples above to click.  OR Type ur Qs inside the bottom green input bar*")

placeholder_value = f"✍️ Type '{selectedExample}' here ✍️"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):st.markdown(message["content"])
    #{"role": "system", "content": "You are a waste management and disposal expert."}


# Accept user input
if prompt := st.chat_input(placeholder=placeholder_value, max_chars=555) or selectedExample:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.write("**Me:**")
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
        st.write("**My AI Bot:** ")
        #time.sleep(0.5)
        response = st.write_stream(stream)
        
    st.session_state.messages.append({"role": "assistant", "content": response})

