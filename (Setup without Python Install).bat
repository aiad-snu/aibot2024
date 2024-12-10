@echo off

echo .....
echo Starting the installation of the AI Invention Bot.
echo First, I will install the Python program. (v.3.10) It may take some time.
echo .....
pause

::call winget install -e --id Python.Python.3.10
::start /wait winget install -e --id Python.Python.3.10

call set PATH=%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Scripts\
::call setx PATH "%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Scripts\"

echo .....
echo The Python program installation is complete. (About 1/3 of the installation is complete.)
echo Starting the source code file copy. The project folder will be 'c:\aibot2024'.
echo .....
pause

call md c:\aibot2024\src\ 
call xcopy .\src\* c:\aibot2024\src\ /E /I
call xcopy .env c:\aibot2024\
call xcopy aibot2024.bat c:\aibot2024\
call xcopy aibot2024.bat %USERPROFILE%\Desktop\
call xcopy aibot2024.bat %USERPROFILE%\OneDrive\Desktop\

call cd /d C:\aibot2024\
echo .....
echo About 1/2 of the installation is complete.
echo We are creating a Python virtual environment. 
echo It is done to manage and protect package versions.
echo Sometimes the creation process may fail or get stuck in the middle. 
echo. This happens because the next command (activation) is executed before the creation is complete. 
echo To resolve this, simply run the installation file again
echo .....
pause 
call python -m venv venv
call C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python -m venv venv
call venv\Scripts\activate
call C:\aibot2024\venv\Scripts\activate.bat

call cd /d C:\aibot2024\src\
echo .....
echo About 2/3 of the installation is complete.
echo The Python packages and libraries will be installed soon.
echo .....
pause
call pip --version
call pip install -r requirements.txt

echo .....
echo ======= Installation is almost complete. =======
echo AI invention bot (server) will run automatically, and you can see 2 IPs. 
echo (1) http://127.0.0.1:5000 is an internal IP address. It can only be accessed from This PC without delay.
echo (2) The other IP address below is an external IP address that can be accessed from outside. 
echo .   The numbers may vary depending on how you are connected to the internet. 
echo .   If you are connected through a router, it will likely appear as something like 192.168.xxx.xxx or 172.xx.xxx.xxx.
echo If you are using a PC (Windows laptop or desktop), open an internet browser (Edge, Chrome) and go to the above address. 
echo .   (On Windows 11, you can simply 'Ctrl+Click' to open it directly.) 
echo For Android phones, open the internet browser (Samsung Browser) and go to the same address. 
echo .   The same method applies to Macs and iPhones. 
echo .   However, due to voice recognition, you must use an internet browser that allows microphone permissions.
echo .
echo Once you connect, the AI Invention Bot's face will appear. 
echo .   Tap the bot's nose. If you don��t have a touchscreen, press the "q" key on your keyboard (Key-up).
echo .
echo If the IP address has changed(including the first connection), a pop-up will appear asking for microphone permissions. 
echo .   Click "Allow." On smartphones, the pop-up might not be visible due to the small screen size, 
echo .   but rotating the screen a few times should make it appear.
echo .
echo Continue the conversation by triggering the actions (touching the nose or typing "q"). 
echo .   You can ask about idea generation methods, scientific knowledge, how to invent, how to file patents, etc.
echo .
echo Tip) Tapping the nose twice will improve recognition. 
echo .   If the screen scrolls while tapping, input may not be registered.
pause
echo .....
echo Summary)
echo .   http://127.0.0.1:5000 for only This PC (fast)
echo .   http://xxx.xxx.xxx.xxx:5000 for The Other Devices
echo .   #Triggering_by_touch_or_q #Allow_Mic
echo .....
pause

python app.py

pause
:: comments