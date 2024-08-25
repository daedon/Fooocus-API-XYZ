saveCurlFiles   = False         # False saves disk space 
saveDumpFiles   = False         # False saves disk space 
saveLogs        = False         # False saves disk space 
saveNameCFG     = 2             # 0:No parms in file name, 1:ParmValue, 2:ParmName+ParmValue
maxFileNameParm = 80            # Max len of a parm used in save_name
parmSeparator   = "_"           # save_name separator between parameter
parmNVSeparator = "_"           # save_name separator between parameter name & value
barCharacter    = '-'           # Output line between each curl call


jobsDirectory   = f"./jobs/"                # Included with scripts, has sample jobs
defaultParmsDir = f"./default_parameters"   # Included with scripts
defaultTempltDir= f"./default_templates"    # Included with scripts
currentJobDir   = f"jobs/{jobName}"         # Belongs for job "jobName"
parmsDirectory  = f"{currentJobDir}/parms"  # User editable fooocus parameters
dumpDirectory   = f"{currentJobDir}/dumps"  # Parameters used to create image
logsDirectory   = f"{currentJobDir}/logs"   # 
curlDirectory   = f"{currentJobDir}/curls"

# Initialize directories and parameters if New job
if not os.path.exists( parmsDirectory):
   for directory in [ currentJobDir, logsDirectory, curlDirectory, parmsDirectory, dumpDirectory]:
       os.makedirs( directory, exist_ok=True)
   [shutil.copy2(os.path.join(defaultParmsDir, f), parmsDirectory) for f in os.listdir(defaultParmsDir) if f.startswith('_')]   
   shutil.copy( f"{defaultTempltDir}/curl.template", currentJobDir)         # Copy template
   print( f"New Job \"{jobName}\" and associated directories have been created.")
   print( f"Default parameter files have been copied to \"{parmsDirectory}\".")
