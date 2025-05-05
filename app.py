import os

# Load the raw text file extracted using AWS Textract
with open("COMBINE_3.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

#Chunk the Data for Processing
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Define a text splitter to break long documents into smaller, retrievable chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2500,  # Each chunk has 2500 characters
    chunk_overlap=300  # Overlapping text to maintain context
)

# Split raw text into chunks
docs = text_splitter.split_text(raw_text)


from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load OpenAI embeddings (or use any other embedding model)
embedding_model = OpenAIEmbeddings(openai_api_key="OpenAI_API_Key")

# Store document chunks in FAISS for fast retrieval
vectorstore = FAISS.from_texts(docs, embedding_model)

# Save the FAISS index for future use
vectorstore.save_local("faiss_cba_index")

#Build the Chatbot Using LangChain
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load FAISS index
vectorstore = FAISS.load_local("faiss_cba_index", embedding_model, allow_dangerous_deserialization=True)

# Use GPT-4 model for high accuracy responses
llm = ChatOpenAI(model_name="gpt-4", openai_api_key="OpenAI_API_Key")

# Create a retrieval-based QA system
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),  # Retrieve top 3 relevant chunks
    chain_type="stuff"
)

# Function to interact with the chatbot
def chatbot(question):
    response = qa_chain.run(question)
    return response

import warnings
import random

warnings.filterwarnings("ignore", category=UserWarning)

# Define greeting inputs and responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """Check if the user input contains a greeting."""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

def response(user_input):
    """Generate a response based on user input."""
    answer = chatbot(user_input)
    return answer


import streamlit as st

# Streamlit UI
st.set_page_config(page_title="Pilot Buddy Chatbot", page_icon="✈️")

# Main text
st.markdown("<h1 style='text-align: center; color: #3366cc;'>Pilot Buddy ✈️ - AI Chatbot for CBAs</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Ask me anything about CBAs, and I'll provide accurate insights! 🚀</p>", unsafe_allow_html=True)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with fancy icons and formatted messages
for message in st.session_state.messages:
    if message["role"] == "user":
        # User message with a user icon and formatted text
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(f"**You**: {message['content']}")
    elif message["role"] == "assistant":
        # Bot message with a bot icon and formatted text
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"**Pilot Buddy**: {message['content']}")

# User Input (placed after the main text)
if prompt := st.chat_input("Type your message here and press Enter..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(f"**You**: {prompt}")

    # Process chatbot response
    if prompt.lower() in ["bye", "exit", "quit"]:
        bot_response = "Goodbye! Have a great day! 👋"
        # Add bot's goodbye message to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"**Pilot Buddy**: {bot_response}")
        
        # Display a warning and stop the session
        st.warning("Chatbot session has ended. Refresh the page to restart.")
        st.stop()
    else:
        # Generate a response for normal queries
        bot_response = greeting(prompt) or response(prompt)

        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(f"**Pilot Buddy**: {bot_response}")
