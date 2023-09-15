from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

#Setup LLMChain & prompts for pet owner
def prompt_o():
    
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

    template = """
    You Own a company called PetCloud where pet owners can get their pets taken care of.
    I will share a pet owner's question with you and you will give me the best answer that
    I should send to this pet owner based on past best practies,
    and you will follow ALL of the rules below:

    1/ Response should be very similar or even identical to the past best practies,
    in terms of length, ton of voice, logical arguments and other details

    2/ If the best practice are irrelevant, then try to mimic the style of the best practice to pet owner's message
    3/ do not set placeholders in you message
    Below is a message I received from the a pet owner:
    {message}

    Here is a list of best practies of how we normally respond to a pet owner in similar scenarios:
    {best_practice}

    Please write the best response that I should send to this pet owner:
    """
    #create PromptTemplate variable
    prompt = PromptTemplate(
        input_variables=["message", "best_practice"],
        template=template
    )
    #Use LLMChain from langchain to input the prompt to llm(gpt-3.5-turbo-16k-0613)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain