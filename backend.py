import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


groq = st.secrets["Groq_API_Key"]



llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    groq_api_key=groq,
    temperature=0
    # other params...
)

def main_prompt(text_string):
    template = """
            I need you to help me create impactful bullet points for my resume. I will provide you with text {text_string} describing a task or accomplishment from my professional career.
            For each piece of text I provide, please:
            1. Analyze the text and extract key results, actions, and context.
            2. Create concise bullet points (no more than one line each) in the Result - Action - Context (RAC) format.
            3. Start each bullet point with a strong action verb. Prioritize impactful and dynamic verbs that emphasize achievements and skills.
            4. Use relevant keywords throughout the bullet point to optimize for Applicant Tracking Systems (ATS).
            5. If necessary, break down the provided text into multiple bullet points to ensure conciseness and clarity.
            6. Ensure the bullet point sequence should be Result - Action - Context like:
            Increased plant efficiency by 10% by spearheading the extruder upgrade project execution in a Polyethylene plant.
            
            Here's an example of the text that user will provide:
            'Led a team of five engineers in developing a new machine learning algorithm that improved customer conversion rates by 15% within six months by analyzing user behavior patterns.'
            I expect an output similar to this:
            Improved customer conversion rates by 15% within six months by leading a team of five engineers in the development of a new machine learning algorithm that analyzed user behavior patterns.
            """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    try:
        response = chain.invoke({"text_string": text_string})
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

