## A HUGE thank you to Alexa Mayer for these amazing lessons
## https://plus.google.com/+AlexaMayer/posts
## Responds to each of the cues for the lesson names
##  /bot sl <#>, /bot sl random, /bot sl list, and /bot sl <keyword>
## option to add in all the keywords as commands

import aiohttp, io, logging, os, re, plugins, random

def _initialise(bot):
##    plugins.register_user_command(["sl","how","walk","portals","hacking","resonators",\
##                                   "xmp","keys","linking","fielding","defensemods",\
##                                   "hackmods","linkamps","leveling","mu","cubes",\
##                                   "farming","terms","virus","placement",\
##                                   "campfire","ultrastrikes","anomaly",\
##                                   "smartfarming","capsules","mufg","softbank",\
##                                   "store", "lawson"])
    plugins.register_user_command(["sl"])
    return []

def smurflinglesson(bot, event, link_image):
    if link_image == "list":
    	commands = ["how do i walk","walk","portals","hacking","resonators",\
                    "bursters","keys","linking","fielding","defensemods","hackmods",\
                    "linkamps","leveling","mu","cubes","farming","terms","virus",\
                    "placement","campfire","ultrastrikes","anomaly","smartfarming",\
                    "capsules","mufg","softbank","store","lawson"]
    	commands.insert(0,_("<b>The available lessons are:</b>"))
    	message = _("<br />".join(commands))
    	yield from bot.coro_send_message( event.conv_id, message)
    elif link_image == "none":
        url = []
        url.append(_("<b>The smurfling lessons can be found here:</b>"))
        url.append(_("https://plus.google.com/photos/+AlexaMayer/albums/6069486745282199137"))
        message = _("<br />".join(url))
        yield from bot.coro_send_message(event.conv.id_, message)
    else:
        try:   
            filename = os.path.basename(link_image)
            r = yield from aiohttp.request('get', link_image)
            raw = yield from r.read()
            image_data = io.BytesIO(raw)
            image_id = yield from bot._client.upload_image(image_data, filename=filename)
            yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)
        except:
            url = []
            url.append(_("<b>Error... but</b> the smurfling lessons can be found here:"))
            url.append(_("https://plus.google.com/photos/+AlexaMayer/albums/6069486745282199137"))
            message = _("<br />".join(url))
            yield from bot.coro_send_message(event.conv.id_, message)

def sl(bot, event, *args):
    param = list(args)
    try:
        lesson = int(param[0])
    except:
        try: lesson = param[0]
        except: lesson = "none"
    
    lessonNames = {"how":1,"walk":1,"portals":2,"hacking":3,"resonators":4,\
                    "xmp":5,"keys":6,"linking":7,"fielding":8,"defensemods":9,\
                    "hackmods":10,"linkamps":11,"leveling":12,"mu":13,"cubes":14,\
                    "farming":15,"terms":16,"virus":17,"placement":18,\
                    "campfire":19,"ultrastrikes":20,"anomaly":21,\
                    "smartfarming":22,"capsules":23,"mufg":24,"softbank":25,\
                    "store":26,"lawson":27}
    
    
    link_image = "none"
    allLessons = ["https://lh5.googleusercontent.com/-J2fEJVz-3dI/VDsmC4Cn3gI/AAAAAAAAQfI/2z9dBxwoi1M/w662-h856-no/1-Walking.png",\
                "https://lh5.googleusercontent.com/-Hf3WmS_elXc/VYAerQ_XLoI/AAAAAAAAdfw/uaWbLtECsbw/w776-h1004-no/2-Portals.png",\
                "https://lh5.googleusercontent.com/-rf86cgbh2Fs/VYAmQH0JheI/AAAAAAAAdeA/r8Fu1w9Ky4g/w776-h1004-no/3-Hacking.png",\
                "https://lh3.googleusercontent.com/-4aFCdpIsYYU/VYAmQDGA5kI/AAAAAAAAdeE/ZU8cbaD0ROk/w776-h1004-no/4-Resonators.png",\
                "https://lh5.googleusercontent.com/-YgxwgFDkOTs/VYAmQO_NfrI/AAAAAAAAdeI/21NtvxppuSk/w776-h1004-no/5-Bursters.png",\
                "https://lh3.googleusercontent.com/-UXCV2t_CUjA/VDsmH4v-oHI/AAAAAAAAQgk/OriM4_QeyR0/w776-h1004-no/6-PortalKeys.png",\
                "https://lh3.googleusercontent.com/-3qHVoV_VqqI/VDsmH-bSnQI/AAAAAAAAQgs/eH2SD0qXGLI/w776-h1004-no/7-Linking.png",\
                "https://lh3.googleusercontent.com/-XtTbqbPrhYQ/VDsmIpGoO6I/AAAAAAAAQg4/gwlqWEY_krs/w776-h1004-no/8-Fielding.png",\
                "https://lh5.googleusercontent.com/-WrjAAvnaH7k/VYGG8Dwtn1I/AAAAAAAAdlk/utcmAMZWFxY/w776-h1004-no/9-DefenseMods.png",\
                "https://lh3.googleusercontent.com/-voUze_0Bd_Q/VDsmC_HQt-I/AAAAAAAAQfM/_BWORWw8aWA/w776-h1004-no/10-HackMods.png",\
                "https://lh3.googleusercontent.com/-V0iCiQWN5cg/VDsmCkfxNZI/AAAAAAAAQfE/JXmnmoECrpM/w776-h1004-no/11-LinkAmps.png",\
                "https://lh3.googleusercontent.com/-pz0YD5avqto/VDsmEKGRfJI/AAAAAAAAQfs/rszf8ilLQs8/w776-h1004-no/12-Leveling.png",\
                "https://lh5.googleusercontent.com/-PbtYYv5nfhI/VDsmEVVKlgI/AAAAAAAAQfo/gUXG7mP21XI/w776-h1004-no/13-MUscoring.png",\
                "https://lh5.googleusercontent.com/-dpQPYEbSN_c/VDsmEe462LI/AAAAAAAAQfk/PF07ddPoqSg/w776-h1004-no/14-PowerCubes.png",\
                "https://lh3.googleusercontent.com/-x0rw0_xgjXY/VDsmFrIul6I/AAAAAAAAQgA/xYb6kUMHies/w776-h1004-no/15-Farming.png",\
                "https://lh3.googleusercontent.com/-donlBCedLnQ/VFfBPwDMbfI/AAAAAAAASk8/fwfpO6PbhOI/w776-h1004-no/16-TYSK.png",\
                "https://lh5.googleusercontent.com/-aMy7XoJ0JIE/VDtR51w0l_I/AAAAAAAAQqk/jlos_0V8rzY/w776-h1004-no/17-ADAJARVIS.png",\
                "https://lh5.googleusercontent.com/-ZX9xO6gVWiI/VFpCWALhKkI/AAAAAAAAS2o/arI0uukmhIg/w776-h1004-no/18-ResoPlacement.png",\
                "https://lh5.googleusercontent.com/-TjPTIDctozA/VDstyuAbqgI/AAAAAAAAQhk/f7_E7lEmtTQ/w776-h1004-no/19-Campfiring.png",\
                "https://lh3.googleusercontent.com/-82J8Ppz15Jk/VFe-_MHdvJI/AAAAAAAASjA/WUYfQ1-81_E/w776-h1004-no/20-ultrastrikes.png",\
                "https://lh3.googleusercontent.com/-32vilg99LAQ/VFe-_Fq3fHI/AAAAAAAASjE/5FIEBOfMeZA/w776-h1004-no/21-Anomaly.png",\
                "https://lh5.googleusercontent.com/-n7iEVCJN3hs/VYAsR4-PaoI/AAAAAAAAde0/rIK5zGy1_mU/w776-h1004-no/22-TheArtofFarming.png",\
                "https://lh3.googleusercontent.com/-M44yA_tGZzI/VNt5vdogVNI/AAAAAAAAXg8/xRHGC84gNZE/w776-h1004-no/23-Capsules.png",\
                "https://lh5.googleusercontent.com/-KwLcC_yJJeo/VgwGFQgDWxI/AAAAAAAAmVQ/04lfFFH6rLQ/w776-h1004-no/24-MUFG.png",\
                "https://lh3.googleusercontent.com/-j-GE89rVgwU/Vgxe6KzVtoI/AAAAAAAAmXg/Uq7-3lWxMp4/w776-h1004-no/25-%2BSBULA.png",\
                "https://lh3.googleusercontent.com/-OmM1N2JysTY/VkOdNkbLRPI/AAAAAAAAn40/JjLuc6KLpHo/w776-h1004-no/26-%2BIngress%2BStore.png",\
                "https://lh5.googleusercontent.com/-47IvmKvFI4s/Vwf4-mhXnjI/AAAAAAAAvFM/Mu59w7po7Gsro0JawycVeKCSEwz6aVm8wCL0B/w697-h902-no/27-LAwsonCubes.png"]

    if  type(lesson) == int:
        try:
            link_image = allLessons[lesson-1]
        except:
            link_image = "error"
    elif lesson == "list":
        link_image = "list"
    elif lesson == "random":
        link_image = allLessons[random.randint(0,25)]
    elif lesson == "none":
        link_image = "none"
    else:
        try: link_image = allLessons[lessonNames[lesson]-1]
        except: link_image = "none"

    yield from smurflinglesson(bot, event, link_image)

##def how(bot, event, *args):
##    message=event.text.lower()
##    lesson1=re.search('how do i walk',message)
##    if lesson1: yield from sl(bot, event, 1, *args)

##def walk(bot, event, *args): yield from sl(bot, event, 1, *args)
##def portals(bot, event, *args): yield from sl(bot, event, 2, *args)
##def hacking(bot, event, *args): yield from sl(bot, event, 3, *args)
##def resonators(bot, event, *args): yield from sl(bot, event, 4, *args)
##def bursters(bot, event, *args): yield from sl(bot, event, 5, *args)
##def keys(bot, event, *args): yield from sl(bot, event, 6, *args)
##def linking(bot, event, *args): yield from sl(bot, event, 7, *args)
##def fielding(bot, event, *args): yield from sl(bot, event, 8, *args)
##def defensemods(bot, event, *args): yield from sl(bot, event, 9, *args)
##def hackmods(bot, event, *args): yield from sl(bot, event, 10, *args)
##def linkamps(bot, event, *args): yield from sl(bot, event, 11, *args)
##def leveling(bot, event, *args): yield from sl(bot, event, 12, *args)
##def mu(bot, event, *args): yield from sl(bot, event, 13, *args)
##def cubes(bot, event, *args): yield from sl(bot, event, 14, *args)
##def farming(bot, event, *args): yield from sl(bot, event, 15, *args)
##def terms(bot, event, *args): yield from sl(bot, event, 16, *args)
##def virus(bot, event, *args): yield from sl(bot, event, 17, *args)
##def placement(bot, event, *args): yield from sl(bot, event, 18, *args)
##def campfire(bot, event, *args): yield from sl(bot, event, 19, *args)
##def ultrastrikes(bot, event, *args): yield from sl(bot, event, 20, *args)
##def anomaly(bot, event, *args): yield from sl(bot, event, 21, *args)
##def smartfarming(bot, event, *args): yield from sl(bot, event, 22, *args)
##def capsules(bot, event, *args): yield from sl(bot, event, 23, *args)
##def mufg(bot, event, *args): yield from sl(bot, event, 24, *args)
##def softbank(bot, event, *args): yield from sl(bot, event, 25, *args)
##def store(bot, event, *args): yield from sl(bot, event, 26, *args)
##def lawson(bot, event, *args): yield from sl(bot, event, 27, *args)
