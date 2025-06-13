# filepath: c:\Users\Dell\Desktop\work\medical\backend.py
# Simplified Medical Billing System (Affordable Version)

# Fixed low-cost price list for procedures (in USD)
procedure_costs = {
    "general_checkup": 20,
    "blood_test": 15,
    "xray": 25,
    "consultation": 10,
    "medication": 30,
    "minor_surgery": 50,
    "vaccination": 10
}

def get_patient_info():
    print("Enter Patient Information")
    name = input("Name: ")
    age = int(input("Age: "))
    sickness = input("Diagnosis/Sickness: ")
    symptoms = input("Symptoms (comma-separated): ").split(",")
    
    print("\nAvailable Procedures:")
    for p, cost in procedure_costs.items():
        print(f" - {p} (${cost})")
    
    procedures = input("Enter procedures done (comma-separated): ").lower().split(",")
    procedures = [p.strip() for p in procedures if p.strip() in procedure_costs]
    
    return {
        "name": name,
        "age": age,
        "sickness": sickness,
        "symptoms": [s.strip() for s in symptoms],
        "procedures": procedures
    }

def calculate_bill(procedures):
    total = sum(procedure_costs[p] for p in procedures)
    return total

def print_bill(patient):
    print("\n--- Medical Bill Summary ---")
    print(f"Patient Name   : {patient['name']}")
    print(f"Age            : {patient['age']}")
    print(f"Sickness       : {patient['sickness']}")
    print(f"Symptoms       : {', '.join(patient['symptoms'])}")
    print(f"Procedures     : {', '.join(patient['procedures'])}")
    
    total = calculate_bill(patient['procedures'])
    print(f"Total Bill     : ${total:.2f}")
    print("\nThank you! Get well soon.")

def diagnose_symptoms(symptoms):
    from ai.symptom_diagnosis import get_diagnosis
    diagnoses = get_diagnosis(symptoms)
    return diagnoses

# Main Program
if __name__ == "__main__":
    patient_data = get_patient_info()
    print_bill(patient_data)
    
    if patient_data['symptoms']:
        diagnoses = diagnose_symptoms(patient_data['symptoms'])
        print("\nPotential Diagnoses:")
        for diagnosis in diagnoses:
            print(f" - {diagnosis}")