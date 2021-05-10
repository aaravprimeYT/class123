from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        "id":1,
        "title":u"buy groceries",
        "description":u"milk,cereal,chips,bananas",
        "done":False
    },
    {
        "id":2,
        "title":u"finish doomsday heist",
        "description":u"get data from a submarine then blow it up",
        "done":False
    }
]

@app.route("/")
def helloWorld():
    return "Hello World"

@app.route("/add-data",methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",''),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def getTask():
    return jsonify({
        "data":tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)

