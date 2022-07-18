import subprocess

def inOutConsole():
    print("Idiomas disponibles: \n" + 
    "1. Español \n" +
    "2. English \n" + 
    "3. Exit")
    lang = int(input("\nSelecciona un idioma:"))

    return lang

def getNetworkKey(filter1, filter2):
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if filter1 in i]
    
    for i in profiles:
        
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if filter2 in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
            
lang = inOutConsole()

while lang != 3:
    
    if lang == 1:
        filter1 = "todos los usuarios"
        filter2 = "Contenido"
        getNetworkKey(filter1, filter2)
        break
    elif lang == 2: 
        filter1 = "All User Profile"
        filter2 = "Key Content" 
        getNetworkKey(filter1, filter2)
        break
    elif lang == 3:
        break
    else:
        print("\nPlease, select a valid option")
        lang = inOutConsole()


