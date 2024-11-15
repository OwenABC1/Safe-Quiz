from flask import Flask, request, render_template, flash, redirect, session
from markupsafe import Markup


import os
import json

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/p1", methods=['GET','POST'])
def render_p1():
    session["questionNumber"] = 0
    session["usersAnswersArray"] = []
    
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    

    
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"], RenderPage =  answers[session['questionNumber']]["RenderPage"] )
    
@app.route("/p2", methods=['GET','POST'])
def render_p2():
    session["questionNumber"] += 1
    session["usersAnswersArray"].append(request.form["answer"])
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    

   
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"])
    
@app.route("/p3", methods=['GET','POST'])
def render_p3():
    session["questionNumber"] += 1
    session["usersAnswersArray"].append(request.form["answer"])
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    

   
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"])
    
@app.route("/p4", methods=['GET','POST'])
def render_p4():
    session["questionNumber"] += 1
    session["usersAnswersArray"].append(request.form["answer"])
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    

    
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"])
    
@app.route("/p5", methods=['GET','POST'])
def render_p5():
    session["questionNumber"] += 1
    session["usersAnswersArray"].append(request.form["answer"])
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    

   
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = session["questionNumber"])
    

    

@app.route("/end")
def render_end():
    session["usersAnswersArray"].append(request.form["answer"])
    
    
    session.clear()
    return render_template('End.html')

if __name__=="__main__":
    app.run(debug=True)