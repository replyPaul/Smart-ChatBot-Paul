---
title: Smart Waste Bot
app_file: mainChat.py
sdk/ library: streamlit
lib_version: 1.31.2
lib_author: Snowflake Inc
app_author: Paul Biswa
author_email: replypaul@gmail.com
---

# Smart ChatBot Paul
A user-friendly AI powered chat assistant with expertise in circular design & waste management.


This Bot is designed and fine tuned to provide guidance on Domestic Waste Disposal and offer recommendations for Community Waste Management. 


The shared (separetely) a/v presentation will highlight the key features and benefits of the Smart Waste Bot in promoting sustainable practices.


It was done within as part of 72 hours AI Hackathon Challenge sponsored by Saudi Data and Ministry of Communications & IT with aroun 4.4k particpants.


After learning the intrictae techniques of super fine tuning and/or retrieval augmented genration, this interactive chat bot will be enhanced with emhanced output.






## Getting Started:


### Step 1: Clone the Repository

Clone the repository containing the Streamlit app to your local machine.
Navigate to your local repository folder using 'cd' command.


### Step 2: Create and Activate a Virtual Environment

Create a virtual environment to isolate the dependencies for the app.

```bash
python3.8 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required Python dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```


### Step 4: Install Necessary Libraries

Install the necessary libraries using pip:

```bash
pip install streamlit trulens-eval openai
```

### Step 5: Set Up Streamlit Secrets

To incorporate your OpenAI API key and HuggingFace Access Token into Streamlit secrets, follow these steps:

1. Create a `.streamlit/secrets.toml` file within your project directory:

```bash
touch .streamlit/secrets.toml
```


### Step 6: Configure API Keys

Add the following lines to the file, replacing `"YOUR_API_KEY"` and `"YOUR_ACCESS_TOKEN"` with your respective keys:

```toml
OPENAI_API_KEY = "YOUR_API_KEY"
HUGGINGFACE_API_KEY = "YOUR_ACCESS_TOKEN"
```


### Step 7: Run the Streamlit App

Run the Streamlit app using the `streamlit` command.

```bash
streamlit run main.py
```


### Step 8: Access the App

Access the Streamlit app in your web browser by navigating to the URL provided by Streamlit.
Typically the URL is [http://localhost:8501](http://localhost:8501)


