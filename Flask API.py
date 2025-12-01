from flask import Flask

app = Flask(__name__)

@app.route("/resume")    
def resume():
    return"""
    <h1> RESUME </h1>
    <h3>Hello everyone , my name is Harshit.</h3>
    <h3><a href ="/projects">/projects</a></h3>
    <h3><a href ="/skills">/skills</a></h3>
    <h3><a href ="/experiences">/experiences</a></h3>
    """

@app.route("/projects")    
def projects():
    return"""
    <h1> My Projects </h1>
    <h3>Currently , I am learning python programming language.</h3>
    <h3>I have build :Calculator 
                      ATM PIN System 
                      Unit Converter 
                      Movie Ticket Booking 
                      Positive/Negative Checker
                      File Transfer App 
                      Streamlit Dashboard 
                      OpenAI Chat App 
                      Text-to-Speech Tool 
                      Game App 
                      Flask API Project</h3>
        """

@app.route("/skills")    
def skills():
    return"""
    <h1> SKILLS </h1>
    
    <h3>I have learned basics of C programming , html. </h3>
    <h3>I also know about video editing.</h3>
    <h3>I play cricket , volleyball , basketball.</h3>
    <h3></h3>
    """

@app.route("/experiences")    
def experiences():
    return"""
    <h1> EXPERIENCES </h1>
    <h3>Currently, I am doing internship in python programming at LinuxWorld</h3>
    """

if __name__=='__main__':
   app.run()
