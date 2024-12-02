import os
user_choice=0;
print("Please choose one of the number\n")
print("1. Update OS\n" + "2. Set hostname\n" + "3. Set ip address\n")


user_choice=input("Please enter your choice")


match user_choice:
    case 1:             
        print("Updating system")
        os.system("sudo apt update && apt upgrade")
        print("\n")
        print("Update is complete, please reboot the system")
    case 2:
        print("Setting hostname: ")
        hostname = input("Please enter your hostname: ")
        os.system(f"hostnamectl set-hostname {hostname}")
        print("Please reboot the system")
    case 3:
        print("Setting ip address: ")
        ip_addr = input("please enter your ip address of this host: ")
        ip_mask = input("please enter the subnet mask: ")
        print("available interfaces below: ")
        os.system("ip -br a")
        ip_int = input("please choose interface: ")
        os.system(f"ip a add {ip_addr}/{ip_mask} dev {ip_int}")
        print("")