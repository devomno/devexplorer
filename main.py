from google.cloud import dialogflow
import os

def detect_intent(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service_account_key.json"
    session_id = "unique_session_id"
    project_id = "your_project_id"

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    
    text_input = dialogflow.TextInput(text=text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})

    return response.query_result.fulfillment_text

if __name__ == "__main__":
    user_input = input("User: ")
    response = detect_intent(user_input)
    print("Bot:", response)
