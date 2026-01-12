from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

app = Flask(__name__)
CORS(app)

# --- 1. LOCAL AI SETUP (Ollama) ---
# Ensure you ran 'ollama pull llama3' in your terminal
llm = Ollama(model="llama3.2:1b", temperature=0.2)
chat_history = []

# --- 2. AI PROMPT SETUP ---
system_prompt = "You are a helpful Academic Assistant. Help students with their studies."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])
ai_chain = prompt | llm | StrOutputParser()

# --- 3. ROUTES (Navigation) ---

@app.route('/')
def index():
    # Looks for index.html in the templates folder
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is where your login logic will go later
        return "Login form submitted!" 
    return render_template('login.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        # This is where your registration logic will go later
        return "Registration form submitted!"
    return render_template('registration.html')

@app.route('/chat', methods=['POST'])
def chat():
    global chat_history
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        
        # Talk to local Ollama
        response = ai_chain.invoke({"input": user_input, "history": chat_history})
        
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response))
        
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "I'm having trouble. Is Ollama running?"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)