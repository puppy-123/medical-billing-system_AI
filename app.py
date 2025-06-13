from flask import Flask, render_template, request, jsonify
import backend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bill = None
    ai_result = None
    error = None
    if request.method == "POST":
        if "bill" in request.form:
            try:
                name = request.form["name"]
                age = int(request.form["age"])
                sickness = request.form["sickness"]
                symptoms = [s.strip() for s in request.form["symptoms"].split(",")]
                procedures = [p.strip() for p in request.form.getlist("procedures")]
                patient = {
                    "name": name,
                    "age": age,
                    "sickness": sickness,
                    "symptoms": symptoms,
                    "procedures": procedures
                }
                total = backend.calculate_bill(procedures)
                bill = {
                    "patient": patient,
                    "total": total
                }
            except Exception as e:
                error = f"Error: {e}"
        elif "ai" in request.form:
            symptom = request.form["ai_symptom"]
            ai_result = backend.ai_symptom_search(symptom)
    return render_template("index.html", bill=bill, ai_result=ai_result, error=error, procedure_costs=backend.procedure_costs)

@app.route("/ai", methods=["POST"])
def ai_api():
    data = request.get_json()
    symptom = data.get("symptom", "")
    result = backend.ai_symptom_search(symptom)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)