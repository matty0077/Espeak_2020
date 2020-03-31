#########raspbian stretch, Buster installation
# in the terminal...
#sudo apt install python3-espeak speech-dispatcher-espeak

#########################################################MBROLA VOICE OPTIONS
#####################ACCENTS
#CAN COME IN HANDY FOR WHEN YOU WANT TO APPLY OTHER LANGUAGES TO ESPEAK
#OR TO SIMPLY GIVE YOUR COMPUTER A MORE DISTINCTIVE SOUND
MBUSA='mb-en1'
MBGERMAN='mb-de4-en'
################VOICE VARIATION EXAMPLES
#FOR FURTHER CUSTOMIZATION
##################MALE VARIATIONS
VARM1='+m1'
VARM2='+m2'
VARM3='+m3'
VARM4='+m4'
VARM5='+m5'
VARM6='+m6'
VARM7='+m7'
################FEMALE VARIATIONS
VARF1='+f1'
VARF2='+f2'
VARF3='+f3'
VARF4='+f4'
VARF5='+f5'

#######################SPEAK FUNCTION
#TO CUSTOMIZE:
#CHANGE THE 'MBUSA' AND THE 'VARF2' VARIABLES WITH ONE OF THE ABOVE OPTIONS TO CHANGE VOICE SETTINGS
#AND THE NUMERIC VALUES BELOW THE SPEED, PITCH, VOLUME AND TEXT COMMENTS FOR MORE PERSONALIZED CUSTOMIZATION SETTINGS
def Msay(something):
    try:
        import subprocess#custom options-  accent,           speed,     pitch,    volume     text to speak
        voice1=subprocess.Popen(["espeak", "-v", MBUSA+VARF2,"-s",'175',"-p",'45',"-a",'80', something])
    except Exception as e:
        print(e)

##################TEXT VARIABLE. NOT TOTALLY NECCESSARY BUT USEFUL IN THE LONG RUN.
port='hey how have you been?'

##RUN THE PROGRAM
Msay(port)
#or
#Msay('hey how have you been?')

