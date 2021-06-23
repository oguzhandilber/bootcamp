from flask import Flask
from flask import jsonify
helloworld = Flask(__name__)

data = {
  "users": [
    {
      "username": "oguzhan",
      "mail": "test2@test2.com"
    },
    {
      "username": "dilber",
      "mail": "test1@test1.com"
    },
    {
      "status": "DevOps Engineer",
      "source": "test@test.com"
    }
  ]
}

healthcheck = {
  "health": [
    {
      "status": "{OK}",
    }
   
  ]
}

@helloworld.route("/data")
def run():
    return jsonify(data)
@helloworld.route("/healthcheck")
def run():
    return jsonify(healthcheck)
  
if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)
    
