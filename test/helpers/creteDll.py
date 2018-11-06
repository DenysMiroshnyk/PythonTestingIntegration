#-*- coding:utf-8 -*-
import os
from helpers import callCommandHelper



def CreateDll(folderTargetName, fileTargetName,fileSO):
    
    templateCompill = "g++  {flags}  {fileSourse} -o {fileTarget}"
    templateLinc    = "g++  -shared {objectfile} -o {fileTarget}"


    if os.path.exists(folderTargetName) == False:
        os.makedirs(folderTargetName)
    

#---------------delete old version-----------------------------------
    if os.path.exists(fileTargetName):
        os.remove(fileTargetName)
        #print("remove : "+ fileTargetName)
    for fso in fileSO:
        if os.path.exists(fso["rezultName"]):
            os.remove(fso["rezultName"])
            #print("remove : "+ fso["rezultName"])
#---------------compil -----------------------------------------------
    
    for filePair in fileSO:
        fileSourseName  =  filePair["sourseName"]
        fileObjecteName = filePair["rezultName"]
        flagCompil = filePair["flagsCompil"]
        cmd = templateCompill.format(
            fileSourse = fileSourseName,
            flags      = flagCompil, 
            fileTarget = fileObjecteName)
        
        
        callCommandHelper.CallCommandHelper(cmd)
   
#---------------linck-----------------------------------------------
    fileObjectName = " "
    for filePair in fileSO:
        fileObjectName = fileObjectName + filePair["rezultName"]+" "
    
    
    cmd = templateLinc.format(
        objectfile = fileObjectName,
        fileTarget = fileTargetName)
    
    
    callCommandHelper.CallCommandHelper(cmd)    
#=====================================================================    
