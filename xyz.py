#08-25_0106 
import os
import re
import sys
import time 
import shutil
import itertools
from datetime import datetime
os.system('clear')
DEBUG= False

##########################################################################################
def S( n):                                          
    if int(n) == 1:
        return ""
    else:
        return("s")

##########################################################################################
def debug( debugString):
    if not DEBUG: return
    print( debugString)
    answer = input(f"\n Enter=Next X=Abort: ").strip().lower()
    if answer == "x":
       sys.exit( 1)

##########################################################################################
def readParmFile(parmFile):
    lines = []
    with open(parmsDirectory+"/"+parmFile, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line == ".":                            # Don't read parms after "."
                break
            if stripped_line and not stripped_line.startswith("#"):
                lines.append(stripped_line)                     #
    return lines

##########################################################################################
def timeInDHMS( secondsRemaining):
    minutesRemaining = secondsRemaining // 60
    hoursRemaining   = round( minutesRemaining / 60, 1)
    daysRemaining    = round( hoursRemaining / 24, 1)
    return( f"{daysRemaining} days"        if daysRemaining >=1 else
                     f"{hoursRemaining} hours"      if hoursRemaining >=1 else
                     f"{minutesRemaining} minute"   if minutesRemaining == 1 else
                     f"{minutesRemaining} minutes"  if minutesRemaining > 1 else
                     f"{secondsRemaining} seconds")

##########################################################################################
def generateImages( jobName):
    image_number=0                                              # Fooocus-API "image_number", # of images per curl call
    global parm_count, stats
    parm_count  = {}                                            # Number of values/lines in each parameter file
    name_include= {}                                            # Parameters to be included in file name
    parm_names  = []
    parm_values = []
    nParmFiles  = 0
    numberOfMultiParms= 0
    multiplications= ""
    for fileName in sorted( os.listdir(parmsDirectory)):      ### READ ALL PARAMETERS, files must start with "_XY"
        if fileName.startswith("_"):                            # 1st 3 characters Parameter files are only
            parmName= fileName[3:]                              # used for sorting and are discarded.
            if parmName.endswith("_"):                          # Parm name to be included in file name
               parmName= parmName[:-1]                          # used for sorting and are discarded.
               name_include[parmName]= True
            else:
               name_include[parmName]= False
            if parmName in parm_names:                          # Check for duplicate
               print(f"WARNING: Duplicate parameter \"{parmName}\" ignored")
               continue                                         # Discard duplicate parameter file
            nParmFiles+= 1
            next_parm_value= readParmFile( fileName)
            if parmName == "image_number":
               image_number= int(next_parm_value[0])    
            parm_names.append( parmName)
            parm_values.append( next_parm_value)
            parm_count[parmName]= len(next_parm_value)          # To keep track of parameters with more than 1 value
            if len(next_parm_value) > 1:
               name_include[parmName]= True          
               numberOfMultiParms+= 1
               multiplications+= str( len(next_parm_value)) + " * "         # ( For the A * B * C ... output)
    multiplications+= str( image_number) 
    permutations = list( itertools.product( *parm_values))    ### GENERATE PERMUTATIONS of all parameters in all files
    if permutations == [()]:
       totalCurlCalls= 0
    else:
       totalCurlCalls= len(permutations)
    totalImages= len(permutations) * image_number
    print( f"Job \"{jobName}\" has {nParmFiles} parameters:\n  {parm_names}")
    if numberOfMultiParms > 0:
       print(f"The following parameter{S(numberOfMultiParms)} {'have' if numberOfMultiParms > 1 else 'has'} more than one value:")
       for parmName in (parm_names):
           if int( parm_count[parmName]) > 1:
              print( f"  {parmName}[{parm_count[parmName]}] ")
    print(f"Fooocus \"image_number\" is set to {image_number} image{S(image_number)} per Curl call")
    print(f"{totalCurlCalls} Curl call{S(totalCurlCalls)} will be made.")
    print(f"{totalImages} image{S(totalImages)} will be generated ({multiplications})")
    if totalImages == 0:
       sys.exit( 1)
    ############################################################################################################
    answer = input(f"Generate the {totalImages} image{S(totalImages)} now ? (y/n) ").strip().lower()
    if answer != 'y' or totalImages == 0:
       sys.exit( 1)
    startTime = time.time()                                                 # Start timer
    currentCurlCall= 0
    for permutation in permutations:                                        # For each combination of parameters
        currentCurlCall+= 1
        parmDump= ""
        with open( currentJobDir+'/curl.template', 'r') as f:       
            template = f.read()                                             # Read bash curl template script
        fileNameParms= ""
        fNameDescription= "{jobName}{Curl#}"
        args= []
        for parmName, parmValue in zip(parm_names,permutation):             # Fill Curl Template
            parmDump+= f"{parmName} : {parmValue}\n"
            if parm_count[parmName] > 1 or name_include[parmName]:          # Include value of Multi-value parameters in image file name
               args+= parmValue
               pV= parmValue
               pV= parmValue.replace( ".safetensors", "").replace( " ", "").replace( "*", "x").replace( "_", "").replace( " ", "_")\
                     .replace( ",", "_").replace( "'", "").replace( "(", "").replace( ")", "").replace( ":", "")
               pV= re.sub( r'[\[\]<>:"/\\|?*]', '', pV) 

               '''
               translation_table = str.maketrans( "* ,", "x__")             # Replace characters
               parmValue = parmValue.translate(translation_table)    # 
               translation_table = str.maketrans( "", "", "\\_'():")          # Delete characters
               pV = parmValue.translate(translation_table)
               '''

               if saveNameCFG == 1:                                         # Include parameter value in file name
                    fileNameParms+= f"{parmSeparator}{pV[:maxFileNameParm]}"               
               elif saveNameCFG == 2:                                       # Include parameter name & value in file name
                    fileNameParms+= f"{parmSeparator}{parmName}{parmNVSeparator}{pV[:maxFileNameParm]}"    
               fNameDescription+= "{" + parmName + "}"
            template= template.replace( f"___{parmName}", str(parmValue))   # Substitute ___place-holder for actual parameter value
        lines = template.splitlines()                                       # Look for un-replaced parameters
        missing_parameters= [line for line in lines if "___" in line]
        if len( missing_parameters) > 0:
           for line in missing_parameters:
               print(f"Missing Parameter file {line}")
           sys.exit( 1)

        fNameDescription+= "{timeStamp HrMinSec}"
        fName= f"{jobName}_{currentCurlCall:04d}" + fileNameParms + f"{parmSeparator}" + f"{datetime.now().strftime( '%H%M%S')}"
        parmDump= f"{fName}\n" + parmDump
        template = template.replace( "_save_name_", fName)
        with open( 'runCURL', 'w') as f:                        # Save template
             f.write( template)
        os.chmod( 'runCURL', 0o755)                             # Make template executable
        print(f"{barCharacter * 100}")
        print(f"Curl {currentCurlCall} of {totalCurlCalls} ({image_number} image{S(image_number)} will be generated)")
        print(f"save_name: \"{fName}\"\n")
        ############################################################################################################

        status= os.system( f"./runCURL >{logsDirectory}/{fName}.curl.log >>{logsDirectory}/{fName}.curl.log")
        if saveCurlFiles:
           shutil.copy( 'runCURL', os.path.join( curlDirectory, fName))
        if saveDumpFiles:
           with open( f"{dumpDirectory}/{fName}.parms", 'w') as dFile:   
             dFile.write( parmDump)
        if status != 0:
           print(f"\nExit status: {status}")
           sys.exit( 1)
        secondsPerCurl   = (int(time.time() - startTime)) / currentCurlCall
        secondsPerImage  = secondsPerCurl / image_number
        imagesRemaining  = totalImages - (currentCurlCall * image_number)
        if imagesRemaining > 0:
           timeRemaining= timeInDHMS( int(imagesRemaining * secondsPerImage))
           print( f"{imagesRemaining} image{S(imagesRemaining)} remaining, ESTIMATED time remaining: {timeRemaining}")
        '''
        '''

    return currentCurlCall

##########################################################################################
if __name__ == "__main__":
  if len( sys.argv) != 2:
     print( "Usage: python xyz.py <JobName>")
     sys.exit( 1)
  jobName = sys.argv[1]
  with open( 'config.py') as f:
       code = f.read( )
       exec( code)
  generateImages( jobName)
  print( globals())

