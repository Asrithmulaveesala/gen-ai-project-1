import os
import streamlit as st
from dotenv import load_dotenv

# ============================================================
# Environment Variables
# ============================================================

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# ============================================================
# LangChain Imports
# ============================================================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Gemma AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ============================================================
# Custom CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       Remove User and Assistant Avatars
       ======================================================== */

    [data-testid="stChatMessageAvatarUser"],
    [data-testid="stChatMessageAvatarAssistant"] {
        display: none;
    }


    /* ========================================================
       Main Title
       ======================================================== */

    .main-title {
        text-align: center;
        font-size: 48px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 8px;
    }


    /* ========================================================
       Subtitle
       ======================================================== */

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #9ca3af;
        margin-bottom: 30px;
    }


    /* ========================================================
       Move Chat Input Slightly Above Bottom
       ======================================================== */

    [data-testid="stChatInput"] {
        bottom: 42px;
    }


    /* ========================================================
       Created By Footer
       ======================================================== */

    .footer {
        position: fixed;
        bottom: 5px;
        left: 0;
        right: 0;
        text-align: center;
        color: #9ca3af;
        font-size: 13px;
        z-index: 999;
    }


    /* ========================================================
       Give Bottom Space For Chat Input + Footer
       ======================================================== */

    [data-testid="stAppViewContainer"] {
        padding-bottom: 100px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="main-title">🤖 Gemma AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Powered by LangChain + Ollama + Gemma 2B'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# Load Ollama Model
# ============================================================

llm = OllamaLLM(
    model="gemma:2b"
)


# ============================================================
# Chat History
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# Prompt
# ============================================================

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. "
            "Answer the user's questions clearly and accurately."
        ),
        (
            "user",
            """
            Conversation history:
            {history}

            Current question:
            {question}
            """
        )
    ]
)


# ============================================================
# Output Parser
# ============================================================

output_parser = StrOutputParser()


# ============================================================
# LangChain Chain
# ============================================================

chain = prompt | llm | output_parser


# ============================================================
# Display Previous Messages
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# Chat Input
# ============================================================

input_text = st.chat_input(
    "Ask Gemma anything..."
)


# ============================================================
# Created By
# ============================================================

st.markdown(
    """
    <div class="footer">
        Created by <strong>Koushik Asrith Mulavisala</strong>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# Process User Question
# ============================================================

if input_text:

    # --------------------------------------------------------
    # Display User Message
    # --------------------------------------------------------

    with st.chat_message("user"):
        st.markdown(input_text)


    # --------------------------------------------------------
    # Store User Message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": input_text
        }
    )


    # --------------------------------------------------------
    # Create Conversation History
    # --------------------------------------------------------

    history = ""

    for message in st.session_state.messages[:-1]:

        if message["role"] == "user":

            history += (
                f"User: {message['content']}\n"
            )

        elif message["role"] == "assistant":

            history += (
                f"Assistant: {message['content']}\n"
            )


    # --------------------------------------------------------
    # Generate AI Response
    # --------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = chain.invoke(
                {
                    "history": history,
                    "question": input_text
                }
            )

        st.markdown(response)


    # --------------------------------------------------------
    # Store Assistant Response
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )