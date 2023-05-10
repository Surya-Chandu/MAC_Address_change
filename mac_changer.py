#!/use/bin/env python3

from tkinter import *
import random
import subprocess

root = Tk(className="Change MAC address of eth0")
root. geometry("600x150")

def get_12_digit_MAC(length):
    return ''.join(random.choices('0123456789ABCDEFabcdef', k=length))

def MAC_goodbad(mac):
    if (mac[1] == '0' or mac[1] == '2' or mac[1] == '4' or mac[1] == '6' or mac[1] == '8' or mac[1] == 'a' or mac[1] == 'A' or mac[1] == 'c' or mac[1] == 'C' or mac[1] == 'e' or mac[1] == 'E'):
        return ("good")
    else:
        return ("bad")

def change_mac(out):
    changed = "eth0 interface of kali linux is changed to this MAc address --" + out
    label1 = Label(root, text=changed)
    label1.pack()
    subprocess.call(["ifconfig", "eth0", "down"])
    subprocess.call(["ifconfig", "eth0", "hw", "ether", out])
    subprocess.call(["ifconfig", "eth0", "up"])
    subprocess.call(["ifconfig"])

def mac_main():
    mac = get_12_digit_MAC(12)
    fin = MAC_goodbad(mac)
    if (fin == "good"):
        #print("Even we can do sepreate now")
        index = [0, 2, 4, 6, 8, 10]
        parts = [mac[i:j] for i, j in zip(index, index[1:] + [None])]
        out= ':'.join(map(str, parts))
        change_mac(out)
    else:
        mac_main()

if __name__ == "__main__":
    #main()
    label = Label(root, text="Changing the MAC address of the eth0 to get Anonymous in this network")
    label.pack()
    button = Button(root, text="Mac_change", command=mac_main)
    button.pack()
    button_exit = Button(root, text="Exit", command=root.destroy, bg="RED")
    button_exit.place(x=400, y=80)
root.mainloop()

