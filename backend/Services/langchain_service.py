import os
from typing import Dict

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise Exception("API_KEY not found in .env file")

MODEL_NAME = "llama-3.3-70b-versatile"

llm = ChatGroq(
    model=MODEL_NAME,
    groq_api_key=API_KEY,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are TalentSpark AI. Help users with jobs, careers, interviews and programming."),
        ("placeholder", "{chat_history}"),
        ("human", "{user_query}"),
    ]
)

chain = prompt | llm

store: Dict[str, ChatMessageHistory] = {}


def get_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


chat_chain = RunnableWithMessageHistory(
    runnable=chain,
    get_session_history=get_history,
    input_messages_key="user_query",
    history_messages_key="chat_history",
)


def get_chat_response(user_query: str, session_id: str = "default"):
    try:
        response = chat_chain.invoke(
            {"user_query": user_query},
            config={
                "configurable": {
                    "session_id": session_id
                }
            },
        )

        return response.content

    except Exception as e:
        print("LANGCHAIN ERROR:", e)
        return f"Error: {str(e)}"