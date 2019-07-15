import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import sys
import smtplib
import os
import wolframalpha
global a
a=True

'''This is simple assitant. In this you need to enter wolframalpha ID and also need to enter your Gmail ID in send_mail()'''

############################said#########################
engine=pyttsx3.init()

def say(audio):
    ''' this function makes text to speech'''
    print(audio)
    engine.say(audio)
    engine.runAndWait()

#------------------------------------------------------

##########wolframe alpha###############
client=wolframalpha.Client('''enter_your_wolframe_alpha_here''')

#####################take#############################
def take():
    '''take() is like a main function it listen the voice'''
    r=sr.Recognizer()    
    with   sr.Microphone() as source:
        print('listening....')
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print(text)
            Text= text.lower()
            main(Text)
        except:
            print('sorry')
##########################new_listen#######################
def new_listen():
    '''this function recognize the voice but it use for email sending'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        audio=r.listen(source)
        try:  
            text=r.recognize_google(audio)
            #print(text)
            Text= text.lower()
            return Text
        except:
            new_listen()
############-###############  send mail fun c#########################
def send_mail(reciever):
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        mymail='your_mail@gmail.com'#here write your own gmail

        with open('pass.txt','r') as f:#i use external txt file for password
            password=f.readline()
    
        server.login(mymail,password)
        say('say message')
        message=new_listen()
        print(message)
        server.sendmail(mymail,reciever,message)        
        say('mail sent')
        server.quit()
    except:
        print('mail not send')

#############################main############################
def main(Text):
    #Text=take()
    global a
    dic={
        'what is your name?':'my name is zarvis',

    }
    if 'abhishek' in Text:
        say('he is boss')
    
    elif 'hello' in Text or 'omega'==Text:
        say('hi sir! how may i help you ?')
    
    elif 'exit' in Text:
        say('see you later')
        quit()
        sys.exit()
    
    elif 'open' in Text:
        #print(Text.find('open'))
        ans=Text[Text.find('open')+5:]
        say(f'opening {ans}')
        wb.open(f'http://www.{ans.replace(" ","")}.com')
    
    elif 'on google' in Text:
        say('searching on google')
        wb.open(Text.replace('on google',''))        
    
    elif 'what is' in Text or 'who' in Text:
        say('searching!')
        ans=wikipedia.summary(Text,sentences=2)
        say(ans)
    
    elif 'image' in Text:
        link=Text.replace('image','')
        say('opening image')
        wb.open(f'https://www.google.com/search?tbm=isch&source=hp&biw=1536&bih=722&ei=wBEWXe3qB9K7rQHU46joBQ&q={link}&oq=amitbchchan&gs_l=img.3..0l10.8210.15359..17495...3.0..1.365.2771.0j2j6j3......0....1..gws-wiz-img.....0..35i39.OxGpGdUWEg4')
    
    elif 'email' in Text:
        say('what you want write gmail or  say gmail')
        while True:
            
            ask=new_listen()
            print(ask)
            if 'write' in ask:
                say('alright')
                reciever=input('enter Gmail>')
                send_mail(reciever)
                break
            elif 'say' in ask:
                say('say reciever gmail')
                reciever=new_listen().replace(' ','')
                print(reciever)
                send_mail(reciever)
                break
            else:
                print('say again')

    elif 'play' in Text:
        #song=Text.find('play').replace(' ','-')
        wb.open(f"""https://www.jiosaavn.com/search/{Text.replace('play','').replace(' ','-')}""")
    elif 'bye' in Text or 'stop' in Text:
        a=False
        say('thankyou!')
    else:
        try:
            ans=client.query(Text)
            res=next(ans.results).text
            say(res)
        except:
            say('opening google')
            search=Text.replace(' ','')
            wb.open(f"https://www.google.com/search?source=hp&ei=zloXXeSHMJjorQH52J_ACA&q={search}&oq=bhopal&gs_l=psy-ab.3..0l2j0i131j0l7.1770.3077..3740...0.0..0.291.1443.0j4j3......0....1..gws-wiz.....0..35i39.ZRWvFIYZ2mA")
        
if __name__=="__main__":
    say('hello Boss!')
    a=True
    while a==True:
        say('ask somthing!')    
        take()
