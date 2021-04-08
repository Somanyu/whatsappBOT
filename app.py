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
    resp.message("Hi, I am friday personal assistant of Somanyu. Your message: *{}*".format(msg))
    if (msg == "How are you??"):
        resp.message("Somanyu is doing good. He might know how are you doing?")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)