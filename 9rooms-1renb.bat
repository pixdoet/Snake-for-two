@echo off
color 0a
title 9 Rooms-1 Ren B Edition (Alpha 0.0.1)

:title
echo Welcome to 9 Rooms!
echo Type Start to enter the game, Credits to view who made this
set "titleCmd= "
set /p "titleCmd=Command: "
if %titleCmd% == Start goto room1
if %titleCmd% == start goto room1
if %titleCmd% == Credits goto credits1
if %titleCmd% == credits goto credits1
goto title

:room1
echo.
echo You have entered Room 1. Type look to look around, directions for more directions, help for more commands
set "room1Cmd= "
set /p "room1Cmd=Command: "
if %room1Cmd% == look echo You see Liang Zen arguing with Ms Lim
if %room1Cmd% == help echo Type argueLZ to argue with Liang Zen. Type beat to beat Liang Zen. Type exit to exit
if %room1Cmd% == argueLZ echo You were sent to the discipline room by Ms Lim. Game Over! && pause && goto title
if %room1Cmd% == directions echo Right: Room 2, Down: Room 4
if %room1Cmd% == beat echo You've killed Liang Zen and was taken to the Police. Game Over! && pause && goto title
if %room1Cmd% == right goto room2
if %room1Cmd% == down goto room4
if %room1Cmd% == cls cls
goto room1

:credits1
echo.
echo 9 Rooms is a text adventure engine made by Jun Ian. This version of 9 Rooms is probably the first game to use it.
echo 9 Rooms engine deveploped by Jun Ian
echo This version of 9 Rooms is made by Jun Ian
echo.
echo Dedicated to all my friends and classmates in JM 1 Ren B, especially stupid Liang Zen.
set "creditsCmd= "
set /p "creditsCmd=Enter a command to continue, type help for help: "
if %creditsCmd% == exit game exit /B
if %creditsCmd% == title goto title
if %creditsCmd% == help goto cHelp
if %creditsCmd% == cls cls
goto credits1

:cHelp
echo Type title to go to the title screen. Type exit game to exit.
pause
goto credits1
pause>nul
