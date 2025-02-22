from tts import TTS
from listining import Listining
from model_llm import Models
from details import utils
from gmail import SendMail

sm=SendMail()
Utils=utils()
speak=TTS()
listen=Listining()
model=Models()

def main():
    greetings="Hello! how are you doing. I'm from ABC company. I'm here as your tour service agent."
    responce_1=model.conversation(greetings)
    print(responce_1)
    speak.Speak(responce_1)
     ## greetings
    try:
          text_1=listen.Listen()
          print(text_1)

    except FileNotFoundError:
        speak.Speak("Didn't get it. speak again.....")
        return 
    
    #starting 
    text_i='I need few details from you so that i can design a perfect trip plan for you.'
    reprase_st=model.conversation(text_i)
    speak.Speak(reprase_st)

    #may i know your name
    text_name='first thing first may i know your name.'
    rephrase_name=model.conversation(text_name)
    speak.Speak(rephrase_name)
    while True:
        try:
            list_name=listen.Listen()
            name=model.Retrive(list_name)
            print(name)
            break
        except FileNotFoundError:
            speak.Speak("Didn't get it. speak again.....")
        except Exception as e:
            print(e)
            speak.Speak("Some error has occured getting starting location.")
            return
    #getting from address
    text_where='where are you from. and is it the location you are gona take off your flight.'
    resprase_or=model.conversation(text_where)
    speak.Speak(resprase_or)
    while True:
        try:
            list_wh=listen.Listen()
            From=model.Retrive(list_wh)
            print(From)
            break
        except FileNotFoundError:
            speak.Speak("Didn't get it. speak again.....")
        except Exception as e:
            print(e)
            speak.Speak("Some error has occured getting starting location.")
            return
    #get To address
    text_to="where do you to plan to go for the trip."
    reprase_to=model.conversation(text_to)
    speak.Speak(reprase_to)
    while True:
        try:
            list_to=listen.Listen()
            to=model.Retrive(list_to)
            print(to)
            break
        except FileNotFoundError:
            speak.Speak("Didn't get it. speak again.....")
        except Exception as e:
            print(e)
            speak.Speak("Some error has occured getting starting location.")
            return
    # date
    text_d="when are you planing your trip."
    rephrase_d=model.conversation(text_d)
    speak.Speak(rephrase_d)
    while True:
        try:
            list_d=listen.Listen()
            d=model.Retrive(list_d)
            print(d)
            break
        except FileNotFoundError:
            speak.Speak("Didn't get it. speak again.....")
        except Exception as e:
            print(e)
            speak.Speak("Some error has occured getting starting location.")
            return
    #adults
    text_a="how many people and going for this trip. And how many of them are adults"
    rephrase_a=model.conversation(text_a)
    speak.Speak(rephrase_a)
    while True:
        try:
            list_a=listen.Listen()
            a=model.Retrive(list_a)
            print(a)
            break
        except FileNotFoundError:
            speak.Speak("Didn't get it. speak again.....")
        except Exception as e:
            print(e)
            speak.Speak("Some error has occured getting starting location.")
            return
    #childs
    text_c="And how many childs"
    rephrase_c=model.conversation(text_c)
    speak.Speak(rephrase_c)
    while True:
        try:
            list_c=listen.Listen()
            c=model.Retrive(list_c)
            print(c)
            break
        except FileNotFoundError:
            speak.Speak("Didn't get it. speak again.....")
        except Exception as e:
            print(e)
            speak.Speak("Some error has occured getting starting location.")
            return
    # Done

    text_end="that's all the questions from me. I will be mailing you the trip details."
    responce_end=model.conversation(text_end)
    speak.Speak(responce_end)
    From,_=Utils.iATA(From)
    to,lat_lon=Utils.iATA(to)

    flight_details=Utils.getFlights(From=From,destination=to,date=d,adults=int(a),childs=int(c))
    hotel_details=Utils.getHotels(to)
    
    # mail
    Subject,Body=model.GenerateMail(From,to,d,hotel_details,flight_details)
    sm.sendMail(Subject,Body)

if __name__=='__main__':
    main()