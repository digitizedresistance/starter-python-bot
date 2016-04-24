import time
import re
import random
import logging
crontable = []
outputs = []
attachments = []
typing_sleep = 0

greetings = ['Hi freak!', 'Hello mate.', 'Howdy!', 'Yo!', 'Hi!', 'Hey.']
help_text = "{}\n{}\n{}\n{}\n{}\n{}".format(
    "Hello Mate, I am cyber-punk Resistance bot: ",
    "`Punk hi` for a random greeting.",
    "`Punk joke` for a question, typing indicator, then answer style joke.",
    "`Punk attachment` to see a Slack attachment message.",
    "`Hi @<your bot's name>` to demonstrate detecting a mention.",
    "`Punk help` to see this again.")

# regular expression patterns for string matching
p_bot_hi = re.compile("Punk[\s]*hi")
p_bot_joke = re.compile("Punk[\s]*joke")
p_bot_attach = re.compile("Punk[\s]*attachment")
p_bot_help = re.compile("Punk[\s]*help")

def process_message(data):
    logging.debug("process_message:data: {}".format(data))

    if p_bot_hi.match(data['text']):
        outputs.append([data['channel'], "{}".format(random.choice(greetings))])

    elif p_bot_joke.match(data['text']):
        outputs.append([data['channel'], "Why did the PuNk cross the road?"])
        outputs.append([data['channel'], "__typing__", 5])
        outputs.append([data['channel'], "To Hack the portal YO! :laughing: Cyber-Punk!"])

    elif p_bot_attach.match(data['text']):
        txt = "Punk is a radicalbot for RiChMoNd Resistance."
        attachments.append([data['channel'], txt, build_demo_attachment(txt)])

    elif p_bot_help.match(data['text']):
        outputs.append([data['channel'], "{}".format(help_text)])

    elif data['text'].startswith("Punk"):
        outputs.append([data['channel'], "YO, This punks laptop don't know how to: `{}`".format(data['text'])])
        
    elif data['channel'].startswith("D"):  # direct message channel to the bot
        outputs.append([data['channel'], "Hello, I'm the BeepBoop python starter bot.\n{}".format(help_text)])

def process_mention(data):
    logging.debug("process_mention:data: {}".format(data))
    outputs.append([data['channel'], "Who the hell, do I know you. Chugs:beer:"])

def build_demo_attachment(txt):
    return {
        "pretext" : "We bring tears to FROGs. :sunglasses: :thumbsup:",
		"title" : "Richmond Resistance Community.",
		"title_link" : "https://plus.google.com/communities/115151623822426436338",
		"text" : txt,
		"fallback" : txt,
		"image_url" : "https://s-media-cache-ak0.pinimg.com/236x/77/10/ab/7710abf5fc857090b68efe776cf0dad3.jpg",
		"color" : "#7CD197",
    }
