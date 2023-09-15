from dataloader import load_embed_data 
from prompt_owner import prompt_o
from prompt_caretaker import prompt_c
from dotenv import load_dotenv


#load api OpenAI apikey stored in .env file
load_dotenv()

#Set similarity parameter here k = ?
#function to get k similar results from the knowledge base
def retrieve_info(query, db):
    similar_response = db.similarity_search(query, k=2)
    page_contents_array = [doc.page_content for doc in similar_response]
    return page_contents_array

#function to generate response given message
def generate_response(message, chain, db):
    best_practice = retrieve_info(message, db)
    response = chain.run(message=message, best_practice=best_practice)
    return response


#driver function
def main():    
    #define type of user and message for chatbot    
    user = 'Owner'
    message = 'What is the Australian legislation governing animal welfare?'

    #generate seperate response for users and caretakers
    #for PetOwner
    if user == 'Owner':
        db = load_embed_data('data\owners.csv')        
        chain = prompt_o()
        result = generate_response(message, chain, db)
        print(result)

    #for Pet Caretakers
    else:
        db = load_embed_data('data\caretakers.csv')      
        chain = prompt_c()
        result = generate_response(message, chain, db)
        print(result)


if __name__ == '__main__':
    main()
    
