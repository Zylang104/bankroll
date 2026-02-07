import os
import sys
import webbrowser
import urllib.request # make sure you have all of those libraries

# ANSI Colors
PINK = '\033[95m'
RESET = '\033[0m'

LOGO = f"""{PINK}
  ____              _              _ _ 
 |  _ \            | |            | | |
 | |_) | __ _ _ __ | | ___ __ ___ | | |
 |  _ < / _` | '_ \| |/ / '__/ _ \| | |
 | |_) | (_| | | | |   <| | | (_) | | |
 |____/ \__,_|_| |_|_|\_\_|  \___/|_|_|
{RESET}"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_music():
    print(f"\n{PINK}[?] Enter the full path to your executor's workspace folder:{RESET}")
    folder_path = input(f"{PINK}> {RESET}").strip()
    
    # Remove quotes if user copied path as "C:\Path"
    folder_path = folder_path.strip('"')
        
    if not os.path.isdir(folder_path):
        print(f"{PINK}[!] The directory '{folder_path}' does not exist.{RESET}")
        input(f"{PINK}[Press Enter to continue]{RESET}")
        return

    file_url = "https://cdn.discordapp.com/attachments/1469803876315304136/1469803985648091207/BANKROLL.mp3?ex=6988fd21&is=6987aba1&hm=211f4849dda9f4ec18619ea1a43c1c598690e4357c78aa8da32e85434c0dcd3b&"
    destination = os.path.join(folder_path, "BANKROLL.mp3")

    print(f"{PINK}[*] Downloading BANKROLL.mp3...{RESET}")
    try:
        req = urllib.request.Request(file_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(destination, 'wb') as out_file:
            out_file.write(response.read())
        print(f"{PINK}[+] Successfully downloaded to: {destination}{RESET}")
    except Exception as e:
        print(f"{PINK}[!] Error downloading file: {e}{RESET}")
    
    input(f"{PINK}[Press Enter to return to menu]{RESET}")

def main():
    # Enable ANSI support on Windows just in case
    os.system('')
    
    try:
        while True:
            clear_screen()
            print(LOGO)
            print(f"{PINK}[1] Install necessary files{RESET}")
            print(f"{PINK}[2] Join Discord Server{RESET}")
            print(f"{PINK}[3] Exit{RESET}")
            
            choice = input(f"\n{PINK}Select option > {RESET}")
            
            if choice == '1':
                install_music()
            elif choice == '2':
                webbrowser.open("https://discord.gg/Pmnk9e6egS")
            elif choice == '3':
                sys.exit()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()