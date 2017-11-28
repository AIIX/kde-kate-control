## KDE-Kate-Control
This skill enables an user to control the Kate client on the Desktop.

## Description 
#### Installation of skill:
* Download or Clone Git (run: git clone https://github.com/AIIX/kde-kate-control inside /opt/mycroft/skills)
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "kde-kate-control". (Clone does not require this step)
* Copy the kde-kate-control folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora: 
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Ubuntu / KDE Neon: 
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

## Examples
###### New File
* "Hey Mycroft, create new file "

###### Close File
* "Hey Mycroft, close file "

###### Save File
* "Hey Mycroft, save documents "

###### Go to next tab
* "Hey Mycroft, goto next tab "

###### Go to previous tab
* "Hey Mycroft, goto previous tab "

###### Split view horizontally 
* "Hey Mycroft, split view horizontally "

###### Split view vertically 
* "Hey Mycroft, split view vertically "

###### Go to next view
* "Hey Mycroft, goto next view "

###### Go to previous view
* "Hey Mycroft, goto previous view "

###### Show kate config
* "Hey Mycroft, show config "

## Credits 
(AIX) Aditya Mehra
