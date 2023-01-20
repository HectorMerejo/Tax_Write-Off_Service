from datetime import date
from flask import Flask, request
from merejo_properties import dict_function, dict_terms
from retirement.retirement_merejo import getAllRetirementSettings

app = Flask(__name__)


# to run data through postman

@app.route("/developer")
def developer():
    general_info = {"developer": "Merejo, Hector",
                    "skills": ["HTML", "Java", "JavaScript", "XML",
                               "Python", "Flutter", "SQL"],
                    "date": date.today()
                    }

    return general_info


@app.route("/properties")
def getProperties():
    author = developer()
    data = request.args.get("mode", default=1, type=int)
    print("the date from the client", data, "the type is", type(data))

    func = dict_function[data]
    terms = dict_terms[data]
    resultSet = func()
    length = len(resultSet)

    return {"author": author, "result": resultSet, 'message': terms, "count": length}


@app.route("/retirement")
def getRetirement():
    mode = request.args.get("mode", default="s01", type=str)
    userSettings = getAllRetirementSettings(mode=mode)
    return userSettings


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=9215)
