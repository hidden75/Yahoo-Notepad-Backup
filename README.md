Simple script to backup Yahoo Notepad notes. 

This script is based off of the Firefox Plugin: https://github.com/sanx/radnotepad-firefox

I could no longer get the  Firefox plug-in to work, so I wrote this script to do the same task using Python.

Due to the script running from a terminal window, it was not possible to grab the WSSID from a Firefox session.

[testuser@NOTEBOOK Yahoo Notepad Backup]$ ./yahoo-notepad-backup.py  
What is your Yahoo username: testuser  
Password:  
Created directory: ./Yahoo-Notepad.testuser/Notebook  
Processing folder: Notebook  
Found (14) journal entries in folder  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/holy_grail.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/Five_Flags7_Flags.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/HOG.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/Addresses.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/App_Ideas.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/Clense.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/cobra.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/FoodsProducts.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/linux_backup.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/misc_products.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/Names.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/perfect_hard_bolied_eggs.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/Sign-Up_Complete!.txt  
Wrote file: ./Yahoo-Notepad.testuser/Notebook/Travel.txt  
Done processing folder: Notebook  
Created directory: ./Yahoo-Notepad.testuser/Test  
Processing folder: Test  
Found (1) journal entries in folder  
Wrote file: ./Yahoo-Notepad.testuser/Test/Test_note.txt  
Done processing folder: Test  
Created zipfile: Yahoo-Notepad-Backup.testuser.2017-10-01-08-45-28.zip  
Removed folder: ./Yahoo-Notepad.testuser  
