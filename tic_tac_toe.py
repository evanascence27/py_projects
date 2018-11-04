#tic tac toe
import sys
import os
import time
import numpy as n
import random as r
p="";p1="";p2=""
c=1#counts number of chances
#err#error in passing empty shell
b=n.array([[" "," "," "],[" "," "," "],[" "," "," "]])#maintains row and column content
def tab():
    os.system("cls")
    for i in range(13):
        print()
    for j in range(4):
        print(end="\t")
def tabb():
    for j in range(4):
        print(end="\t")
def tic_main():
    intro()
def intro():
    os.system("COLOR 4E")
    global p1;global p2;global p
    #delay
    os.system("cls")
    for i in range(17):
        print()
    for j in range(8):
        print(end="\t")
    print("LOADING...")
    time.sleep(7)
    #logo
    tab()
    print(" __________   __    ______	  __________     _         ______	 __________    ________    ________")
    tabb()
    print("|!!!!!!!!!!| |!!|  /!!!!!!|	 |!!!!!!!!!!|   /!\\       /!!!!!!|	|!!!!!!!!!!|  ////!!\\\\\\\\  |!!!!!!!!|")
    tabb()	
    print("    |!!|     |!!|  |!!|		     |!!|      //!\\\\      |!!|		    |!!|      |!!/  \\!!|  |!!|")
    tabb()
    print("    |!!|     |!!|  |!!|	   ___       |!!|     ///_\\\\\\     |!!|   ___        |!!|      |!!|  |!!|  |!!|___")
    tabb()	
    print("    |!!|     |!!|  |!!|	  |xxx|      |!!|    ////!\\\\\\\\    |!!|	|xxx|	    |!!|      |!!|  |!!|  |!!!!!!|")
    tabb()
    print("    |!!|     |!!|  |!!|              |!!|   ////   \\\\\\\   |!!|  	    |!!|      |!!|  |!!|  |!!|")
    tabb()
    print("    |!!|     |!!|  |!!|___           |!!|  ////     \\\\\\\\  |!!|___	    |!!|      |!!\\__/!!|  |!!|_____")
    tabb()
    print("    |!!|     |!!|  \\!!!!!!|          |!!| ////       \\\\\\\\ \\!!!!!!|	    |!!|      \\\\\\\\\\!!///  |!!!!!!!!|")
    time.sleep(6)
    #player mode
    tab()
    print("1. SINGLE PLAYER")
    tabb()
    print("2. DUAL PLAYER")
    tabb()
    print("3. EXIT\n")
    tabb()
    choice=int(input("Enter choice:"))
    if choice==1:
        tab()
        p=input("Player Enter your name: ")
        #game on
        tab()
        print("READY...")
        time.sleep(2)
        tab()
        print("SET...")
        time.sleep(2)
        tab()
        print("GO!!!")
        time.sleep(2)
        print("\a")
        single()
    elif choice==2:
        tab()
        p1=input("Player 1 enter your name: ")
        tab()
        p2=input("Player 2 enter your name: ")
        #game on
        tab()
        print("READY...")
        time.sleep(2)
        tab()
        print("SET...")
        time.sleep(2)
        tab()
        print("GO!!!")
        time.sleep(2)
        print("\a")
        dual()
    else:
        sys.exit()
#board layout
def board():
    global b
    tab()
    print("  Current board layout:")
    tabb()
    print("     1         2         3")
    tabb()
    print(" _________ _________ _________")
    for i in range(3):
        tabb()
        print("|         |         |         |")
        tabb()
        for j in range(3):
            print("|   ",b[i][j],"   ",end="")
        print("|")
        tabb()
        print("|_________|_________|_________|")
#single player
def single():
    global p;global b
    while True:
        ch='\0'
        c=1
        board()
        while True:
	    #turn checking
            if c%2!=0:
                ch='X'                 
                err=0
                print()
                tabb()
                print("%s enter row and column number,respectively: "%(p))
                try:
                    tabb()
                    row=int(input("Enter row:"))
                    tabb()
                    col=int(input("Enter column:"))
                    tabb()
                    if row<1 or row>3 or col<1 or col>3:
                        raise IndexError
                    if b[row-1][col-1]==" ":
                        b[row-1][col-1]=ch
                        board()
                    else:
                        err+=1
                except IndexError:
                    print("Please enter correct row and column.")
                    err+=2
                if win(ch)==1:#checking for player win
                    print()
                    tabb()
                    print("Player %s wins!!!"%(p))
                    w=1
                    break
                elif err==1:
                    print("")			
                    tabb()
                    print("Shell already filled.")
                    time.sleep(1)
                elif c==9:
                    print()
                    tabb()
                    print("Its a draw. Play again.")
                    time.sleep(1)
                    break
            else:
                row=r.randrange(3)
                col=r.randrange(3)
                while b[row-1][col-1]!=" ":
                    row=r.randrange(3)
                    col=r.randrange(3)
                ch='O'
                b[row-1][col-1]=ch
                board()
                if win(ch)==1:#checking for machine win
                    print()
                    tabb()
                    print("Sorry. you lose:((")
                    w=1
                    break
            if err==0:
                c+=1
        if w==1:
            tab()
            print("GOODBYE")
            time.sleep(4)
            sys.exit()
            break
        
#dual player
def dual():
    w=0
    global p1;global p2;global b
    while True:
        ch='\0'
        c=1
        board()
        while True:
	    #turn checking
            if c%2==0:
                ch='O'
                p=p2
            else:
                ch='X'
                p=p1
            err=0
            print()
            tabb()
            print("Player %s enter row and column number,respectively: "%(p))
            tabb()
            row=int(input("Enter row:"))
            tabb()
            col=int(input("Enter column:"))
            if b[row-1][col-1]==" ":
                b[row-1][col-1]=ch
                board()
            else:
                err+=1
            if win(ch)==1:#checking for win
                print()
                tabb()
                print("Player %s wins!!!"%(p))
                w=1
                break
            elif err!=0:
                print("")			
                tabb()
                print("Shell already filled.")
                time.sleep(1)
            elif c==9:
                print()
                tabb()
                print("Its a draw. Play again.")
                time.sleep(1)
                break
            else:
                c+=1
        if w==1:
            tab()
            print("GOODBYE")
            time.sleep(3)
            break
#checks for winning
def win(ch):
    global b
    fd1=0;fd2=0;flag=0
    for i in range(3):
        fr=0;fc=0
        for j in range(3):
            if i==j and b[i][j]==ch:#checks for 3 in a leading diagonal
                fd1+=1
            if b[i][j]==ch:#checks for 3 in a row
                fr+=1
            if b[j][i]==ch:#checks for 3 in a column
                fc+=1
        if fr==3 or fc==3:
            return 1
    j=2;i=0
    while j>=0:#checks for 3 in the other diagonal
        if b[i][j]==ch:
            fd2+=1
        i+=1
        j-=1 
    if fd1==3 or fd2==3:
        return 1
    else:
        return 0
