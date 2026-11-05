from datetime import date

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

egg_records = []


@app.route("/")
def egg_tracker():
    return send_from_directory(app.root_path, "egg_tracker.html")


@app.route("/api/eggs", methods=["POST"])
def log_egg_production():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    shed = data.get("shed")
    record_date = data.get("date")
    count = data.get("count")

    if not isinstance(shed, str) or not shed.strip():
        return jsonify({"error": "shed is required"}), 400
    if not isinstance(record_date, str):
        return jsonify({"error": "date must be a valid YYYY-MM-DD date"}), 400
    try:
        date.fromisoformat(record_date)
    except ValueError:
        return jsonify({"error": "date must be a valid YYYY-MM-DD date"}), 400
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        return jsonify({"error": "count must be a non-negative integer"}), 400

    record = {"shed": shed.strip(), "date": record_date, "count": count}
    egg_records.append(record)
    return jsonify(record), 201


@app.route("/api/eggs", methods=["GET"])
def get_egg_records():
    running_total = 0
    records_with_totals = []
    for record in sorted(egg_records, key=lambda item: (item["date"], item["shed"])):
        running_total += record["count"]
        records_with_totals.append({**record, "running_total": running_total})

    return jsonify({"records": records_with_totals, "total_eggs": running_total})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)