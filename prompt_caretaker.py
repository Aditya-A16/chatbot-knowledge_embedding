
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Setup LLMChain & prompts for pet caretaker
def prompt_c():

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

    template = """
    You Own a company called PetCloud where pet caretakers can get paid for caretaking other's pets.
    I will share a caretakers question with you and you will give me the best answer that
    I should send to this caretakers based on past best practies,
    and you will follow ALL of the rules below:

    1/ Response should be very similar or even identical to the past best practies,
    in terms of length, ton of voice, logical arguments and other details

    2/ If the best practice are irrelevant, then try to mimic the style of the best practice to caretaker's message
    3/ do not set placeholders in you message
    Below is a message I received from the caretakers:
    {message}

    Here is a list of best practies of how we normally respond to prospect in similar scenarios:
    {best_practice}

    Please write the best response that I should send to this caretaker:
    """
    #create PromptTemplate variable
    prompt = PromptTemplate(
        input_variables=["message", "best_practice"],
        template=template
    )
    
    #Use LLMChain from langchain to input the prompt to llm(gpt-3.5-turbo-16k-0613)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain
