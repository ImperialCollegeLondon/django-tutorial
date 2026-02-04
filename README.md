## Django Tutorial

The commands below are used during the session and are included here for convenience
of allowing you to copy/paste

### 1 - Log into the server compnode1.bc.ic.ac.uk

       Note: The Django server can be run an any computer, icluding your desktops.
       However, we are using compnode1 today as specific ports [15001-15025]
       have been enabled (by the computer administrator) on this machine. If you
       wish to run Django an another machine then the administrator would allocate 
       and enable a specific port(s) for you.

### 2 - On compnode1 (download tutorial files and start the server)
```
module load python/3.11.5
```
```
git clone https://github.com/ImperialCollegeLondon/django-tutorial.git
# 'git clone' will create a directory called django-tutorial
```
```
cd django-tutorial/tutorial_project
```
```
python manage.py migrate
```
```
python manage.py runserver 0:PORT_NUMBER
# Where PORT_NUMBER = 15001 - 15025 (each student to be allocated a
# different port number)
# Note: to stop the server running in the Terminal, type CTRL-C  

```


### 3 - In a browser on your local machine (e.g., PC in 310 SECB) type

    http://compnode1.bc.ic.ac.uk:PORT_NUMBER/proteins
