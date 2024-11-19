from flask import Flask, request, render_template, flash, redirect, session, url_for
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
    

    
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = 1, RenderPage =  answers[session['questionNumber']]["RenderPage"] )
    
@app.route("/p2", methods=['GET','POST'])
def render_p2():
    session["questionNumber"] = 1
    if "answer" in request.form:
        if len(session["usersAnswersArray"]) == 1:
            session["usersAnswersArray"].append(request.form["answer"])
        else:
            session["usersAnswersArray"].append("N/A")
    else:
        session["usersAnswersArray"].append("N/A")
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    
    print(session)
   
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = 2)
    
@app.route("/p3", methods=['GET','POST'])
def render_p3():
    session["questionNumber"] = 2
    if "answer" in request.form:
        if len(session["usersAnswersArray"]) == 2:
            session["usersAnswersArray"].append(request.form["answer"])
        else:
            session["usersAnswersArray"].append("N/A")
    else:
        session["usersAnswersArray"].append("N/A")
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    
    print(session)
   
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = 3)
    
@app.route("/p4", methods=['GET','POST'])
def render_p4():
    session["questionNumber"] = 3
    if "answer" in request.form: 
        if len(session["usersAnswersArray"]) == 3:
            session["usersAnswersArray"].append(request.form["answer"])
        else:
            session["usersAnswersArray"].append("N/A")
    else:
        session["usersAnswersArray"].append("N/A")
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    
    print(session)
    
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = 4)
    
@app.route("/p5", methods=['GET','POST'])
def render_p5():
    session["questionNumber"] = 4
    if "answer" in request.form:
        if len(session["usersAnswersArray"]) == 4:
            session["usersAnswersArray"].append(request.form["answer"])
        else:
            session["usersAnswersArray"].append("N/A")
    else:
        session["usersAnswersArray"].append("N/A")
    with open("static/Quiz.json") as data:
        answers = json.load(data)
    
    print(session)
   
    return render_template('p1.html', Question = answers[session['questionNumber']]["Question"], BarSize = answers[session['questionNumber']]["BarSize"], Ans1 = answers[session['questionNumber']]["Answers"][0], Ans2 = answers[session['questionNumber']]["Answers"][1], Ans3 = answers[session['questionNumber']]["Answers"][2], NextPage = answers[session['questionNumber']]["NextPage"], QuestionNum = 5)
    

    

@app.route("/end", methods=['GET','POST'])
def render_end():
    if "answer" in request.form:
        if len(session["usersAnswersArray"]) == 5:
            session["usersAnswersArray"].append(request.form["answer"])
        else:
            session["usersAnswersArray"].append("N/A")
    else:
        session["usersAnswersArray"].append("N/A")
        
    print(session)
    
    Score = 0
    
    if session["usersAnswersArray"][0] == "Hummingbirds":
        Score = Score + 1
    if session["usersAnswersArray"][1] == "The Mongol Empire":
        Score = Score + 1
    if session["usersAnswersArray"][2] == "Disease":
        Score = Score + 1
    if session["usersAnswersArray"][3] == "Leonardo da Vinci":
        Score = Score + 1
    if session["usersAnswersArray"][4] == "Franklin D. Roosevelt":
        Score = Score + 1
    print(session)
    session.clear()
    return render_template('End.html', Score=Score)
    
@app.route("/Restart")
def render_Restart():
    session.clear()
    return redirect(url_for('render_main'))
    
if __name__=="__main__":
    app.run(debug=True)