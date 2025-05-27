# Webchatbot_TinyLlamma
chatbot webpage built up using Tinyllamma model
Project name: Web-Chatbot 

Features:
            ▪ Agentic AI Capabilities
            ▪ Optimized for CPU/Edge Devices
            ▪ Interactive Chat Interface
            ▪ Customizable Behavior
            ▪ Error-Resilient Design
Technical Insights:
        ◦ Hugging Face Transformers integration
        ◦ Proper chat templating for TinyLlama
        ◦ Performance monitoring (response timing)
        ◦ Extensible architecture (easy to add new features)


Project Structure:
Name-of-project/
├── Main_Code.py
├── app.py
├── .env
└── templates/
    └── chat.html
    • Main_Code.py: Contains your chatbot logic using the TinyLlama model.
    • app.py: The Flask application that will serve the web interface.
    • templates/chat.html: The HTML template for the chat interface.
    • .env: environment variables 
      [SECRET_KEY=your-very-secret-key-here;  FLASK_DEBUG=True]


Libraries to be installed:

    • Python 3.11 installed 
    • python -m venv venv     #Create and Use a Virtual Environment 
    • venv\Scripts\activate
    • pip install flask
    • pip install transformers
    • pip install torch   
    • pip install python-dotenv flask-limiter markdown
    • pip install accelerate
