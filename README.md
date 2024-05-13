## Chat Bot with OpenAI API and Flask

Introducing the Mortgage Chat Bot for resolving loan related queries.


## Prerequisites

- Python 3.9 or higher
- Flask
- Langchain
- OpenAI API
- OpenAI Python library

## Getting Started

1. Clone the repository:

   ```bash
   git clone [https://github.com/vaskar16/genai)

2  Navigate to the project directory:
    
    cd genai

3 Install the required dependencies using pip:
    
    pip install -r requirements.txt

4 Set up OpenAI API:

- Create an OpenAI account and obtain an API key.
- Set the OPENAI_API_KEY environment variable with your API key 

    On Windows:
    - Use the search bar in the Start menu to find “Edit the system environment variables”.
    - Click “Environment variables”
    - Use the upper “New…” button to add a User variable
    - Create a new variable called OPENAI_API_KEY and set the value to the secret key you got from your account settings on openai.com


5 Run the application:

    python main.py

6 Open your web browser and visit http://127.0.0.1:{port}/ to access the chat bot.



## Usage
Once the application is running, you can interact with the chat bot through the web interface. Type your messages in the input box, and the bot will respond accordingly.

## Deployment
To deploy the chat bot to a production environment, follow the deployment instructions provided by the Flask documentation. It's recommended to use a production-ready WSGI server, such as Gunicorn or uWSGI.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

    Feel free to modify and expand upon this template according to your specific project needs.
