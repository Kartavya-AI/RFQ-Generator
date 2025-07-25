# api.py
from flask import Flask, request, jsonify
from datetime import datetime
import os

from src.rfq_generator.crew import RfqGenerator

app = Flask(__name__)

@app.route("/generate-rfq", methods=["POST"])
def generate_rfq():
    data = request.get_json()
    if not data or "business_requirement" not in data:
        return jsonify({"error": "Missing 'business_requirement'"}), 400

    inputs = {
        'business_requirement': data["business_requirement"],
        'current_year': str(datetime.now().year)
    }

    try:
        # Run the crew
        RfqGenerator().crew().kickoff(inputs=inputs)

        # Read the generated markdown file
        output_path = "rfq_final.md"
        if os.path.exists(output_path):
            with open(output_path, "r") as file:
                content = file.read()
            return jsonify({
                "message": "RFQ generation complete.",
                "rfq": content
            }), 200
        else:
            return jsonify({
                "message": "RFQ generation complete, but no output file found."
            }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8084)
