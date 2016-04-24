# Ingress Checkpoints plugin for hangupsbot
# The command "/bot cp [day]" will print checkpoints for the given day of the week. If no day is given, it returns today's checkpoints. Case insensitive, partial ok (Mon, Monday and mon all work). [day] can also be tmrw or tomorrow. example usage: cp tmrw, cp tue

from datetime import datetime,timedelta

def _initialise(Handlers, bot=None):
    Handlers.register_user_command(["cp"])
    Handlers.register_user_command(["checkpoint"])
    Handlers.register_user_command(["checkpoints"])
    return []

def cp(bot=None,event=None,day='today'):
    """
    Print checkpoints for the given day of the week. If no day is given, it returns today's checkpoints. Case insensitive, partial ok (Mon, Monday and mon all work). [day] can also be tmrw or tomorrow. example usage: cp tmrw, cp tue
    """
    day = day.lower()
    days = {"mon":0, "tue":1, "wed":2, "thu":3, "fri":4, "sat":5, "sun":6}
    reference = datetime(2015,3,7,1) # An arbitrary checkpoint in the past in UTC
    utc_offset = round((datetime.now()-datetime.utcnow()).total_seconds())
    reference += timedelta(seconds=utc_offset) # Convert to localtime
    
    today = datetime.now()
    today = datetime(today.year,today.month,today.day) # Discard time data
    
    hours = int((today - reference).total_seconds()/60/60/5)*5
    
    cp = reference + timedelta(hours=hours) # The checkpoint right before today
    
    short_day = day[:3]
    
    if short_day=='tod':
        d=today.weekday()
    elif short_day=='tmr' or short_day=='tom':
        d=(today.weekday()+1)%7
    else:
        if short_day not in days:
            bot.send_message(event.conv,"No match for {}. Valid options are (Mon,Tue,Wed,Thu,Fri,Sat,Sun)".format(day))
            return
        d=days[short_day]
    while cp.weekday()!=d: # fast forward to the requested day
        cp += timedelta(hours=5)
    results = []
    results.append(cp.strftime('%H%Mhrs'))
    while cp.weekday()==d:
        cp += timedelta(hours=5)
        results.append(cp.strftime('%H%Mhrs'))
    result = "Checkpoints for {}: {}".format(day,",".join(results))
    bot.send_message(event.conv, result)

def checkpoint(bot=None,event=None,day='today'):
    """
    Print checkpoints for the given day of the week. If no day is given, it returns today's checkpoints. Case insensitive, partial ok (Mon, Monday and mon all work). [day] can also be tmrw or tomorrow. example usage: cp tmrw, cp tue
    """
    cp(bot,event,day)

def checkpoints(bot=None,event=None,day='today'):
    """
    Print checkpoints for the given day of the week. If no day is given, it returns today's checkpoints. Case insensitive, partial ok (Mon, Monday and mon all work). [day] can also be tmrw or tomorrow. example usage: cp tmrw, cp tue
    """
    cp(bot,event,day)
