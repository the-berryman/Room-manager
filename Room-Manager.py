import csv
import sys
import os
import subprocess
import vlc

FILENAME = "contacts.csv"

def display_title():
    print()
    print("==================")
    print(" Law Room Manager")
    print("==================")
    print()

def display_menu():
    print("COMMAND MENU")
    print("list - Display all rooms")
    print("view - View a room")
    print("add - Add a room")
    print("del - Delete a room")
    print("toolbox - Open Toolbox")
    print("stream - Open a network stream")
    print("exit - Exit program")
    print()

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
    contacts = []

def read_contacts():
    try:
        contacts = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
        return contacts
    except FileNotFoundError:
        print("----------------------------------------")
        print("ALERT: Could not find " + FILENAME + " file.")
        print("----------------------------------------")
        write_contacts(contacts)
        print("Starting new contacts file...")
        print("----------------------------------------")
        main()

def list_contacts(contacts):
    while True:
        if len(contacts) < 1:
            print()
            print("--------------------------------------------------------------")
            print("There are no contacts. Add some contacts to use this function.")
            print("--------------------------------------------------------------")
            print()
            return
        else:
            break
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0] )
        

def add_contact(contacts):
    room = input("Room: ")
    dmps = input("DMPS IP: ")
    pp = input("Projector/Processor: ")
    mediasite = input("Mediasite: ")
    touchpanelip = input("Touchpanel IP: ")
    airmediaip = input("AirMedia IP: ")
    additionalinfo = input("Additional Information: ")
    contact = []
    contact.append(room)
    contact.append(dmps)
    contact.append(pp)
    contact.append(mediasite)
    contact.append(touchpanelip)
    contact.append(airmediaip)
    contact.append(additionalinfo)
    contacts.append(contact)
    write_contacts(contacts)
    print()
    print(room + " was added.\n")
    print()
    main()

def delete_contact(contacts):
    while True:
        try:
            index = int(input("Number: "))
        except ValueError:
            print()
            print("---------------------------------")
            print("Invalid number. Please try again.")
            print("---------------------------------")
            main()
        if index < 1 or index > len(contacts):
            print()
            print()
            print("---------------------------------------------------------")
            print("There are no contacts with that number. Please try again.")
            print("---------------------------------------------------------")
            print()
            print("Restarting program...")
            print()
            main()
        else:
            break
    contact = contacts.pop(index - 1)
    write_contacts(contacts)
    print(contact[0] + " was deleted.\n")

def view_contact(contact):
    while True:
        try:
            i = int(input("Number: "))
        except ValueError:
            print("---------------------------------")
            print("Invalid number. Please try again.")
            print("---------------------------------")
            main()
        if i < 1 or i > len(contact):
            print()
            print()
            print("---------------------------------------------------------")
            print("There are no contacts with that number. Please try again.")
            print("---------------------------------------------------------")
            print()
            print("Restarting program...")
            print()
            main()
        else:
            break
    contact = contact[i-1]
    print()
    print("===========================================")
    print("============ Room Information =============")
    print("===========================================")
    print()
    print("Room name: " + contact[0])
    print()
    print("DMPS IP: " + contact[1])
    print()
    print("Projector/Processor: " + contact[2])
    print()
    print("Mediasite: " + contact[3])
    print()
    print("Touchpanel IP: " + contact[4])
    print()
    print("AirMedia IP: " + contact[5])
    print()
    print("Additional Information: " + contact[6])
    print()
    print("===========================================")
    print("===========================================")
    
    print()
    print()

def open_toolbox():
    subprocess.Popen(["C:\Program Files (x86)\Crestron\Toolbox\Toolbox.exe"])

def open_stream():
    import vlc
    stream_room = input("What room would you like to stream?: ")
    stream355cfront = vlc.MediaPlayer("rtsp://10.249.68.19")
    stream355cback = vlc.MediaPlayer("rtsp://10.249.68.27")
    stream355bfront = vlc.MediaPlayer("rtsp://10.249.68.22")
    stream355bback = vlc.MediaPlayer("rtsp://10.249.68.25")
    stream285cfront = vlc.MediaPlayer("rtsp://10.249.68.51")
    stream285cback = vlc.MediaPlayer("rtsp://10.249.68.57")
    stream382back = vlc.MediaPlayer("rtsp://10.249.68.217")

    
    if stream_room == "355c front":
        stream355cfront.play()
    elif stream_room == "355c back":
        stream355cback.play()
    elif stream_room == "355b front":
        stream355bfront.play()
    elif stream_room == "355b back":
        stream355bback.play()
    elif stream_room == "285c front":
        stream285cfront.play()
    elif stream_room == "285c back":
        stream285cback.play()
    elif stream_room == "382 back":
        stream382back.play()
    elif stream_room == "custom":
        streaminput = input("What's the IP of the stream you'd like to open?: ")
        customstream = vlc.MediaPlayer("rtsp://" + streaminput)
        customstream.play()
    else:
        print("Room not found")
   
   
    



def main():
    contacts = read_contacts()
    display_title()
    display_menu()
    list_contacts(contacts)
    
    print()
    
    while True:
          command = input("Command: ")
          if command.lower() == "list":
              list_contacts(contacts)
          elif command.lower() == "view":
              view_contact(contacts)
          elif command.lower() == "add":
              add_contact(contacts)
          elif command.lower() == "toolbox":
              open_toolbox()
          elif command.lower() == "stream":
              open_stream()
          elif command.lower() == "del":
              delete_contact(contacts)
          elif command.lower() == "exit":
              break
          else:
              print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()

          

        
        
