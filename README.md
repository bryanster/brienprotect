# brienprotect

![image](https://raw.githubusercontent.com/bryanster/brienprotect/master/icon.ico)

this is a simple implementation of the clamav virus scanner using python

you can use the brienprotect-installer.exe to install it

⚠️ brienprotect gives no garantees

## requirements

``pip install -r requirements.txt``

## build

first build the python file to an exe

  `auto-py-to-exe`

using the main-to-exe.json config file

systray is compiled using the systray-to-exe.json config file

download clamav zip for windows x64 and extract to scanengine


then create the installer using inno setup compiler

inoo.iss

## in progress
the shield is currently in progress 
it should provide a service that automaticly scan new and changed files for viruses
