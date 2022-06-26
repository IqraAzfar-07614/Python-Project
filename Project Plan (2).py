#Central Idea

import time
import math
import random

def main():
    competition_results.clear()
    print("Welcome to AIR Typing Test. This is a tool designed to test and improve your typing speed through practice!")
    print("Please select the mode. The available modes are 'Practice' and 'Competition'.\nFor More Information, please enter 'info'")
    comp=comparison(["practice","competition","info"])
    f_select(comp)
    print("Thank you very much for considering AIR Typing Test. Would you like to return to Main Menu? Yes or No? ")
    while True:
        message=input().lower().strip()
        if message=="yes":
            return main()
        elif message=="no":
            break
    print("Would You like to give us some feedback? Yes or No? Entering 'No' will close the application! ")
    while True:
        message2=input().lower().strip()
        if message2=="yes":
            user_feedback()
            break
        elif message2=="no":
            return
    access=input("Press Enter to close the application: ")
    if access=="Admin":
        password=input("Enter Your Password! Incorrect Password will Clear the Data: ")
        if password=="090078601":
            print("Game Ratings: {} Result Accuracy Rating: {} Template Rating: {} Suggestion: {}".format(feedback_list[0],feedback_list[1],feedback_list[2],feedback_list[3]))
            return
        else:
            print("Wrong Password! Removing Data...Reset Complete...\nTerminating Program....")
            feedback_list.clear()
            return
    return

    #Feedback function will ask for ratings on a scale of 1-5 for various aspects such as rating the templates, how accurate do you think the results were.
    #Lastly, it should ask for a string input, on 'How do you think we can further improve our tool?'
    #Also check that appropriate error checking is involved

def comparison(mode_list):
    comp=False
    while type(comp)==bool:
        first_selection=input("Your mode is: ").lower().strip()
        if first_selection not in mode_list:
            comp=False
        else:
            for x in range(len(mode_list)):
                if first_selection==mode_list[x]:
                    comp=x+1
    return comp
    
def f_select(comp): #Modify this function if you add new modes
    if comp==1:
        practice_mode(False,True)
    elif comp==2:
        print()
        print("Welcome to Competition Mode! You will be asked some information about the contestants first ")
        participants=input("Please enter the number of participants in this competition: ").strip()
        if not (participants.isnumeric()):
            return f_select(comp)
        if int(participants) > 10 or int(participants) <2 :
            return f_select(comp)
        competition_mode(int(participants))
    elif comp==3:
        information()
        
def level_authentication(level):
    if level.isnumeric()==False:
        print("Invalid Input. Please ensure that the input is an integer! ")
        print()
        return level_authentication(input("Please choose a Difficulty Level between 1 and 4: ").strip())
    level=int(level)
    if level not in range(1,5):
        print()
        return level_authentication(input("Please enter a valid Level. Choose a difficulty level between 1 and 4").strip())
    return level

def practice_mode(defined_level,level_ammendment):
    if defined_level==False:
        level=level_authentication(input("Please choose a Difficulty Level between 1 and 4: ").strip())     
    else:  #For Competition Mode
        level=defined_level
        
    template=difficulty_level(level)
    wordcount=len(template.split())
    
    #start user typing and timer
    while True:
        input("Press enter to start the game: ")
        print("\nType the following message: ")
        print(template)
        t0 = time.time()
        input_para = str(input("Start Typing: "))
        t1 = time.time()
        timetaken = t1-t0
        wpm = (wordcount/timetaken)*60
        raw_speed=math.floor(wpm)
        acc = accuracy_check(input_para, template, wordcount)
        if acc==0:
            wpm="Not plausible due to 0% Accuracy"
        else:
            wpm=str(math.floor(wpm*acc))+" WPM"
        user_result=[raw_speed, wpm, acc*100,round(timetaken,2)]
        print("Raw Speed: {} WPM  |||  Effective Speed: {}  |||  Accuracy: {}%  |||  Time Taken: {} Seconds.".format(raw_speed,wpm,acc*100,round(timetaken,2)))
        while True:
            message = str(input("\nPlay again: Yes or No? ")).lower().strip()
            if message == "no":
                competition_results.append(user_result)
                return
            elif message == "yes":
                if level_ammendment==True:
                    message2 = input("\nContinue on The Same Level: Yes or No? ").lower().strip()
                    if message2 == "no":
                        return practice_mode(False, True)
                    elif message2=="yes":
                        break
                    else:
                        print("Invalid input. Please enter a valid answer")
                else:
                    break
            else:
                print("Invalid input. Please enter an appropriate answer")
######
def difficulty_level(level):
    if level==1:
        T1=["my pet cat, jersy is a maine coon cat. it is dark brown and black in colour. she is quite active and playful. she spends most of her time with me and is therefore more affectionate towards me than any of my other family member. many of my friends and neighbours had pets at their home and i also longed to have one. i often told my mother to get home a pup or a kitten and she always dismissed my wish saying she doesn’t have time to look after it.","when my brother went to the hostel for higher studies, i felt quite lonely. my father went to the office and my mother was engrossed in the household tasks most of the times. I did not have anyone to play and felt the need of having a pet all the more. i again requested my parents to get me a pet. looking at how lonely i had grown ever since my brother had gone to the hostel, they decided to fulfil my wish. i was overjoyed at hearing this."]
        template = random.choice(T1)
    elif level ==2:
        T2=["My pet CAT, jerSY is a maine cOOn cat. it is daRK brOwn and blAck in colouR. She is QUITE ACTIVE and playFUL. she spends moST OF her time with Me and IS therefore more AFFectionate towards me than any of my other famILY MeMBer. many of my FRiends and NEIGHhbours had peTS at their hOME and i also longed to have one. i often told my mother to GET hOmE A PuP or a kiTTEN and she alwayS dismissed my wiSH saying she DOEsn’t have time to LOOK AFTeR IT.","When MY BROther went to the hOsTel for Higher Studies, I Felt quite Lonely. My Father wEnT To THE OFFice AND MY MoTHeR wAS EngroSSeD in The houseHOLD tasks most of the times. I did not have anyone to play AND Felt the need of having a pet all the more. i AGAIN ReQuested my parents to GET ME a PET. Looking at how lonely i had gROWN Ever Since MY Brother Had Gone to The Hostel, They Decided To Fulfil My Wish. I Was Overjoyed At hearing this."]
        template = random.choice(T2)
    elif level==3:
        T3=["My pet C@T, jerSY is @ maine c88n cat. !t ~s daRK brOwn and blAck in colouR. $$$ is QUITE ACTIVE and play###. she spends moS^ OF her t!me with Me &&& IS thErEfor! more @FFectionate tow@rds me than any of ; other #famILY MeMBer. m@ny of my FRiends) and NEIGHhbours had peTS ** their hOME and i also longed to have one. i often told my #mOther O GET hOmE @ PuP or @ k!TTEN @nd shE @lw@y$ d!sm!sseD my wiSH sAy!nG she DOEsn’t have time to LOOK AFTeR IT.","When MY BRO**** w#nt to the hOsTel for Higher $tudies, I Felt quite L***ly. M% F%ther wEnT #o THE OFFice @ND () MoTHeR wAS !ngroSSeD in The houseHOLD tasks m@st Of the t!mes. ! ^id not have anYone to play && Felt the need of having a pet @ll the more. i @GAIN ReQuested my p@rents to GET ME @ PET. Looking at h^w lonely i had gROWN Ever Since MY Brother H@d Gone to The Hostel, They Decided To F*****l My Wish. I W@s Overjoyed At hearing this."]
        template = random.choice(T3)
    else:
        T4=["yI.vhdT uitVpO inseGro.Qd . Ods& eofnME @O hhcos!HI.newe mpocEbnU a ed nAm@e  pe r oAD ddOloSlDNe* tt8Ers ir   iEs$Smn Oaao Mte twtoe GnwI Iel!yFs O @a hs#t hy&Tee T E  TTIS eTlmH amtSEe.R  eem ec  ohKrE f  #RwCseo #et $.m P O!OnFof#t o mSLe$ B ’y @R Y^ h~KhlTe @trinarn @@etoab anfn  caaahsEsRT&FIMip# @dor h)hfo  d  yOn@Mut nihrMTmam!im!tb sEFnkC t@nysen8jyid!F*r crlydui nor shng   l e$dwimstheym Nk;Lm hAavtY,td  E aA Goois Pan r E  se  se a!dth o"," osPrTj MSoeee^H geei TT  ntWhe.r   tgt Ts tttnOeRGero ee*n o e  ,H il Iynea ET) f EtB eokAc W n%luY RtMlrpol e fN*NawotYtymAs @ O  HHhn  Tti dih *dv oo#d  ryhOtepch ! v e h !eh*s@.  c *oRhlgtaLGHo  ya@ glM*nsshgTsSntEieil Seve #tvfe et sneil@weleote^e@E$h  oeroOTdahFNooOFyie.*u HpWTmFDeh ae rn&ie, !q ea    e .ta&R t  oir.*u E@LemSy FMheEm.la eD Dn*e*gu nsw hitMedttIdM n e*I@t% doni  B@kLh doh hwi*dD hiWOAOi TYotlGrFhFr s(nshn oe Qsy srtt "]
        template = random.choice(T4) 
    return template

def competition_mode(participant_number):
    print("This competition will be based on the same difficulty level for the entire duration")
    level=level_authentication(input("Please choose a Difficulty Level between 1 and 4: ").strip())
    for x in range(participant_number):
        while True:
            contestant_name=input("Please tell us your name: ").strip()
            if len(contestant_name)>=2:
                break
        competition_results.append(contestant_name)
        print("Well...",contestant_name,"Best of luck with your test!")
        practice_mode(level, False)
    greatest=0
    for x in competition_results:
        if type(x)==str:
            temp=x
            print("Name:",x,end="")
        else:
            if greatest < math.floor(x[0]*x[2]/100):
                greatest=math.floor(x[0]*x[2]/100)
                winner=temp
            print(" || Raw Speed:", x[0], "|| Effective Speed:", x[1], "|| Accuracy:", x[2], "|| Time Taken:", x[3])
            print()

    print("The Winner is:",winner)
    print("With an Effective Speed of: {} WPM".format(greatest))
    print()

        
def accuracy_check(input_para, template, wordcount):
    acc = len(set(input_para.split())&set(template.split()))
    acc = acc/wordcount
    return acc

def user_feedback():
    print('Rate the Game between 1 and 5.')
    ratings=input()
    if ratings.isnumeric()==False:
        print('Invalid Statement, Please enter number between 1 and 5.')
        return user_feedback()
    ratings=int(ratings)
    if ratings<1 or ratings>5:
        print('Invalid Statement, Please enter number between 1 and 5.')
        return user_feedback()
    feedback_list.append(ratings)
    print("How would you rate the accuracy of our results? Rate between 1 and 5! ")
    ratings2=input()
    if ratings2.isnumeric()==False:
        print('Invalid Statement, Please enter number between 1 and 5.')
        return user_feedback()
    ratings2=int(ratings2)
    if ratings2<1 or ratings2>5:
        print('Invalid Statement, Please enter number between 1 and 5.')
        return user_feedback()
    feedback_list.append(ratings2)
    print("How would you rate our templates? Rate between 1 and 5! ")
    ratings3=input()
    if ratings3.isnumeric()==False:
        print('Invalid Statement, Please enter number between 1 and 5.')
        return user_feedback()
    ratings3=int(ratings3)
    if ratings3<1 or ratings3>5:
        print('Invalid Statement, Please enter number between 1 and 5.')
        return user_feedback()
    feedback_list.append(ratings3)
    print("Please tell us if you have any other suggestions/improvements for us!")
    suggestions=input()
    feedback_list.append(suggestions)
    print("Thanks for your valuable Feedback!")
    return

def information():
    print()
    print("Air Typing Speed Calculator has two modes for increasing your typing speed and improving your Muscle Memory! ")
    print("Practice Mode has around 4 difficulty levels and has 5 templates for each level. The template is randomly selected and user types it to improve their speed.")
    print("Competition Mode is similar. However in this upto 10 users can take the test one by one and the winner will be declared at the end!\nObviously number of users cannot be less than 2")
    print("Is there any further information you would like to know? Yes or No?")
    choice=input().lower().strip()
    if choice=='yes':
        print("Enter 'tips' for typing tips")
        print("Enter 'about' for information regarding the creation of this tool")
        print("Enter 'donate' to learn information about donation methods!")
        prompt=input().lower().strip()
        if prompt=="tips":
            print()
            print()
            print("4 Tips for Improving Your Typing Speed & Accuracy")  #Enter Tips Here!
            print("1.) Use the correct starting position!\nWhen practicing your typing skills, it’s important to use proper hand placement. To start, keep your fingers positioned over the home row keys (left hand over the A, S, D, and F keys),\nand (the right hand over the J, K, L, and ; keys), with your thumbs hovering over the space bar. \nFrom here, you can move your fingers slightly to reach neighboring keys. Your hands should always return this starting position.")
            print("2.) Don’t look down your hands!Instead of looking down at your hands, focus on your screen.\nThis can be difficult at first, especially if you have not yet mastered the exact placement of the keys.\nHowever, looking at the screen will help improve your accuracy because you will be able to catch your typos as they occur. You’ll also begin to memorize the placement of the keys,\nso you’ll be able to type more quickly as you practice.")
            print("3.) Maintain good posture!\nSitting in an upright position is going to make it easier to type faster. If you are used to slouching in your chair or working from the couch,\ntry moving to a straight-backed chair or working at your desk")
            print("4.) Practice! Nothing is mastered overnight, and in order to really improve your typing accuracy and speed, you need to practice every day.")
            print("Reference: https://www.herzing.edu/blog/5-tips-improving-your-typing-speed-accuracy")
            return
        elif prompt=="about":
            print("About Us: ")
            print("This tool was designed as part of CS101 Programming Fundamentals (PFUN) Semester 1 Final Project at Habib University by Group 3.\nThe Overall Structure, Plan, Functionality, main program, competition mode was designed by Abduullah Junejo followed by Quality assurance.\nRabia designed the fundamental concept of using the time module and designed the first version of the practice mode. She created the accuracy measuring and speed calculating part of this program!\nIqra being a freelancer designed the templates that are used in this program and designed the first version of feedback Tab and this information Tab.")  #About
            return
        elif prompt=="donate":
            print("You can visit our Patreon to support us! @Elites.AJ.Productions. Do not forget to visit our Instagram & Facebook as Well: @elites.aj.productions") #Enter Payment Details
            return
        else:
            return information()
    elif choice=="no":
        pass
    else:
        information()
    return
    

competition_results=[]
feedback_list=[]
main()


