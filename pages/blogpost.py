from utils import VertexLLM, VertexChat, VertexEmbeddings, VertexMultiTurnChat
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
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.tools import YouTubeSearchTool


llm = VertexLLM(
    model_name='text-bison@001',
    max_output_tokens=1000,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
)


##Meal Prompt template 

from langchain.prompts import PromptTemplate

image=Image.open("colab.png")
st.image(image, width=600)


st.header('Tyson Blog Post Ideator')

# meal template
blogtitle_template = PromptTemplate(
    input_variables=["topic"],
    template="You are a  blogger and work with Tyson food marketing suggest few blog post titles for tyson foods with {topic}"
)
blogtitle_chain=LLMChain(llm=llm, prompt=blogtitle_template)

blogcontent_template=PromptTemplate(
    input_variables=["blogtitle"],
    template="""You are a  blogger and work with Tyson food marketing. Write a detailed engaging blog post for tyson foods with {blogtitle}. with a eadline, a teaser, a subtitle. Format everything in markdown, blog post should be at least 1000 words long and should include the Tyson food"""
)

blogcontent_chain=LLMChain(llm=llm, prompt=blogcontent_template)

#overall_chain = SimpleSequentialChain(chains=[blogtitle_chain, blogcontent_template], verbose=True)

st.write ("This will generate a list of post ideas for entered topic")
user_prompt = st.text_input("Enter a topic, for example: summer party")
if st.button("Generate topics") and user_prompt:
    with st.spinner("Generating..."):
        topic_ideas=blogtitle_chain.run(user_prompt)
        st.write(topic_ideas)


st.write ("Please copy one of the topics from above and generate blog post")

post_prompt = st.text_input("Enter a post title to write a blog:")
if st.button("Generate Post") and post_prompt:
    with st.spinner("Generating..."):
        post_content=blogcontent_chain.run(post_prompt)
        st.markdown(post_content)    
        
        #tool = YouTubeSearchTool()

