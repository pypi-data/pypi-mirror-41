#!/usr/bin/env python
'''
This contains useful functions to help with disk target selection

Ensure installation of wmi and pywin32

########### VERSION HISTORY ###########

13/08/2018 - Andy Norrie    - First version, based on initial work from Pedro Leao
'''

import re
import sys
import os
import collections

#linux system do not require this import 
if "win" in sys.platform:
    import wmi
    import win32file
    import win32api

from subprocess import check_output

from device import quarchDevice
from connection_specific.connection_QPS import QpsInterface
from device_specific.quarchQPS import quarchQPS

def GetDiskTargetSelection ():
    # Get available physical disks
    diskList = getAvailableDisks ("OS")
    # Get available mapped drives
    driveList = getAvailableDrives ()
    # Combine into a single list
    deviceList = driveList + diskList
 
    # Print selection dialog
    print ("\n\n ########## STEP 2 = Select a target drive. ##########\n")
    print (' ------------------------------------------------------------------')
    print (' |  {:^5}  |  {:^10}  |  {:^35}  |'.format("INDEX", "VOLUME", "DESCRIPTION"))
    print (' ------------------------------------------------------------------')

    for i in deviceList:
            print (' |  {:^5}  |  {:^10}  |  {:^35}  |'.format(str(deviceList.index(i) + 1), str(i.items()[2][1]), str(i.items()[0][1])))
            print(' ------------------------------------------------------------------')

    # Get user to select the target
    try:
        drive_index = int(raw_input("\n>>> Enter the index of the target device: " )) - 1
    except NameError:
        drive_index = int(input("\n>>> Enter the index of the target device: ")) - 1

    # Verify the selection
    if (drive_index > -1):
        myDeviceID = deviceList[drive_index]
    else:
        myDeviceID = None

    return myDeviceID

'''
Gets a list of available host drives, excluding the one the host os running on if specified
'''
def getAvailableDisks (hostDrive):
    driveList = []

    diskNum = 0

    diskScan = wmi.WMI()

    # Loop through disks
    for disk in diskScan.Win32_diskdrive(["Caption", "DeviceID", "FirmwareRevision"]): 
        driveInfo = {
            "NAME": None,
            "DRIVE": None,
            "FW_REV": None,
            }
        
        DiskInfo= str(disk)
                
        # Try to get the disk caption
        DiskInfo.strip()
        a = re.search('Caption = "(.+?)";', DiskInfo)    
        if a:
            diskName = a.group(1)
           
        # Try to get the disk ID
        b = re.search('DRIVE(.+?)";', DiskInfo)
        if b:
            diskId = b.group(1) 
            
        # Try to get the disk FW
        c = re.search('FirmwareRevision = "(.+?)";', DiskInfo)
        if c:
            diskFw = c.group(1)           

        # Skip if this is our host drive!
        if (diskName != hostDrive):
            # Append drive info to array
            driveInfo.update(dict(zip(['NAME','DRIVE','FW_REV'], [diskName, diskId, diskFw])))
            #driveInfo = collections.OrderedDict(driveInfo)
            driveList.append(driveInfo)

    # Return the list of drives
    return driveList

'''
Gets a list of available drive letters, excluding the current drive
'''
def getAvailableDrives():

    #return string of logicaldisks' specified attributes
    RList = check_output( "wmic logicaldisk get caption, Description" )

    #decode if python version 3
    if sys.version_info.major==3:
        RList = str( RList, "utf-8" )

    #split into readable items
    RList_Lines = RList.split("\n")

    RList_MinusNetwork = []

    #appaend all drives to list that are not network drives
    for item in RList_Lines:
        if "Network Connection" not in item:
            if len(item) > 0:
                RList_MinusNetwork.append(item[0:item.find("  ")])

    #remove column headers
    del RList_MinusNetwork[0]

    #function call to remove every occurance of \r in list
    RList_MinusNetwork = remove_values_from_list(RList_MinusNetwork, "\r")

    RL_DrivesAndVolumeInfo = []

    #call function to return volume name of each drive (if available)
    for i in RList_MinusNetwork:
        i.replace(":", "://")
        try:
            RL_DrivesAndVolumeInfo.append(win32api.GetVolumeInformation(i)[0])
            RL_DrivesAndVolumeInfo.append(i)
            time.sleep(0.1)
        except:
            continue
        
    driveList = []

    try:
        for i in xrange(0, len(RL_DrivesAndVolumeInfo), 2):
            driveInfo = {
                "NAME": None,
                "DRIVE": None,
                "FW_REV": None,
                }
            driveInfo.update(dict(zip(['NAME','DRIVE','FW_REV'], [RL_DrivesAndVolumeInfo[i], RL_DrivesAndVolumeInfo[i+1], ""])))
            #driveInfo = collections.OrderedDict(driveInfo)
            driveList.append(driveInfo)
    except:
        for i in range(0, len(RL_DrivesAndVolumeInfo), 2):
            driveInfo = {
                "NAME": None,
                "DRIVE": None,
                "FW_REV": None,
                }
            driveInfo.update(dict(zip(['NAME','DRIVE','FW_REV'], [RL_DrivesAndVolumeInfo[i], RL_DrivesAndVolumeInfo[i+1], ""])))
            #driveInfo = collections.OrderedDict(driveInfo)
            driveList.append(driveInfo)
  
    return driveList

'''
Simple function to remove a given item from a list
'''
def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]