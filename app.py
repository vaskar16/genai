import os
import mysql.connector
from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import yaml

with open('config.yml') as stream:
    config = yaml.safe_load(stream)
# Initialize the OpenAI client
client = OpenAI(
    api_key = config['openai_key'],
)
def completion_chat_to_openai(message):
    completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        #  model="text-davinci-003",
                        messages=message,
                        temperature=config['temperature'],
                        max_tokens=config['max_tokens']
    )
    return completion.choices[0].message.content

def send_Query_to_DB(SQL_QUERY1):
     db_output = []
     mydb = mysql.connector.connect(
        host=config['db_host'],
        user=config['db_user'],
        password=config['db_password'],
        database=config['db_database'],
        auth_plugin = config['db_auth_plugin']
        )
     mycursor = mydb.cursor()
     mycursor.execute(SQL_QUERY1)
     #print ( "Result is :")
     for db in mycursor:
               # print(db)
                db_output.append(db)


     mycursor.close()
     mydb.close()
     return db_output

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    print(config['val1'])
    data = request.json
    UI_message = data['message']
    
    UI_message_lower = UI_message.lower()

    if UI_message_lower.find("exit") == -1:
        # Process the message (e.g., here we just echo back the message)
        #response_message = "You said: " + UI_message
        prompt = f"Convert the following natural language text to SQL: {UI_message}"
        # Add the user's question to the messages as a User Role    
        messages.append({"role": "user", "content": prompt})
        # Generate a completion using the user's question
        model_response = completion_chat_to_openai(messages)
        model_response_lower = model_response.lower()
        print("1")
        print(model_response_lower)
        if model_response_lower.find("insert") != -1 or model_response_lower.find("update") != -1 or model_response_lower.find("delete") != -1:
             messages.pop()
             return jsonify({'message': "This operation is not permitted"})
        search_strings = ["account_reject_clause", "reject_clause_vs_key_fields", "account_nbr_vs_all_key_fields"]
        found_strings = [s for s in search_strings if s in model_response_lower]
        print(len(found_strings))
        if (len(found_strings)) != 0:
        #if (model_response_lower.find("from")) != -1:
               if model_response_lower.find(" reject_clause") != -1 and model_response_lower.find("account_reject_clause") != -1 and model_response_lower.find("reject_clause_vs_key_fields") == -1 and model_response_lower.find("account_nbr_vs_all_key_fields") == -1:
                        print(model_response_lower.find("reject_clause"))
                        print('X1')
                        #model_response_initial = model_response
                        #UI_message_why = UI_message + "and also provide all the key fields and its values by inner join Account_nbr_vs_all_key_fields and Reject_clause_vs_key_fields"
                        #prompt_why = f"Convert the following natural language text and provide only single SQL : {UI_message_why}"
                        message_org.append({"role": "user", "content": prompt})
                        sql_output_01=send_Query_to_DB(model_response)
                        result_prompt = f"The query output is: {sql_output_01} , Give the output in NLP"
                        message_org.append({"role": "user", "content": result_prompt})
                        model_response_01 = completion_chat_to_openai(message_org)
                        message_org.append({"role": "assistant", "content": model_response_01})
                        print('Y')
                        #prompt_02_i = "what are the key fields of this rejection condition in Reject_clause_vs_key_fields table"
                        #prompt_02 = f"Convert the following natural language text to SQL: {prompt_02_i}"
                        #message_org.append({"role": "user", "content": prompt_02})
                        #model_response = completion_chat_to_openai(message_org)
                        #print(model_response)
                        #sql_output_02=send_Query_to_DB(model_response)
                        #result_prompt = f"The query output is: {sql_output_02} , Give the output in NLP"
                        #message_org.append({"role": "user", "content": result_prompt})
                        #model_response_02 = completion_chat_to_openai(message_org)
                        #message_org.append({"role": "assistant", "content": model_response_02})
                        #print('Z')
                        prompt_03_i = "what are the values of these key fields for this loan"
                        prompt_03 = f"Convert the following natural language text to SQL: {prompt_03_i}"
                        message_org.append({"role": "user", "content": prompt_03})
                        model_response = completion_chat_to_openai(message_org)
                        print(model_response)
                        sql_output_03=send_Query_to_DB(model_response)
                        result_prompt = f"The query output is: {sql_output_03} , Give the output in NLP"
                        message_org.append({"role": "user", "content": result_prompt})
                        model_response_03 = completion_chat_to_openai(message_org)
                        message_org.append({"role": "assistant", "content": model_response_03})

                        Final_user_prompt_why = model_response_01  + model_response_03 + " Can you tell me Logically which key field/fields is responsible for rejection in very short"
                        #print('2. SQL qyery')
                        print(Final_user_prompt_why)
                        del message_org[1:]
                        message_org.append({"role": "user", "content": Final_user_prompt_why})
                        model_response_why = completion_chat_to_openai(message_org)
                        model_response_why_final = model_response_01 + "\n" + model_response_why
                        print(model_response_why)
                        print(message_org)
                        message_org.append({"role": "user", "content": ddl})
                        return jsonify({'message': model_response_why_final})

                        
               else:
                    sql_output=send_Query_to_DB(model_response)
        else:
            messages.pop()
            #promptNLP = f"tell me: {UI_message}"
            #messages.append({"role": "user", "content": promptNLP})
            #print("Hello")            
            #model_response3 = completion_chat_to_openai(messages)
            response=" Hello I am here to assist you regarding Loan rejection queries. Please ask related question"
            return jsonify({'message': response})

        messages.append({"role": "assistant", "content": model_response})
        result_prompt = f"The query output is: {sql_output} , Give the output in NLP"
        messages.append({"role": "user", "content": result_prompt})

        #model_response2 = completion.choices[0].message.content + str(len(messages))
        model_response2 = completion_chat_to_openai(messages)

        return jsonify({'message': model_response2})
    else:
        del messages[2:]
        #messages = messages[:2]
        #messages.clear()
        #return jsonify({'message': "Resetting Chat. Please close the chat window" + str(len(messages)) + UI_message_lower})
        return jsonify({'message': "Resetting Chat. Please close the chat window" })
         
# Route to ignore requests for the favicon
@app.route('/favicon.ico')
def favicon():
    return ''
file_path = "C:\\Users\\USER\\Vaskar\\Python\\ddl.sql"  # Replace "file.txt" with the path to your file
try:
    with open(file_path, "r") as file:
        # Read the entire content of the file
        ddl = file.read()
        #print(ddl)
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
messages = [
    {"role": "system", "content": "Your responses should not exceed five sentences in length."}
]

messages.append({"role": "user", "content": ddl})
message_org = messages.copy()
#print("I am here");
#for message in messages:
        #print(message)
        #print('\r')    

if __name__ == '__main__':
    app.run(debug=True)
