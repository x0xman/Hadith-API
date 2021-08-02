import os
import re
import json
import time
import telebot
from pathlib import Path
import schedule, threading
from fetch import Hadith_api
from dotenv import load_dotenv
from exceptions import NotFoundEnvironmentVariables
from exceptions import JSONDecodeErrorException


"""
  :func Initializer_json() 
    :description load config.json file to get the objects 
    :param object [str] 
"""

def Initializer_json ( object : str ) -> str :
    try :
        config = open ( "config.json" , mode="r" , encoding="UTF-8" )
        return json.load(config)[object]
    except json.decoder.JSONDecodeError:
        raise JSONDecodeErrorException(
           " Exception :: Error - For the solution ? -> https://stackoverflow.com/a/18460958/15710731 "
        )
    

class schedule_textmessage_telegramApi(object):
    def __init__(self):
        self.tele_bot = telebot.TeleBot(get_environment_variables("TOKEN_API"))
        self.seconds_context_hadith : int = 59 # 59  seconds | change if you want 
        self.minutes_context_hadith : int = 60 * 30 # change if you want 
        self.hours_context_hadith   : int = 60 * 60 # change if you want 
        schedule.every(3).seconds.do(self.style_by_context())
        self.start_schedule()
    """
    :description this function will be used schedule for hadith context 
    :func start_schedule [self]
    """
    #@classmethod
    def start_schedule(self):
        while True:
          schedule.run_pending()
          time.sleep(1)
    """
    :description this function will be used threading
    :func start_threading [self]
    """
    def start_threading(self):
        thread = threading.Thread(target=self.start_schedule())
        thread.start()

    """
    :description style by context to send hadith context 
    :func style_by_context [self]
    """
    def style_by_context (self , HadithAPI : Hadith_api.context_hadith_api() ) -> str :
        self.context : str = f"""{HadithAPI}"""
        #self.tele_bot.send_message()
        return self.context


"""
  :func environment_variables()
    :description Environment variables is the set of key-value pairs for the current user environment. 
                They are generally set by the operating system and the current user-specific configurations
    :param variables [str] 
"""

def get_environment_variables( variables : str ) -> str :  
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    try:
        token_telegram : str = os.getenv(variables)
        if token_telegram:     
           return token_telegram
        else:
           return " [-] is Empty [-] "
    except:
        raise NotFoundEnvironmentVariables (
             " Exception :: NotFound Environment Variable  "
            )

# telebot 
token_bot = telebot.TeleBot(get_environment_variables("TOKEN_API"))

"""
  :func parser_json 
    :param keys [str] : Get objects json from 'config.json'

"""
def parser_json (keys : str  , user_id : str ) -> str :
    try:
        with open("config.json" , mode="r" , encoding="UTF-8" ) as json_file:
            json_loads = json.load(json_file)
            if keys == "add_user_id"    :      json_list : list = [];json_loads["USERNAME_ID"].append(user_id);json_list.append(json.dumps(json_loads));open("config.json" , mode="w").write(json_list[0]);return "[+] The user has been added 100% [+]"
            if keys == "support"        :      return json_loads['support']
            if keys == "add_vists"      :      json_loads["vists"] = int(json_loads["vists"]) + 1 ; open("config.json" , mode="w" ).write(json.dumps(json_loads))
            if keys == "information"    :      info_vist : int = 0 ; info_users : int = 0 ; info_vist += json_loads['vists'] ; info_users += len(json_loads['USERNAME_ID']);text = f"""Users : {info_users} \nVists : {info_vist} \n """ ; return text
            if keys == "add_owner"      :      json_list : list = [] ; json_loads["Owner"].append(user_id) ; json_list.append(json.dumps(json_loads));open("config.json" , mode="w").write(json_list[0]);return "[+] The user has been added 100% [+]"
  
    except json.decoder.JSONDecodeError:
        raise JSONDecodeErrorException(
           " Exception :: Error - For the solution ? -> https://stackoverflow.com/a/18460958/15710731 "
        )

"""
- Test 
"""
@token_bot.message_handler(commands=["test"])
def testing(message):
    token_bot.reply_to(message , message.chat.id )

"""
  Add owner in 'config.js'
  Args:
     :decorator [token_bot] : message_handler [commands]
     :func administrator [message : str ] 
"""
@token_bot.message_handler( commands = ["Owner"] )
def administrator(message):
    if len("/Owner") < 8 :
       is_user = message.chat.id if message.chat.id in Initializer_json("Owner") else message.chat.username
       if isinstance (is_user , int ) and int ( is_user ) in Initializer_json("Owner") or str( "@" + is_user ) in Initializer_json("Owner") :
          get_username = re.findall(r"[@].+" , message.text )[0]
          parser_json("add_owner" , get_username )
          token_bot.reply_to ( message , " [+] تمت الاضافة الى الادارة [+]")
       else:
          token_bot.reply_to ( message , " [-] Not allowed [-]" )
    else:
       token_bot.reply_to ( message , 'يجب ان تتبع هذه الخطوات : \n     - عندما تُريد اضافة عضو في الادارة : "/Owner @username"' )
              
"""
  Add user in 'config.js'
  Args:
     :decorator [token_bot] : message_handler [commands]
     :func join_new_memeber [message : str ] 
"""
@token_bot.message_handler( commands = ["join"] )
def join_new_memeber(message):
    is_user : str = message.chat.id
    if int(is_user) not in Initializer_json("USERNAME_ID") or int(message.chat.id) not in Initializer_json("USERNAME_ID"):
       print(Initializer_json("USERNAME_ID"))
       add_new_user = parser_json("add_user_id" , int(message.chat.id) )
       token_bot.reply_to(message , "[+] تمت اضافتك في قائمتنا [+]")
    else:
       token_bot.reply_to(message , "[-] لقد تمت اضافتك من قبل :( [-]")
    
"""
  Get the infromation from 'config.js' | the infromation is usernames and number of vists
  Args:
     :decorator [token_bot] : message_handler [commands]
     :func information [message : str ] 
"""

@token_bot.message_handler( commands = [ "information" ] )
def information (message):
    is_user = message.chat.id 
    if is_user in Initializer_json("Owner"):
        token_bot.reply_to(message  , parser_json("information" , False ) )
    else: 
        token_bot.reply_to(message ,  " Not Allowed " )
    
"""
  Get the help you need .
     :decorator [token_bot] : message_handler [commands]
     :func support [message : str ] 
"""
@token_bot.message_handler( commands = ["support"] )
def support(message):
    if message: 
       token_bot.reply_to(message , parser_json("support" , False ) + "\n [ تواصل معنا ]" )
    else:
       return  

"""
  Enter information (number of visits, usernames , list commands )
     :decorator [token_bot] : message_handler [commands]
     :func options_to_help [message : str ] 
"""
@token_bot.message_handler(commands = ["start" , "help"] )
def options_to_help(message):
    is_user = message.chat.username or message.chat.id
    add_vists : str = parser_json("add_vists" , False )
    if str(is_user) in str("@") + str(Initializer_json("Owner")) or is_user in list(map(lambda get : "@" + str (get) , Initializer_json("Owner"))) or is_user in Initializer_json("Owner"):
        token_bot.reply_to(message , 
                """/support - للتواصل والدعم \n/join - للانضمام للبوت \n/information - الاحصائيات والمعلومات\n/Owner - اضافة اعضاء للأدارة 
        """)
    else: 
       token_bot.reply_to(message , " /support  - للتواصل والدعم \n/join - للانضمام للبوت ")


token_bot.polling()
