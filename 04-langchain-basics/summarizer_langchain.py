from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from scraper import fetch_website_contents   
load_dotenv()

prompt = ChatPromptTemplate.from_template(          
    "Give a short, friendly summary of this website:\n\n{website}")

model  = ChatOpenAI(model="gpt-4o-mini", temperature=0.3) 

parser = StrOutputParser()                            

chain = prompt | model | parser                     

def summarize(url):
    return chain.invoke({"website": fetch_website_contents(url)}) 

print(summarize("https://anthropic.com"))