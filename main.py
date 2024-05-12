from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai,os
#from dotenv.main import load_dotenv
from openai import OpenAI
import mysql.connector
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
llm = OpenAI()
#memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key = "your-key",
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    text=data.get('data')
    print(text)
    user_input = text
    try:
        #conversation = ConversationChain(llm=llm,memory=memory)
        #output = "ok"
        user_input_lower = user_input.lower()
        if user_input_lower.find("exit") == -1:
            prompt = f"Convert the following natural language text to SQL: {user_input}"
            messages.append({"role": "user", "content": prompt})
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            #  model="text-davinci-003",
            messages=messages,
            temperature=0,
            max_tokens=100
            )
            model_response = completion.choices[0].message.content
            model_response_lower = model_response.lower()
            sql_output=send_Query_to_DB(model_response)
            messages.append({"role": "assistant", "content": model_response})
            result_prompt = f"The query output is: {sql_output} , Give the output in NLP"
            messages.append({"role": "user", "content": result_prompt})
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                #  model="text-davinci-003",
                messages=messages,
                temperature=0,
                max_tokens=100
            )
            model_response2 = completion.choices[0].message.content
            
            #memory.save_context({"input": user_input}, {"output": output})
            return jsonify({'message': model_response2})
        else:
            del messages[2:]
            return jsonify({'message': "Resetting Chat. Please close the chat window" })
        
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})

def send_Query_to_DB(SQL_QUERY1):
     db_output = []
     mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taherpur@123",
        database="employeedb",
        auth_plugin = 'mysql_native_password'
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
print("App started");
  
if __name__ == '__main__':
    app.run()