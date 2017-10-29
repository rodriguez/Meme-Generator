from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse, Message
import random

app = Flask(__name__)
fact_list = ["Rinsing your nose with saltwater can help keep you healthy!", "Protip: dogs can smell cancer.", "You can't get a tan from your computer screen. Unplug!", "Four out of five doctors don't get enough exercise.", "Watching yourself run in a mirror can make a workout go by faster and feel easier.", "Farting helps reduce high blood pressure and is good for your health.", "Sitting for more than three hours a day can cut two years off a person's life expectancy.", "There are more skin cancer cases due to indoor tanning than lung cancer cases due to smoking.", "Chewing gum makes you more alert!", "Smell a green apple to prevent claustrophobia.", "Sit-ups won't give you a flat staomch.", "To cool down, drink something hot!", "The thigh bone is stronger than concrete."]
meme_list = ['http://25.media.tumblr.com/9a78e907714a9eb807ec153b3eee9b91/tumblr_mklmh6wVRn1qjkg5jo1_500.gif', 'https://i.pinimg.com/originals/b0/a4/39/b0a43980978ac40dfed82e44cb6d16b3.gif', 
'https://media1.tenor.com/images/f48ad03fac8223a0f7ff62c094b03091/tenor.gif?itemid=8729217', 'http://i0.kym-cdn.com/photos/images/newsfeed/001/072/167/3e2.gif','https://assets-auto.rbl.ms/13273cc2f3968434cec2e5a95ff8e334d7d2d83e342f1a7bce298921eda06399',
'https://media1.tenor.com/images/f72dfd15ebe72fedd7d3aa10359f211b/tenor.gif?itemid=5565130', 'https://media.giphy.com/media/11VQznaInAWg4U/giphy.gif', 'https://media.tenor.com/images/52d13e6274e30ee0fe98d1c20d39a341/tenor.gif', 
'https://media.giphy.com/media/YWf50NNii3r4k/giphy.gif','https://media.giphy.com/media/koUtwnvA3TY7C/200.gif']

#length = 10

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse()
    fact = fact_list[random.randint(0,len(fact_list)-1)]
    msg=resp.message(fact)
    meme = meme_list[random.randint(0,len(meme_list)-1)]
    msg.media(meme)
    return str(resp)

if __name__ == "__main__":
	app.run(debug=True)