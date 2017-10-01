#!/usr/bin/python
########################################
# Author: hidden75
#
# Last Modified on Sep 23, 2017
########################################
import requests
import os
import datetime as dt
import json
import zipfile
import sys
import shutil
import getpass

cur = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

headers = {'Content-Type':'application/json', 'Content-Language':'en-US'}


debug = 0 
verbose = 1

username = ""
password = ""
folder_indexes = []
folder_names = []

def remove_folder(path):
    if os.path.exists(path):
         shutil.rmtree(path)
         if verbose:
             print "Removed folder: %s" % (path)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def makedirectory(directory):
    if not os.path.exists(directory):
       if verbose:
           print "Created directory: %s" % directory
       os.makedirs(directory)


def asyncGet(url, username, password):
    if debug:
        print "in asyncGet. url: " +url+ ""
    r = requests.get(url, headers=headers, auth=(username, password))
    if (r.status_code != 200):
         print "unexpected HTTP status response. expected '200', and got '%d'" % r.status_code
         sys.exit(1)
    #print r.text
    #print r.json
    #print r.status_code
    #print r.headers
    return r

def GetNotepadFolderIndex(username,password):
    indexUrl = "https://calendar.yahoo.com/ws/v3/users/" + username + "/calendars/?format=json"
    r = asyncGet(indexUrl,username, password)
    data = r.json()
    numberofFolders =  data['folders']['count']
    for i in range(numberofFolders):
       folderIndex = data['folders']['folder'][i]['type']
       if folderIndex == 'JOURNAL':
           folder_indexes.append(data['folders']['folder'][i]['id'])
           folder_names.append(data['folders']['folder'][i]['name'])
    return folder_indexes,folder_names



def GetNotepadFolder(folderId, username, password):
    indexUrl = "https://calendar.yahoo.com/ws/v3/users/" + username + "/calendars/" + folderId + "/journals/?format=json"
    res = asyncGet(indexUrl, username, password)
    folderInfo = res.json()
    return folderInfo
    

def processNotepadFolderData(folderdata, foldernames, fullpath):
    numberofJournals = folderdata['journals']['count']
    print "Processing folder: %s" % (foldernames) 
    print "Found (%d) journal entries in folder" % (numberofJournals)
    for i in range(numberofJournals):
        filename = spacereplace(folderdata['journals']['journal'][i]['summary'])
        fullpath_filename = fullpath + "/" + filename + ".txt"
        for des in folderdata['journals']['journal'][i]:
            if 'description' not in des:
                continue
            write_file(fullpath_filename, folderdata['journals']['journal'][i]['description'])
    print "Done processing folder: %s" % (foldernames)
        

def spacereplace(string):
    return ''.join('_' if c == ' ' else c for c in string)

def write_file(path_file, data):
    with open(path_file, 'w') as outfile:
       outfile.write(data.encode('utf8'))
       outfile.close()
       if verbose:
           print "Wrote file: %s" % path_file


def main():

    username = raw_input("What is your Yahoo username: ")
    password = getpass.getpass()


    folderindex,foldernames = GetNotepadFolderIndex(username, password)

    
    for i in range(len(folderindex)):
        folderdata = GetNotepadFolder(folderindex[i], username, password)

        fullpath = "./Yahoo-Notepad." + username + "/" + foldernames[i]
        makedirectory(fullpath)

        processNotepadFolderData(folderdata, foldernames[i], fullpath)


    zpath = "./Yahoo-Notepad."+username+""
    zfile = "Yahoo-Notepad-Backup."+username+"."+cur+".zip"
    zipf = zipfile.ZipFile(zfile, 'w', zipfile.ZIP_DEFLATED)
    zipdir(zpath, zipf)
    zipf.close()
    if verbose:
        print "Created zipfile: %s" % (zfile)
    remove_folder(zpath)





if __name__ == "__main__":

   main()
