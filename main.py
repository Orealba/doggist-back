from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def root():
    return "Home"


@app.route("/users/<user_id>")
def get_user(user_id):
    """
        {"id": user_id, "name": "puppie", "telefono": "2244534"}
        """
    user = {
      "id": "1",
      "name": "Leeloo",
      "species": "Dog",
      "breed": "Boston Terrier",
      "birthDate": "2017-07-07",
      "gender": "Female",
      "color": "Black",
      "microChip": "1234567890",
      "lastAppointment": {
        "data": {
          "weight": 8.1,
          "height": 9.5,
          "date": "2020-07-07",
          "reason": "Annual checkup",
          "doctor": "Dr. Smith",
          "notes": "Leeloo is in good health."
        },
        "medications": [
          {
            "name": "Heartguard",
            "dose": "1 pill",
            "frequency": "monthly"
          },
          {
            "name": "Frontline",
            "dose": "1 pipette",
            "frequency": "monthly"
          }
        ]
      },
      "medications": [
        {
          "type": "vaccine",
          "name": "Rabiesin",
          "dose": "shot",
          "frequency": "yearly",
          "date": "2020-07-07",
          "validUntil": "2021-07-07",
          "isActive": True
        },
        {
          "type": "vaccine",
          "name": "Distemper",
          "dose": "shot",
          "frequency": "yearly",
          "date": "2020-07-07",
          "validUntil": "2021-07-07",
          "isActive": True
        },
        {
          "type": "antiparasite",
          "name": "Frontline",
          "dose": "pipette",
          "frequency": "quarterly",
          "date": "2020-07-07",
          "validUntil": "2021-07-07",
          "isActive": True
        },
        {
          "type": "antiparasite",
          "name": "Heartguard",
          "dose": "pill",
          "frequency": "yearly",
          "date": "2020-07-07",
          "validUntil": "2021-07-07",
          "isActive": True
        }
      ],
      "lastAppointments": [
        {
          "data": {
            "weight": 8.1,
            "height": 9.5,
            "date": "2020-07-07",
            "reason": "Annual checkup",
            "doctor": "Dr. Smith",
            "notes": "Leeloo is in good health."
          },
          "medications": [
            {
              "name": "Heartguard",
              "dose": "1 pill",
              "frequency": "monthly"
            },
            {
              "name": "Frontline",
              "dose": "1 pipette",
              "frequency": "monthly"
            }
          ]
        },
        {
          "data": {
            "weight": 8.1,
            "height": 9.5,
            "date": "2020-07-07",
            "reason": "Annual checkup",
            "doctor": "Dr. Smith",
            "notes": "Leeloo is in good health."
          },
          "medications": [
            {
              "name": "Heartguard",
              "dose": "1 pill",
              "frequency": "monthly"
            },
            {
              "name": "Frontline",
              "dose": "1 pipette",
              "frequency": "monthly"
            }
          ]
        },
        {
          "data": {
            "weight": 8.1,
            "height": 9.5,
            "date": "2020-07-07",
            "reason": "Annual checkup",
            "doctor": "Dr. Smith",
            "notes": "Leeloo is in good health."
          },
          "medications": [
            {
              "name": "Heartguard",
              "dose": "1 pill",
              "frequency": "monthly"
            },
            {
              "name": "Frontline",
              "dose": "1 pipette",
              "frequency": "monthly"
            }
          ]
        }
      ],
      "ownerInfo": {
        "id": "1",
        "name": "John Doe",
        "email": "abc@def.com",
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
      }
    }




    #/users/1?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201




if __name__ == '__main__':
    app.run(debug=True)
