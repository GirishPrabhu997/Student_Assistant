from langchain_google_genai import ChatGoogleGenerativeAI

# 1. REPLACE 'YOUR_HARDCODED_KEY' with the key you are currently using in app.py
GEMINI_KEY = "YOUR_HARDCODED_KEY" 

try:
    # 2. Initialize the model 
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GEMINI_KEY
    )

    # 3. Invoke the model with a simple message
    response = llm.invoke("Say hello and confirm connection.")

    # 4. Print the result
    print("\nSUCCESS! AI Response Received:")
    print(response.content)

except Exception as e:
    print("\nFAILURE! Error details:")
    print("The key or connection is INVALID. Full Error:")
    print(e)