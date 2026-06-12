
#  Event Management System API

A professional RESTful API built with Flask and SQLite for managing events. This application allows users to create, view, update, search, and delete events while following REST API best practices such as input validation, error handling, reusable database connections, and structured JSON responses.


## Technologies Used

* Python 3
* Flask
* SQLite3
* REST API
* JSON

---

##  Project Structure

```text
event-management-system/
│
├── app.py
├── events.db
├── README.md
└── requirem


### 4. Run Application

```bash
python app.py
```

The server will start at:

```text
http://127.0.0.1:5000
```

---

##  Database Schema

```sql
CREATE TABLE events(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL
);
```


## Create Event

### Request

```http
POST /events
```

### Request Body

```json
{
    "event_name": "Python Workshop",
    "event_date": "2026-06-12",
    "location": "Lahore"
}
```

### Response

```json
{
    "message": "Event added successfully",
    "event_id": 1
}
```

Status Code:

```text
201 Created
```

---

## Get All Events

### Request

```http
GET /events
```

### Response

```json
[
    {
        "id": 1,
        "event_name": "Python Workshop",
        "event_date": "2026-06-12",
        "location": "Lahore"
    }
]
```

Status Code:

```text
200 OK
```

---

##  Get Event By ID

### Request

```http
GET /events/1
```

### Response

```json
{
    "id": 1,
    "event_name": "Python Workshop",
    "event_date": "2026-06-12",
    "location": "Lahore"
}
```

---

##  Update Event

### Request

```http
PUT /events/1
```

### Request Body

```json
{
    "event_name": "Flask Workshop",
    "event_date": "2026-06-15",
    "location": "Islamabad"
}
```

### Response

```json
{
    "message": "Event updated successfully"
}
```

---

##  Delete Event

### Request

```http
DELETE /events/1
```

### Response

```json
{
    "message": "Event deleted successfully"
}
```

---

##  Search Event

### Request

```http
GET /events/search/Python
```

### Response

```json
[
    {
        "id": 1,
        "event_name": "Python Workshop",
        "event_date": "2026-06-12",
        "location": "Lahore"
    }
]
```

---

##  Today's Events

### Request

```http
GET /events/today
```

### Response

```json
[
    {
        "id": 1,
        "event_name": "Python Workshop",
        "event_date": "2026-06-12",
        "location": "Lahore"
    }
]
```


##  Learning Outcomes

After completing this project, you will understand:

* Flask API Development
* CRUD Operations
* SQLite Database Integrati

---

##  Future Improvements

* JWT Authenticati
---

##  Author

**Maheen Asad**

Flask • SQLite • REST API Developer

---

If you found this project useful, consider giving it a star on GitHub.
