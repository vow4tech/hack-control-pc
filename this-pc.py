import os
import subprocess

def display_this_pc_control_menu():
    print("PC OPERATIONS MENU")
    print("1. Shutdown Kali Computer Immediately")
    print("2. Shutdown Kali Computer after a given time")
    print("3. Restart Kali Computer Immediately")
    print("4. Restart Kali Computer after a given time")
    print("5. Lock Kali Computer")
    print("6. Exit")

def main():
    while True:
        display_this_pc_control_menu()
        choice = input("Enter desired choice :")
        
        if choice =='1':
            os.system("shutdown now")
        elif choice == '2':
            sec = input("Enter Number of Seconds to wait :")
            try:
                sec = int(sec)
                os.system(f"shutdown -h +{sec//60}")
            except ValueError:
                print("Invalid Input ! Please Enter Number of Seconds to wait")

        elif choice == '3':
            os.system('reboot')
        elif choice == '4':
            sec = input("Enter Number of Seconds to wait :")
            try:
                sec = int(sec)
                os.system(f"shutdown -r +{sec//60}")
            except ValueError:
                print("Invalid Input ! Please Enter Number")

        elif choice == '5':
            os.system("gnome-screensaver-command -l")
        elif choice == '6':
            print("Exiting my PC Control Program")
            break

        else:
            print("Wrong Choice friend ! PLease Select genuine or Valid Option")

if __name__ == "__main__":
    main()
        
    