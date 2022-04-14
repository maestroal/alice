
#!/bin/usr python3
# -*- coding:utf-8 -*-
#
# Broh, jangan kau sakiti Alice, perbaiki dia, dia akan nurut kepadamu:)
# Don't forget to star and donate broh
# I am on Instagram: @maestroal.dev dont forget follow

import os;
import sys;
import gtts;
import random;
import pyttsx3;
import datetime;
import playsound;
import webbrowser;
import speech_recognition;

MASTER = [];
NAME_AI = [];
DATA_DAYS = [];
HOUR = datetime.datetime.now().hour;
globals; MASTER, NAME_AI, DATA_DAYS, HOUR;

class engine:
    def __init__(self, MASTER_NAME=None, AI_NAME=None):
        if(MASTER_NAME==None):
            MASTER.append('Maestro Alvardo');
        else:
            MASTER.append(MASTER_NAME);
        if(AI_NAME==None):
            NAME_AI.append('Alice');
        else:
            NAME_AI.append(AI_NAME);
        # DAYS ADD
        if(HOUR > 0 and HOUR <= 11):
            DATA_DAYS.append("morning");
        elif(HOUR > 11 and HOUR <= 14):
            DATA_DAYS.append("day");
        elif(HOUR > 14 and HOUR <= 18):
            DATA_DAYS.append("evening");
        elif(HOUR > 18 and HOUR <= 24):
            DATA_DAYS.append("night");
        else:
            DATA_DAYS.append("unknown days");
        return None;
    
    def start(self):
        self.saySomethings = [
            #"i love you sir",
            "whats your command",
            "i'll help you everyday sir",
            "don't forget to be grateful today",
            "i  will try to help you as best I can",
            "give me your order"
        ];
        self.saySomething = random.choice(self.saySomethings);
        if(DATA_DAYS[0] == "morning"):
            self.sayWelcome = "Good morning, {}. {}".format(MASTER[0], self.saySomething);
        elif(DATA_DAYS[0] == "day"):
            self.sayWelcome = "Good day, {}. {}".format(MASTER[0], self.saySomething);
        elif(DATA_DAYS[0] == "evening"):
            self.sayWelcome = "Good evening, {}. {}".format(MASTER[0], self.saySomething);
        elif(DATA_DAYS[0] == "night"):
            self.sayWelcome = "Good night, {}. {}".format(MASTER[0], self.saySomething);
        else:
            self.sayWelcome = "{}".format(self.saySomething);
        self.aliceSpeak("{}".format(self.sayWelcome));
        try:
            while(True):
                self.dataVoice = self.listenMe("");
                print("{}: {}".format(MASTER[0], self.dataVoice));
                self.respond(self.dataVoice);
        except (KeyboardInterrupt, EOFError):
            exit("[!] Aborted...");
    
    def aliceSpeak(self, text):
        self.text = str(text);
        self.pyttsxEngine = pyttsx3.init();
        self.pyttsxEngine.say(self.text);
        self.pyttsxEngine.runAndWait();
    
    def aliceSpeak(self, audioString):
        self.audioString = str(audioString);
        self.textToSpeech = gtts.gTTS(
            text=self.audioString,
            lang='en',
            slow=False
        );
        self.randomNumber = random.randint(6, 666000000);
        self.audioSaved = "audio-{}.mp3".format(self.randomNumber);
        self.textToSpeech.save(self.audioSaved);
        playsound.playsound(self.audioSaved)
        print("{}: {}".format(NAME_AI[0], audioString));
        os.remove(self.audioSaved);
    
    def listenMe(self, ask=""):
        self.rec = speech_recognition.Recognizer();
        with speech_recognition.Microphone() as self.source:
            if(ask):
                self.aliceSpeak(ask);
            self.myAudio = self.rec.listen(self.source, 5, 5);
            print("{}: done listening.".format(NAME_AI[0]));
            self.dataVoice = 'not speak';
            try:
                self.dataVoice = self.rec.recognize_google(self.myAudio);
            except speech_recognition.UnknownValueError:
                self.aliceSpeak('hmm');
            except speech_recognition.RequestError:
                self.aliceSpeak('Sorry sir, alice is down');
            return self.dataVoice.lower();

    def thereExists(self, terms, dataVoice):
        for term in terms:
            if(term in dataVoice):
                return dataVoice;

    def respond(self, dataVoice):
        self.specialChar = "what's";
        if(self.thereExists(['hello', 'hai', 'hallo', 'hi', 'whats up', 'hey whats up', self.specialChar+' up'], dataVoice)):
            self.saySomethings = [
                'Hello sir, how are you?',
                'Yes sir, i am here',
                'I am here sir, whats you command?',
                'good {} sir, i  am here'.format(DATA_DAYS[0]),
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['good morning'], dataVoice)):
            if(DATA_DAYS[0] != 'morning'):
                self.saySomethings = [
                    'sorry sir, now is {}'.format(DATA_DAYS[0]),
                    'now is {} sir'.format(DATA_DAYS[0]),
                    'hmm, sorry sir now is no morning days, now is {}'.format(DATA_DAYS[0])
                ];
                self.saySomething= random.choice(self.saySomethings);
            else:
                self.saySomethings = [
                    'Hello sir, how are you?',
                    'Yes sir, i am here',
                    'I am here sir, whats you command?',
                    'good {} sir, i  am here'.format(DATA_DAYS[0]),
                ];
                self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['good day'], dataVoice)):
            if(DATA_DAYS[0] != 'day'):
                self.saySomethings = [
                    'sorry sir, now is {}'.format(DATA_DAYS[0]),
                    'now is {} sir'.format(DATA_DAYS[0]),
                    'hmm, sorry sir now is no days, now is {}'.format(DATA_DAYS[0])
                ];
                self.saySomething= random.choice(self.saySomethings);
            else:
                self.saySomethings = [
                    'Hello sir, how are you?',
                    'Yes sir, i am here',
                    'I am here sir, whats you command?',
                    'good {} sir, i  am here'.format(DATA_DAYS[0]),
                ];
                self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['good evening'], dataVoice)):
            if(DATA_DAYS[0] != 'evening'):
                self.saySomethings = [
                    'sorry sir, now is {}'.format(DATA_DAYS[0]),
                    'now is {} sir'.format(DATA_DAYS[0]),
                    'hmm, sorry sir now is no evening days, now is {}'.format(DATA_DAYS[0])
                ];
                self.saySomething= random.choice(self.saySomethings);
            else:
                self.saySomethings = [
                    'Hello sir, how are you?',
                    'Yes sir, i am here',
                    'I am here sir, whats you command?',
                    'good {} sir, i  am here'.format(DATA_DAYS[0]),
                ];
                self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['good night'], dataVoice)):
            if(DATA_DAYS[0] != 'night'):
                self.saySomethings = [
                    'sorry sir, now is {}'.format(DATA_DAYS[0]),
                    'now is {} sir'.format(DATA_DAYS[0]),
                    'hmm, sorry sir now is no night days, now is {}'.format(DATA_DAYS[0])
                ];
                self.saySomething= random.choice(self.saySomethings);
            else:
                self.saySomethings = [
                    'Hello sir, how are you?',
                    'Yes sir, i am here',
                    'I am here sir, whats you command?',
                    'good {} sir, i  am here'.format(DATA_DAYS[0]),
                ];
                self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['i am fine', 'i  fine', 'fine and you', 'fine and you', "i'm fine thank you"], dataVoice)):
            self.saySomethings = [
                'thank you sir',
                'me too, thank you sir',
            ];
            self.saySomething = random.choice(self.saySomethings);
        
        elif(self.thereExists(['how are you', 'how are you doing'], dataVoice)):
            self.saySomethings = [
                'i am fine sir, and you?',
                'fine sir, how about you?',
                'allways fine sir, how about you?',
                'good sir, and you?'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['you are welcome', 'no problem'], dataVoice)):
            self.saySomethings = [
                'oke sir',
                'fine sir',
                'yes sir'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['tell me your name', 'tell me you name', '{} you name'.format(self.specialChar), '{} your name'.format(self.specialChar)], dataVoice)):
            self.saySomethings = [
                'my name is {} sir, you made it'.format(NAME_AI[0]),
                '{} is my name. you are made it sir'.format(NAME_AI[0]),
                'you made my name is {} sir'.format(NAME_AI[0])
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['tell me you developers', 'who is you developer', 'tell me your developers', 'who is your developers', 'who is you developer'], dataVoice)):
            self.saySomething = "Maestro Alvardo is my developer";
        elif(self.thereExists(['tell my name', '{} my name'.format(MASTER[0]), 'what is my name'], dataVoice)):
            self.saySomethings = [
                '{} is your name sir'.format(MASTER[0]),
                'your name is {}'.format(MASTER[0]),
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['{} time now'.format(self.specialChar), 'what time now', 'tell me the time'], dataVoice)):
            self.saySomethings = [
                'now is {} pass {} sir'.format(datetime.datetime.now().hour, datetime.datetime.now().minute),
                'its {} pass {} sir'.format(datetime.datetime.now().hour, datetime.datetime.now().minute)
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['open youtube'], dataVoice)):
            webbrowser.get().open('https://m.youtube.com/');
            self.saySomethings = [
                'opening youtube',
                'youtube is opening'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['good bye', 'see you', 'stop', 'goodbye'], dataVoice)):
            self.saySomethings = [
                'good bye sir',
                'good bye {}. i will waiting you here'.format(MASTER[0]),
                'oke good bye {}. see you again'.format(MASTER[0]),
                'see you again {}. good bye'.format(MASTER[0])
            ];
            self.saySomething = random.choice(self.saySomethings);
            self.aliceSpeak(self.saySomething);
            exit("bye");
        elif(self.thereExists(['do you have a boyfriend', 'do you have a boyfriends', 'do you have boyfriend', 'do you have boyfriends', 'who is your boyfriend', 'tell me your boyfriend', 'who is you boyfriend', 'tell me you boyfriend', 'who is you lover', 'who is your lover'], dataVoice)):
            self.saySomethings = [
                'i no have a boyfriend sir',
                'hmm, i dont have',
                'sir, i dont have this'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['do you want to be my boyfriend', 'will you be my lover', 'woud you be my lover', 'marry me', 'to me my wife'], dataVoice)):
            self.saySomethings = [
                'sorry sir i can not',
                'i am really sorry sir, i can no',
                'let me to be you assistant sir'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['do you want to be'], dataVoice)):
            self.saySomethings = [
                'sorry sir let me be you assistant',
                'i not will be anything, i will be you assistant sir',
                'i am you assistant sir'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(['do you like '], dataVoice)):
            self.uSay = dataVoice.split('do you like');
            self.resUSay = self.uSay[1];
            if(self.resUSay in [' coffee', ' coca-cola', ' pepsi', ' lemon tea', ' lemontea', 'pizza', 'hamburger', 'cake', 'biscuit']):
                self.saySomethings = [
                    'i can not to drink or eat anything sir',
                    'i am a robot sir, i can not drink or eat anything',
                    'sorry sir, i am a robot, can not to drink and eat anything',
                ];
                self.saySomething = random.choice(self.saySomethings);
            elif(self.resUSay in ['me', 'myself']):
                self.saySomethings = [
                    'i like you sir, you are so funny',
                    'yes i  like you sir'
                ];
                self.saySomething = random.choice(self.saySomethings);
            elif(self.resUSay in ['her', 'him', 'they', 'she', 'he']):
                self.saySomething = "i dont know who sir";
            else:
                self.saySomething = "i dont know sir. i dont like anythin, just like for help you";
        
        elif(self.thereExists(['search'], dataVoice)):
            self.uSay = dataVoice.split('search');
            webbrowser.get().open('https://google.com/search?q={}'.format(self.uSay[1]));
            self.saySomething = "there is i found in google sir";
        elif(self.thereExists(['not speak'], dataVoice)):
            self.saySomethings = [
                'hello sir, what do you still there?',
                'i can not hear you sir, please speak clear voice',
                'sorry sir, please speak clear voice, i can not hear you',
                'sir, do you still there?'
            ];
            self.saySomething = random.choice(self.saySomethings);
        elif(self.thereExists(["i'm here"], dataVoice)):
            self.saySomethings = [
                'oke sir, whats you command?',
                'tell me you order sir',
                'let me help you do something sir'
            ];
            self.saySomething = random.choice(self.saySomethings);
        else:
            self.saySomethings = [
                'i am no understand sir',
                'sorry sir i am no understand',
                'i am no understand you order sir',
                'i am really no understand sir'
            ];
            self.saySomething = random.choice(self.saySomethings);

        self.aliceSpeak(self.saySomething);


# end of lines
