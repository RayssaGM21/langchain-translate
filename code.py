from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("Estou estudando programação hoje!")
]

modelo = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = modelo | parser

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}"),
])

chain = template_mensagem | modelo | parser

