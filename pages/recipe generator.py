from utils import VertexLLM, VertexChat, VertexEmbeddings, VertexMultiTurnChat
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.tools import YouTubeSearchTool
from PIL import Image
# Import os to set API key
#import os
# Import OpenAI as main LLM service
#from langchain.llms import OpenAI
#from langchain.embeddings import OpenAIEmbeddings
# Bring in streamlit for UI/app interface
import streamlit as st
# Import PDF document loaders...there's other ones as well!

# Import chroma as the vector store 

llm = VertexLLM(
    model_name='text-bison@001',
    max_output_tokens=1000,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
)
tool = YouTubeSearchTool()

image=Image.open("tysonairfriedheroimage.webp")
st.image(image,width=600)

##Meal Prompt template 

from langchain.prompts import PromptTemplate

# meal template
meal_template = PromptTemplate(
    input_variables=["ingredients"],
    #template="Give me an example of  meals that could be made using the following ingredients: {ingredients}"
    template="I am a world class chef that prepares intricate meals for food competitions. Give me a recipe and name for a meal that is prepared with {ingredients}"
)
meal_chain=LLMChain(llm=llm, prompt=meal_template)

recipetitle_template = PromptTemplate(
    input_variables=["recipe"],
    template="give me single line  title for this recipe: {recipe}"
    
)
recipetitle_chain=LLMChain(llm=llm, prompt=recipetitle_template)

overall_chain = SimpleSequentialChain(chains=[meal_chain, recipetitle_chain], verbose=True)



st.title('Tyson Recipe Generator')

user_prompt = st.text_input("A comma-separated list of ingredients")
if st.button("Generate Post") and user_prompt:
    with st.spinner("Generating..."):
        
        recipe_body=meal_chain.run(user_prompt)
        #st.write(llm(meal_template.format(ingredients=user_prompt)))
        recipe_title = overall_chain.run(user_prompt)
        st.header(recipe_title)
        recipe_body=meal_chain.run(user_prompt)
        st.write(recipe_body)
        youtube_search=tool.run(recipe_title)
      
       