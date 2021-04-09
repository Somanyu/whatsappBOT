from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body')

    resp = MessagingResponse()

    if(msg == "Hii" or msg == "hii"):
        resp.message("Hi, I am ```Proton``` personal assistant of Somanyu. Your message: *{}*".format(msg))
    elif(msg == "How are you?" or msg == "how are you?" or msg == "How are you"):
        resp.message("Somanyu is doing good. He might know how are you doing?")
    elif(msg == "What is he doing now?"):
        resp.message("He is probably doing something incredible *;)*")


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)