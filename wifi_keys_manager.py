import os
import sys
import re
 
hi =  os.system('netsh wlan show profile | findstr "todos los usuarios"')

# Iterate over output to get each wifi SSID

# Save SSID in a list

# Ask to the user for SSID selection

# If exist, check for WiFi password > netsh wlan show profile name=Calculadora key=clear | findstr "clave"

