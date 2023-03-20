from time import sleep

# Back Injuries Class
class Back_injuries(object):
    contracture = 0
    principle_hernia = 0
    hernia = 0
    idiopathic = 0
    contusion = 0

    def __init__(self, name):
        self.name = name

    def set_contusion(self,cont):
        self.cont = cont 
        if cont == 0:
            self.contusion = 0
        else:
            self.contusion += 1

    # SHOW METHODS
    def show_contracture(self):
        return self.contracture

    def show_principle_hernia(self):
        return self.principle_hernia

    def show_hernia(self):
        return self.hernia

    def show_idiopathic(self):
        return self.idiopathic

    # COUNT METHODS
    def contra_sum(self, number):
        self.contracture += number
        return self.contracture

    def p_hernia_sum(self, number):
        self.principle_hernia += number
        return self.principle_hernia

    def hernia_sum(self, number):
        self.hernia += number
        return self.hernia

    def idiopathic_sum(self, number):
        self.idiopathic += number
        return self.idiopathic

    # COMPARE INJURIES
    def compare_injuries(self, injury1, injury2, injury3, injury4):
        self.injury1 = injury1
        self.injury2 = injury2
        self.injury3 = injury3
        self.injury4 = injury4
        injury_list = [injury1, injury2, injury3, injury4]
        injury_list.sort()
        if injury_list[3] == injury1:
            if self.contusion == 1:
                print("You may have a contracture and a contusion becouse of the fall or get hit.")
            else:
                print("You have a contracture.")
        elif injury_list[3] == injury2:
            if self.contusion == 1:
                print("You may have a principle of hernia and a contusion becouse of the fall or get hit.")
            else:
                print("You have a principle of hernia.")
        elif injury_list[3] == injury3:
            if self.contusion == 1:
                print("You may have a hernia and a contusion becouse of the fall or get hit.")
            else:
                print("You have a hernia.")
        elif injury_list[3] == injury4:
            if self.contusion == 1:
                print("You may have idiopathic low back pain and a contusion becouse of the fall or get hit.")
            else:
                print("You have an idiopathic low back pain.")
        else:
            print("Two or more injuries are mathced.")


# DEFINITION OF INJURIES
comparisor = Back_injuries("Comparisor")
contusion = Back_injuries("Contusion")
contracture = Back_injuries("Contracture")
p_hernia = Back_injuries("Principle of hernia")
hernia = Back_injuries("Hernia")
idiopathic = Back_injuries("Idiopathic")

#METHOD GOR GREET
def greetings():
    print("Hi!")
    sleep(1)
    have_low_back_pain()

#METHOD FOR KNOW IF YOU SUFFER LOW BACK PAIN
def have_low_back_pain():    
    low_back_pain = input("Do you have low back pain? (Y) for yes/ (N) for no): ")
    low_back_pain = low_back_pain.upper()
    if low_back_pain == "N":
        print("Ok you are fine.")
        sleep(2)
        greetings()
        have_low_back_pain()
    elif low_back_pain == "Y":
        print("Ok lets have a look at your problem")
        sleep(1)
        fall_or_kicked()
    else:
        print("Incorrect value entered.")
        have_low_back_pain()

#METHOD TO KNOW IF YOU FALL, GET HIT OR THE PAIN APPEARED PROGRESSIVELY A LONG THE TIME
def fall_or_kicked():
    f_o_k = input("Did you fall or get hit in the lumbar region? (Y) for yes/ (N) for no): ")
    f_o_k = f_o_k.upper()
    if f_o_k == "N":
        contusion.set_contusion(0)
        print("If you didnt fall or get hit probably the pain has a beggining in a bad movement maybe carrying heavy stuff or just for a pesime stand sustained for a long time.")
        sleep(1)
        print("Lets check the affected areas.")
        sleep(1)
        affected_areas()
    elif f_o_k == "Y":
        contusion.set_contusion(1)
        print("It is quite probable that the pain that you are suffering is a consequence of the fall or get hit, but let see which could be the affected areas.")
        sleep(1)
        affected_areas()
    else:
        print("Incorrect value entered. Try again")
        fall_or_kicked()

#METHOD TO KNOW THE PAIN REGION
def affected_areas():
    print("Stand in your normal and relaxed posture.")
    sleep(2)
    aff_area = input("Where do you feel the pain? (B) if the pain is just in the back lumbar region/ (L) if the pain goes down one leg and groin/ (LL) if the pain goes down two legs and groin/ (A) if the pain goes to the abdomen: ")
    aff_area = aff_area.upper()
    if aff_area == "B":
        contracture.contra_sum(1)
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(1)
        idiopathic.idiopathic_sum(1)
        sleep(1)
        sitting_pain()
    elif aff_area == "L":
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(1)
        sleep(1)
        sitting_pain()
    elif aff_area == "LL":
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(1)
        sleep(1)
        sitting_pain()
    elif aff_area == "A":
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(1)
        sleep(1)
        sitting_pain()
    else:
        print("Incorrect value entered. Try again.")
        affected_areas()
    
#METHOD TO KNOW PAIN WHEN SITTING
def sitting_pain():
    print("Sit down on a chair or sofa.")
    sleep(1)
    pain_when_sit = input("Does your pain goes down to the leg or legs when you are sitting? (Y) for yes/ (N) for no: ")
    pain_when_sit = pain_when_sit.upper()
    if pain_when_sit == "Y":
        hernia.hernia_sum(1)
        sleep(1)
        flexing_pain()
    elif pain_when_sit == "N":
        contracture.contra_sum(1)
        idiopathic.idiopathic_sum(1)
        sleep(1)
        flexing_pain()
    else:
        print("Incorrect value entered. Try again.")
        sitting_pain()

#METHOD TO KNOW PAIN WHEN FLEXING
def flexing_pain():
    print("Stand up on your normal and relaxed restposition and slowly get down like if you would want to touch your toes with your hands.")
    sleep(1)
    pain_flexing = input("Does you pain go down to the leg or legs when you flexionate your back? (Y) for yes/ (N) for no: ")
    pain_flexing = pain_flexing.upper()
    if pain_flexing == "Y":
        contracture.contra_sum(1)
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(2)
        sleep(1)
        stiffness()
    elif pain_flexing == "N":
        idiopathic.idiopathic_sum(1)
        sleep(1)
        stiffness()
    else:
        print("Incorrect value entered. Try again.")
        flexing_pain()
        

#METHOD TO KNOW STIFFNESS
def stiffness():
    stiff = input("Do you feel stiffness when you move your low back at different directions? (Y) for yes/ (N) for no: ")
    stiff = stiff.upper()
    if stiff == "Y":
        contracture.contra_sum(1)
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(1)
        sleep(1)
        lack_strength()
    elif stiff == "N":
        idiopathic.idiopathic_sum(1)
        sleep(1)
        lack_strength()
    else:
        print("Incorrect value entered. Try again.")
        stiffness()

#METHOD TO KNOW LACK STRENGTH
def lack_strength():
    l_strength = input("Do you have lack of strength in one or both legs? (Y) for yes/ (N) for no: ")
    l_strength = l_strength.upper()
    if l_strength == "Y":
        p_hernia.p_hernia_sum(1)
        hernia.hernia_sum(1)
        sleep(1)
        leg_numbness()
    elif l_strength == "N":
        contracture.contra_sum(1)
        idiopathic.idiopathic_sum(1)
        sleep(1)
        leg_numbness()
    else:
        print("Incorrect value entered. Try again.")
        lack_strength()

#METHOD TO KNOW IF LEG NUMBNESS
def leg_numbness():
    l_numbness = input("Do you feel numbness in your legs? (Y) for yes/ (N) for no: ")
    l_numbness = l_numbness.upper()
    if l_numbness == "Y":
        hernia.hernia_sum(1)
        sleep(1)
        digestive_problems()
    elif l_numbness == "N":
        contracture.contra_sum(1)
        idiopathic.idiopathic_sum(1)
        sleep(1)
        digestive_problems()
    else:
        print("Incorrect value entered. Try again.")
        leg_numbness()

#METHOD TO KNOW IF DIGESTIVE PROBLEMS ARE PRESENT
def digestive_problems():
    d_problmes = input("Do you have digestive problems since you have the back issue? (Y) for yes/ (N) for no: ")
    d_problmes = d_problmes.upper()
    if d_problmes == "Y":
        hernia.hernia_sum(4)
        comparisor.compare_injuries(contracture.show_contracture(), p_hernia.show_principle_hernia(), hernia.show_hernia(), idiopathic.show_idiopathic())

    elif d_problmes == "N":
        contracture.contra_sum(1)
        p_hernia.p_hernia_sum(1)
        idiopathic.idiopathic_sum(1)
        comparisor.compare_injuries(contracture.show_contracture(), p_hernia.show_principle_hernia(), hernia.show_hernia(), idiopathic.show_idiopathic())
    else:
        print("Incorrect value entered. Try again.")
        digestive_problems()


greetings()

#git2