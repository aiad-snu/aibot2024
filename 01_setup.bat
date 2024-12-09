:: 주석
@echo off

call winget install -e --id Python.Python.3.10
::start /wait winget install -e --id Python.Python.3.10

call set PATH=%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Scripts\
::call setx PATH "%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\Scripts\"

call md c:\aibot2024\src\ 
call xcopy .\src\* c:\aibot2024\src\ /E /I
call xcopy .env c:\aibot2024\
call xcopy aibot2024.bat c:\aibot2024\
call xcopy aibot2024.bat %USERPROFILE%\Desktop\
call xcopy aibot2024.bat %USERPROFILE%\OneDrive\Desktop\

call cd /d C:\aibot2024\
pause
call python -m venv venv
call C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python310\python -m venv venv
call venv\Scripts\activate
call C:\aibot2024\venv\Scripts\activate.bat

call cd /d C:\aibot2024\src\
pause
call pip --version
call pip install -r requirements.txt

pause
python app.py

pause