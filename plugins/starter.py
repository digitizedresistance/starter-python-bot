import time
import re
import random
import logging
crontable = []
outputs = []
attachments = []
typing_sleep = 0

greetings = ['Hi friend!', 'Hello there.', 'Howdy!', 'Yo!', 'Hi!', 'Hey.']
help_text = "{}\n{}\n{}\n{}\n{}\n{}".format(
    "I will kill you with the following messages: ",
    "`punk hi` for a random greeting.",
    "`punk joke` for a question, typing indicator, then answer style joke.",
    "`punk attachment` to see a Slack attachment message.",
    "`@<your bot's name>` to demonstrate detecting a mention.",
    "`punk help` to see this again.")

# regular expression patterns for string matching
p_bot_hi = re.compile("punkbot[\s]*hi")
p_bot_joke = re.compile("punkbot[\s]*joke")
p_bot_attach = re.compile("punkbot[\s]*attachment")
p_bot_help = re.compile("punk[\s]*help")

def process_message(data):
    logging.debug("process_message:data: {}".format(data))

    if p_bot_hi.match(data['text']):
        outputs.append([data['channel'], "{}".format(random.choice(greetings))])

    elif p_bot_joke.match(data['text']):
        outputs.append([data['channel'], "Why did the PuNk cross the road?"])
        outputs.append([data['channel'], "__typing__", 5])
        outputs.append([data['channel'], "To Hack the portal YO! :laughing:"])

    elif p_bot_attach.match(data['text']):
        txt = "Punk is a radicalbot for RiChMoNd Resistance."
        attachments.append([data['channel'], txt, build_demo_attachment(txt)])

    elif p_bot_help.match(data['text']):
        outputs.append([data['channel'], "{}".format(help_text)])

    elif data['text'].startswith("punk test"):
        outputs.append([data['channel'], "YO, This punk don't know how to: `{}`".format(data['text'])])

    elif data['channel'].startswith("D"):  # direct message channel to the bot
        outputs.append([data['channel'], "Hello, I'm the BeepBoop python starter bot.\n{}".format(help_text)])

def process_mention(data):
    logging.debug("process_mention:data: {}".format(data))
    outputs.append([data['channel'], "Who the hell, do I know you. Chugs:beer:"])

def build_demo_attachment(txt):
    return {
        "pretext" : "We bring tears to FROGs. :sunglasses: :thumbsup:",
		"title" : "Hack, deploy and share your tears in seconds.",
		"title_link" : "https://plus.google.com/u/0/communities/106555786480982014723/",
		"text" : txt,
		"fallback" : txt,
		"image_url" : "http://mycolorscreen.com/wp-content/uploads/wallpapers_2012/336154/you%20are%20the%20key.png",
		"color" : "#7CD197",
    }
