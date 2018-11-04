#jumble word game
import random as r
import os
import time
from datetime import date as d
name=""
def tab():
    os.system("cls")
    for i in range(13):
        print()
    for j in range(4):
        print(end="\t")
def tabbe():
    for j in range(4):
        print(end="\t")
def tabb():
    for j in range(8):
        print(end="\t")
def intro():
    os.system("COLOR 1E");
    global name
    tab()
    print()
    tabbe()
    print(" JJJJJJJJJJJ    UUU     UUU    MMM      MMM    BBBBBBB      LLL           EEEEEEEEEEE")
    tabbe()
    print(" JJJJJJJJJJJ    UUU     UUU    MMMM    MMMM    BBBBBBBB     LLL           EEEEEEEEEEE")
    tabbe()
    print("     JJJ        UUU     UUU    MMMMM  MMMMM    BBB    BB    LLL           EEE")
    tabbe()
    print("     JJJ        UUU     UUU    MMM  MM  MMM    BBB    BB    LLL           EEE")
    tabbe()
    print("     JJJ        UUU     UUU    MMM      MMM    BBBBBBB      LLL           EEEEEEEEE")
    tabbe()
    print("     JJJ        UUU     UUU    MMM      MMM    BBBBBBBB     LLL           EEEEEEEEE")
    tabbe()
    print("     JJJ        UUU     UUU    MMM      MMM    BBB    BB    LLL           EEE")
    tabbe()
    print(" JJ  JJJ        UUU     UUU    MMM      MMM    BBB    BB    LLL           EEE")
    tabbe()
    print(" JJJ JJJ        UUUUUUUUUU     MMM      MMM    BBBBBBBB     LLLLLLLLLLL   EEEEEEEEEEE")
    tabbe()
    print(" JJJJJJJ         UUUUUUUU      MMM      MMM    BBBBBBB      LLLLLLLLLLL   EEEEEEEEEEE")
    tabbe()
    print("  JJJJJ")
    time.sleep(6)
    tab()
    print()
    tabb()
    name=input("Enter your name:")
def shuffle(s):
    l1=list(s)
    st=""
    r.shuffle(l1)
    for i in range(len(l1)):
        st+=l1[i]
    return st
def file(f,sec,hint):
    global score
    global name
    fp=open(f,"r")
    s=fp.read()
    fp.close()
    l=s.split(" ")
    fp=open(hint,"r")
    s=fp.read()
    fp.close()
    h=s.split("\n")
    play(l,sec,h)
    s=(f.split("."))[0]
    today=d.today()
    hs=open("score.txt","a+")
    hs.write(name+"        "+str(today)+"        "+s.upper()+"        "+str(score)+"\n")
    hs.close()
def menu():
    while True:
        tab()
        print()
        tabb()
        print("1.EASY")
        tabb()
        print("2.MEDIUM")
        tabb()
        print("3.HARD")
        tabb()
        print("4.HIGH SCORE")
        tabb()
        print("5.EXIT")
        tabb()
        try:
            choice=int(input("Enter choice:"))
        except ValueError:
            print("Please enter integer.")
            continue
        tab()
        print()
        tabb()
        if choice==1:
            file("easy.txt",10,"easy_hint.txt")
        elif choice==2:
            file("medium.txt",8,"medium_hint.txt")
        elif choice==3:
            file("hard.txt",10,"hard_hint.txt")
        elif choice==4:
            high()
        elif choice==5:
            print("GOODBYE")
            break
        else:
            print("Invalid choice")
            time.sleep(2)
def play(l,sec,hint):
    print("READY")
    time.sleep(2)
    tab()
    print()
    tabb()
    print("SET")
    time.sleep(2)
    tab()
    print()
    tabb()
    print("GO!!!")
    time.sleep(2)
    print("\a")
    global score   
    global name
    score=0
    k=int(0)
    for i in l:
        st=shuffle(i)
        while st==i:
            st=shuffle(i)
        else:
            tab()
            print()
            tabb()
            for j in st:
                print(j,end=" ")
        print()
        print()
        tabb()
        print("Your answer",end="")
        ans=input("(Press H to take hint):")
        if ans=='H':
            tabb()
            print(hint[k])
            tabb()
            ans=input("Your answer:")
        print()
        print()
        tabb()
        if ans==i:
            print("You are correct")
            score+=1
        else:
            print("You are wrong")
        time.sleep(2)
        k+=1
    else:
        tab()
        print("{} your score is:{}".format(name,score))
        time.sleep(5)
def high():
    hs=open("score.txt","r")
    print(hs.read())
    hs.close()
    time.sleep(5)
def jumble_main():
    intro()
    menu()
