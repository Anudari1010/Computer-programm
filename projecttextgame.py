########
#import modules
#######
#Game Title: "Explore the keys"
#Game Summary:
#   You wake up after a strange place.
# You find yourself on a creepy room.
#You'll begin the adventure properly and need to collect as much ttreasure as you can.
# Main character supports saving and restoring, and you can even change how much information the game gives you about new locations brief commands.
########
#define functions
#######
def start():
    print("Explore the keys")
    print("You've just wake up in strange house")
    print("You find yourself on a creepy room")
    print("There were no windows, so the room had a dim light and old furniture, including a kitchen, basement, and bathroom, living room.")
    print("you must escape the house before the kidnappers come to you")
    
    move = input("\nWhat to do first? Say one of these choices:\n\topen_the_door\n\tlook_at_the_envelope\n\tto_cry_out_loud\n")
    if move.lower() == "open_the_door":
        open_the_door()

    elif move.lower() == "look_at_the_envelope":
        look_at_the_envelope()
    
    elif move.lower() == "to_cry_out_loud":
        to_cry_out_loud()
    

    else:
        print("\nsorry, I don't understand your input. I'll presume you want to remain here." )
        time.sleep(1)
        open_the_door()

def open_the_door():
    print('''⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠀⠀⠀⠀⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⢀⣴⣶⣶⣦⡀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠈⠻⠿⠿⠟⠁⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')

 
    print("\nYou were open the door you should need a door key.")
    input("\nPress enter to go back")
    start()

    

def to_cry_out_loud():
    print('''⢻⢭⡓⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠸⣏⢖⡲⣅⠀⠀
⣣⢾⡛⣜⢫⣦⠀⠀⢀⣤⠴⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣸⢏⡝⣆⢀
⢿⣧⢹⣬⡷⣚⣒⣶⡾⣍⡞⡱⣞⡇⠀⠀⠀⠀⢀⣠⢤⠖⣦⡤⠤⡶⠦⠤⣤⢶⠲⠤⣄⠀⠀⠀⠀⠀⢀⡤⠶⢶⢤⡀⢸⣛⣮⢞⡜⡚
⠈⡷⣻⢏⠶⣙⢶⣼⠟⡼⣜⡵⠋⠀⠀⠀⣠⠞⡩⢴⣿⣿⣾⣹⠐⢢⢁⡾⡵⠚⢻⣷⣤⡙⠲⢄⠀⠀⢾⣍⡻⣌⢧⣷⡾⡞⣥⢫⡝⣃
⠀⢻⣿⢊⣟⣾⢫⢇⡻⣱⢺⠁⠀⠀⠀⡼⣡⣿⣄⣀⡿⣿⣿⡏⡇⢢⢸⡿⣷⣤⣼⠿⢿⣿⣷⣎⣷⠀⠈⠳⣵⡩⢖⡻⣱⢻⣌⡳⢎⡵
⠀⠀⢻⡧⢞⡧⣋⣮⣕⡣⢿⠀⠀⢀⡼⢃⣻⢿⣿⣿⣧⠾⠟⡙⣧⣂⣌⢣⡛⡿⠿⠷⠾⠿⠿⠣⣌⠳⡀⢰⢯⡱⣫⡶⢥⣛⢮⡓⣏⢶
⠀⠀⠈⢯⡧⣓⢧⡚⣽⣞⡾⠀⢀⡞⠠⣿⠀⡰⢂⣖⣤⣯⣾⣿⣿⣿⣿⣿⣿⣇⠄⣎⣱⣉⢎⡱⣘⡇⠹⡞⣮⢵⢯⣱⠳⡬⢧⡙⣦⠋
⠀⠀⠀⠈⠳⣭⢲⡹⢲⡞⠁⠀⣼⢐⠡⡙⠳⠗⡛⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡁⡉⠛⣶⣵⠋⡐⢿⠈⠻⣆⢧⡛⢜⣣⠟⠁⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⢰⡇⢊⠔⡡⢊⠔⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠡⣿⢹⡄⢡⢚⣇⠀⠈⠉⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢊⠤⢑⠢⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢹⠃⢢⢻⡄⢊⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠌⢢⠁⢎⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⢿⣿⣿⣿⣿⣿⣿⣏⡄⢣⢺⡇⢼⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡊⠤⠉⢼⣿⣿⣿⣿⠿⠋⡄⠒⡌⢢⠐⡌⠻⣿⣿⣿⣿⣯⠛⢓⠛⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡘⡏⣿⣿⣿⡿⠋⡄⠣⠌⡱⢈⠄⢣⠐⡡⠘⢿⣿⣿⣿⡐⣌⢒⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡅⠸⠿⢛⡡⠘⡄⠣⡘⠄⠣⡘⠄⢣⠐⣉⠂⠻⢿⠿⠁⢼⡲⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣁⠦⠟⡁⢣⠐⡡⠂⡍⠰⢁⠎⡄⠣⢄⡉⠲⢦⣂⣉⢴⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢲⢥⣂⠅⣂⠑⡈⢅⠊⡐⠌⢡⢂⣌⣡⠶⣛⣙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

    print("\nWhen you scream, the abductors will approach you.")
    input("\nPress enter to go back.")
    start()
    

def look_at_the_envelope():
   
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⠆⠀⠀
⠀⠀⠀⣼⣿⣿⡿⠟⠛⠉⣉⣀⠘⣿⣿⣿⡿⠿⠿⠟⠛⠛⠉⣉⣀⣤⣤⣶⠂⠀
⠀⠀⣼⠟⠉⣀⣤⣶⣿⣿⣿⣿⣦⣤⣤⣤⡀⢠⣶⣶⣾⣿⣿⣿⣿⣿⣿⠃⠀⠀
⠀⠀⢠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⢿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠸⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⠿⣿⣿⡇⢻⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    print("The keys near you are stated in the letter when you look it up. ")
    

    move = input("\nWhat to do first? Say one of these choices:\n\tlook_under_the_bed\n")
    
    if move.lower() == "look_under_the_bed":
        look_under_the_bed()

   
    
       

def look_under_the_bed():
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀
⠀⠀⠀⣦⠀⠀⠀⠀⢀⣴⣿⡟⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠱⠉
⠀⠀⠀⡇⠓⠦⡀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⡀⠀⠀⠘
⠀⠀⠀⠀⢇⠀⠉⣹⣿⡏⠀⠀⠀⠀⠀⢸⡿⠛⢻⠿⠿⠿⢿⣿⣿⣿⣅⠀⠀⠁⠺
⠀⠀⠀⠀⠀⠈⠦⣿⣿⠁⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⣠⠀⠈⠙⢿⣷⡦⠤⠴
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⠀⠀⠀⡚⣧⡄⠀⠀⠀⣿⡇⠀⠀⠀⠀⣿⣷⠀⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠀⠀⠀⠷⢻⣷⣦⣤⣭⣯⣶⣶⣶⣶⣿⣿⣿⠀⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢑⠒⠫⢙⢉⣿⣿⡿⠃⠀⠀
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⢸⣦⢤⣤⠠⣄⡀⠀⠀⠀⣀⠀⠀⢸⣿⣧⠀⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⣷⠳⠎⢷⣇⡭⣿⣿⠛⡝⠉⠓⣼⣿⣿⠀⢠⡆
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠉⠛⠿⣵⢯⣿⡿⠏⠉⠛⠧⣤⣸⣿⣿⠀⢀⡟
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠷⠯⠽
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    print("\n Yayy!!! you found the key, now you can escape the strange house")
    print("\nCongrulations")
    exit()

########
#main
#######
#TODO: Add some global variables

start()