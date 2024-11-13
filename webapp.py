from flask import Flask, request, render_template, flash, redirect, session
from markupsafe import Markup


import os
import json

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/question", methods=['GET','POST'])
def render_question():
    session["questionNumber"] += 1
    session["usersAnswersArray"].append(request.form["answer"])
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    

    session["questionNumber"] += 1
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"])
    
@app.route("/start", methods=['GET','POST'])
def render_start():
    session["questionNumber"] = 0
    session["userAnswersArray"] = []
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    
    
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"])



@app.route("/end")
def render_end():
    return render_template('End.html')

if __name__=="__main__":
    app.run(debug=True)