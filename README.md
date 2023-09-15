# Custom Chatbot

This project utilizes OpenAI's GPT-3.5-turbo model with knowledge embedding to create a custom chatbot that responds differently to two types of users: Pet Owners (User type 1) and Pet Caretakers (User type 2).

## Project Structure
```bash 
Deb
|
├── data 
|   ├── owners.csv
|   ├── caretakers.csv
|
├── prompt_owner.py #prompt for owner user.
├── prompt_caretaker.py #prompt for caretaker user.
├── main.py #driver function
├── requirements.txt
├── .env #(You need to create this file and store your OpenAI API key here)
|
├── README.md
```
## Guide
To run the script, follow these steps:

1. Install the project dependencies by running the following command in your terminal:

```sh
pip install -r requirements.txt
```
2. Create a .env file in the project directory and store your OpenAI API key in it.

3. * In the main.py script, there are two variables you can customize:
user: This variable takes two inputs: 'Owner' and 'Caretaker'.  

    * Select the appropriate user type based on your scenario.

    * message: This variable is used to input the user's query or message to the chatbot.

4. Run the main.py script:
```
python main.py
```
The script will use the specified user type and message to interact with the custom chatbot and print the response in the command line.

Feel free to customize and extend the functionality of the chatbot according to your specific use case and requirements.