#########raspbian stretch, Buster updated installation
#IN THE TERMINAL...
#sudo apt install python3-espeak speech-dispatcher-espeak

###########################SOME DEFAULT CUSTOM OPTIONS.
#####################ACCENTS
#CAN COME IN HANDY FOR WHEN YOU WANT TO APPLY OTHER LANGUAGES TO ESPEAK
#OR TO SIMPLY GIVE YOUR COMPUTER A MORE DISTINCTIVE SOUND
USA='en-us1'
SCOTTS='en-sc'
AFRIKA='af'
ITALIA='it'
GERMAN='de'
SPAIN='es'
FRENCH='fr'
POLISH='pl'
PORT='pt'
ROMANIAN='ro'
TURKISH='tr'
LATIN='la'#???
########################################################DEFAULT VOICES
#CUSTOMIZE
#CHANGE THE 'USA' VARIABLE WITH ONE OF THE ABOVE OPTIONS TO CHANGE VOICE SETTINGS
#AND THE NUMERIC VALUES BELOW THE SPEED, PITCH, VOLUME AND TEXT COMMENTS FOR MORE PERSONALIZED CUSTOMIZATION SETTINGS

def say(something):
    try:
        import subprocess#custom options-  accent,   speed,     pitch,    volume     text to speak
        voice1=subprocess.Popen(["espeak", "-v", USA,"-s",'175',"-p",'45',"-a",'80', something])
    except Exception as e:
        print(e)

##################TEXT VARIABLE. NOT TOTALLY NECCESSARY BUT CAN BE USEFUL IN THE LONG RUN.
port='hey how have you been?'

say(port)
#OR
#say('hey how have you been?')

