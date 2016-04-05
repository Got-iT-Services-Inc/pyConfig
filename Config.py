#############################################################
# Title: Python Config File Class	                    #
# Description: Wrapper For Loading a config file and        #
#              returning the information in the appropriate #
#	       form.					    #
# Version:                                                  #
#   * Version 1.0 10/30/2015 RC                             #
#                                                           #
# Author: Richard Cintorino (c) Richard Cintorino 2015      #
#############################################################

#################################################################
# Help: Python Config File Class	                    	#
#    Var = PConfig("Path-To-Config","Display-Debug-True-False") #
#								#
#    Var.get(self,"Config-Key-Name") returns "Value"		#
#################################################################

import sys
from Debug import pyDebugger

class pyConfig:

    __cfgFileName = "/opt/avi/config.ini"
    
    def __init__(self, ConfigFile, bDebug = True):
        self.__cfgFileName = ConfigFile
        self.Debugger = pyDebugger(self,bDebug,False)
        
        try:
            self.Debugger.Log("Opening Configuration File '" + self.__cfgFileName + "'...",endd='')
            with open (self.__cfgFileName) as cfgFile:
                self.Debugger.Log("...Success!",PrintName=False)
                self.__Config = cfgFile.read().split("\n")

        except Exception as e:
            self.Debugger.Log("Failed!",PrintName=False)
            self.Debugger.Log("Error: " + str(e))

    def Get(self,sKey):
        try:
            self.Debugger.Log("Searching for Key '" + sKey + "'")
            _match = [s for s in self.__Config if sKey in s]
            _pairs = _match[0].split("=")
            _value = _pairs[1]
            self.Debugger.Log("Returning value '" + _value + "' for key '" + sKey + "'")
            if _value == "True":
                _value = True
            elif _value == "False":
                _value = False
            return _value
        except Exception as e:
            self.Debugger.Log("Error: " + str(e))
            return None

    def GetAll(self,sKey,sRemove=None):
        try:
            self.Debugger.Log("Searching for Keys that have  '" + sKey + "' in them...")
            dDict = {}
            for sKv in self.__Config:
                sKV = sKv.split("=")
                if sKey in sKV[0]:
                    self.Debugger.Log("Found key '" + sKV[0] + "' with value '" + sKV[1] + "'")
                    if sRemove != None:
                        sKV[0] = sKV[0].replace(sRemove,"")
                    if sKV[1] == "True":
                        sKV[1] = True
                    elif sKV[1] == "False":
                        sKV[1] = False
                    dDict[sKV[0]] = sKV[1]
                    
            return dDict
        except Exception as e:
            self.Debugger.Log("Error: " + str(e))
            return None
            
    def Set(self,sKey,sValue,Autowrite=True):
        self.Debugger.Log("Searching for key '" + sKey + "' to alter")
        _nConfig = []
        try:
            for sC in self.__Config:
                if sKey in sC:
                    _pairs = sC.split("=")
                    self.Debugger.Log("Updating Key '" + str(sKey) + "' with value '" + str(sValue) +
                        "', original was '" + str(_pairs[1]) + "'...",endd='')
                    _nConfig.append(sKey + "=" + sValue)
                else:
                    _nConfig.append(sC)
            self.__Config = _nConfig
            if Autowrite == True:
                return self.Write()
            else:
                return True
        except e as Exception:
            self.Debugger.Log("Error: " + str(e))
            return False
                   
 
    def Del(self,sKey,Autowrite=True):
        self.Debugger.Log("Searching for key '" + sKey + "' to Delete...")
        _nConfig = []
        try:
            for sC in self.__Config:
                if sKey in sC:
                    _pairs = sC.split("=")
                    self.Debugger.Log("Deleting Key '" + str(sKey) + "' with value '" + str(sValue) +
                        "'...")
                else:
                    _nConfig.append(sC)
            self.__Config = _nConfig
            asdf
            if Autowrite == True:
                return self.Write()
            else:
                return True
        except e as Exception:
            self.Debugger.Log("Error: " + str(e))
            return False



    def Write(self):
        
            try:
                with open("/etc/network/interfaces",'w') as Cfg:
                    #Get config as '\n' separated list
                    for sL in self.__Config:
                        Cfg.write(sL + "\n")
                Cfg.close()
                return True
            except e as Exception:
                self.Debugger.Log("Error: " + str(e))
                return False
                      

