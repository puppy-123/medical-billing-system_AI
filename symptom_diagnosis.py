import openai

# Function to get potential diagnoses based on symptoms
def diagnose_symptoms(symptoms):
    # Join symptoms into a single string for the AI model
    symptom_input = ", ".join(symptoms)
    
    # Call to OpenAI's API (ensure you have set your API key in your environment)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"I have the following symptoms: {symptom_input}. What could be the potential diagnoses?"}
        ]
    )
    
    # Extract the response from the API
    diagnoses = response['choices'][0]['message']['content']
    
    return diagnoses

# Example usage (this can be removed or commented out in production)
if __name__ == "__main__":
    symptoms = input("Enter symptoms (comma-separated): ").split(",")
    symptoms = [s.strip() for s in symptoms]
    potential_diagnoses = diagnose_symptoms(symptoms)
    print("Potential Diagnoses:")
    print(potential_diagnoses)
