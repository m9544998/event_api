from flask import Flask, request, jsonify
import sqlite3
from datetime import date

app = Flask(__name__)

DATABASE = "events.db"


# Database Connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_name TEXT NOT NULL,
        event_date TEXT NOT NULL,
        location TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()

@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    event_name = data.get("event_name")
    event_date = data.get("event_date")
    location = data.get("location")

    if not event_name or not event_date or not location:
        return jsonify({
            "error": "event_name, event_date and location are required"
        }), 400

    try:
        conn = get_db_connection()

        cursor = conn.execute("""
        INSERT INTO events(event_name, event_date, location)
        VALUES (?, ?, ?)
        """, (event_name, event_date, location))

        conn.commit()

        event_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "message": "Event added successfully",
            "event_id": event_id
        }), 201

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500



@app.route("/events", methods=["GET"])
def get_events():
    try:
        conn = get_db_connection()

        events = conn.execute(
            "SELECT * FROM events"
        ).fetchall()

        conn.close()

        return jsonify([dict(event) for event in events])

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/events/<int:id>", methods=["GET"])
def get_event(id):
    try:
        conn = get_db_connection()

        event = conn.execute(
            "SELECT * FROM events WHERE id=?",
            (id,)
        ).fetchone()

        conn.close()

        if event is None:
            return jsonify({"error": "Event not found"}), 404

        return jsonify(dict(event))

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500



@app.route("/events/<int:id>", methods=["PUT"])
def update_event(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    event_name = data.get("event_name")
    event_date = data.get("event_date")
    location = data.get("location")

    if not event_name or not event_date or not location:
        return jsonify({
            "error": "All fields are required"
        }), 400

    try:
        conn = get_db_connection()

        event = conn.execute(
            "SELECT * FROM events WHERE id=?",
            (id,)
        ).fetchone()

        if event is None:
            conn.close()
            return jsonify({"error": "Event not found"}), 404

        conn.execute("""
        UPDATE events
        SET event_name=?, event_date=?, location=?
        WHERE id=?
        """, (event_name, event_date, location, id))

        conn.commit()
        conn.close()

        return jsonify({"message": "Event updated successfully"})

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500



@app.route("/events/<int:id>", methods=["DELETE"])
def delete_event(id):
    try:
        conn = get_db_connection()

        event = conn.execute(
            "SELECT * FROM events WHERE id=?",
            (id,)
        ).fetchone()

        if event is None:
            conn.close()
            return jsonify({"error": "Event not found"}), 404

        conn.execute(
            "DELETE FROM events WHERE id=?",
            (id,)
        )

        conn.commit()
        conn.close()

        return jsonify({"message": "Event deleted successfully"})

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500



@app.route("/events/search/<string:name>", methods=["GET"])
def search_event(name):
    try:
        conn = get_db_connection()

        events = conn.execute(
            "SELECT * FROM events WHERE event_name LIKE ?",
            ('%' + name + '%',)
        ).fetchall()

        conn.close()

        return jsonify([dict(event) for event in events])

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


@app.route("/events/today", methods=["GET"])
def today_events():
    today = date.today().isoformat()

    try:
        conn = get_db_connection()

        events = conn.execute(
            "SELECT * FROM events WHERE event_date=?",
            (today,)
        ).fetchall()

        conn.close()

        return jsonify([dict(event) for event in events])

    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)