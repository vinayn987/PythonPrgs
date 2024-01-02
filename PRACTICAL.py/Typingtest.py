from time import *
import random as rd

def testing(text, type):
    mistake = 0
    for i in range(len(text)):
        try:
           if text[i] != type[i]:
               mistake += 1
        except:
             mistake += 1
    return mistake

def type_speed(start, end, type_in):
    time_taken = end - start 
    total_time = round(time_taken, 2)
    speed = len(type_in)/total_time
    return round(speed)
if __name__ == "__main__":
    while True:
        choice = input("ARE YOU READY TO DRILL (YES/NO): ").lower()
        match choice:
            case "yes":  
                    text = ["Python is high level, general purpose", 
                            "Interpreted language developed by Guido Van Rossum",
                            "Python is very simple to understand",
                            "Python is free and open-source"]
                    test = rd.choice(text)
                
                    print(test)
                    stime = time()
                    user_input = input("Start:==> ")
                    etime = time()

                    word = testing(test, user_input)
                    fast = type_speed(stime, etime, user_input)
                    print(f"Typing Speed: {fast} W/s")
                    print(f"Wrongs: {word}")
            case "no":
                print("Good bye! Come again tomorrow")
            
            case _:
                print("Invalid choice.")

