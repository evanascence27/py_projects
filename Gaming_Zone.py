from jumble_word import *
from tic_tac_toe import*
def main():
    os.system("COLOR 2E")
    tab()
    print()
    tabb()
    tabb()
    print("       GGGGG")
    tabb()
    tabb()
    print("      GGGGGGG")
    tabb()
    tabb()
    print("     GGG   GGG")
    tabb()
    tabb()
    print("    GGG      GGG")
    tabb()
    tabb()
    print("   GGG")
    tabb()
    tabb()
    print("  GGG           ZZZZZZZZZZZZZZZZ")
    tabb()
    tabb()
    print("  GGG          ZZZZZZZZZZZZZZZZ")
    tabb()
    tabb()
    print("  GGG                      ZZZ")
    tabb()
    tabb()
    print("  GGG      GGGGGGG        ZZZ")
    tabb()
    tabb()
    print("  GGG      GGGGGGG       ZZZ")
    tabb()
    tabb()
    print("   GGG       GGG        ZZZ")
    tabb()
    tabb()
    print("    GGG      GGG       ZZZ")
    tabb()
    tabb()
    print("     GGG    GGG       ZZZ")
    tabb()
    tabb()
    print("      GGGGGGGG       ZZZZZZZZZZZZZZZZ")
    tabb()
    tabb()
    print("       GGGGGG       ZZZZZZZZZZZZZZZZ")
    time.sleep(6)
    while True:
        tab()
        print()
        tabb()
        print("1. JUMBLE WORDS\t2. TIC_TAC_TOE\t3. EXIT")
        try:
            tabb()
            choice=int(input("Enter choice:"))
            if choice==1:
                jumble_main()
            elif choice==2:
                tic_main()
            elif choice==3:
                sys.exit()
            else:
                tabb()
                print("Invalid choice.")
        except ValueError:
            tabb()
            print("Please enter an integer.")
main()