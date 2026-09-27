
import time
sessions  = []
def study_session():
    subject = input("enter subject ->")
    print("Start studying !")
    start = time.time()
    input('press enter to stop ->')
    end = time.time()
    duration = end - start
    sessions.append([subject,duration])
    print("session commpleted !")
    print("time:",int(duration//60),"minutes",int(duration % 60),"seconds")

def productivity():
    total = 0
    for session in sessions:
        total = total + session[1]
    print("\nTotal session ->",len(sessions))      
    print("total study time ->",int(total//60),"minutes",int(total % 60),"seconds")

def report():      
    print('\n___STUDY REPORT___')
    for session in sessions:
        print("subject ->",session[0])
        print("time ->",int(session[1]//60),"minutes",int(session[1] % 60),"seconds")

while True:
    print("\n____STUDY TRACKER____")
    print("1.start studying")
    print("2.productivity")
    print("3.Report")
    print("4.Exit") 
    choice = input("enter your choice ->")
    if choice == "1":
        study_session()
    elif choice == "2":
        productivity()
    elif choice == "3":
        report()
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("invalid choice")