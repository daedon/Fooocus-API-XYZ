#08-28_0455 
saveNameCFG     = 2             # 0:No parms in file name, 1:ParmValue, 2:ParmName+ParmValue
maxFileNameParm = 80            # Max len of a parm used in save_name
saveCurlFiles   = False         # False saves disk space 
saveDumpFiles   = False         # False saves disk space 
saveLogs        = False         # False saves disk space 
parmSeparator   = "_"           # save_name separator between parameter
parmNVSeparator = "_"           # save_name separator between parameter name & value
barCharacter    = '-'           # Output line between each curl call

# Only touch the lines above, not below

jobsDirectory   = f"./jobs/"                # Root job directory
defaultParmsDir = f"./default_parameters"   # Included with scripts
defaultTempltDir= f"./default_templates"    # Included with scripts
currentJobDir   = f"jobs/{job}"         
parmsDirectory  = f"{currentJobDir}/parms"  # User editable fooocus parameters
dumpDirectory   = f"{currentJobDir}/dumps"  # Parameters used to create image
logsDirectory   = f"{currentJobDir}/logs"   # 
curlDirectory   = f"{currentJobDir}/curls"

dirs = { currentJobDir: f"jobs/{job}", logsDirectory: f"{currentJobDir}/logs"}




# Initialize directories and parameters if New job
if not os.path.exists( parmsDirectory):
   for directory in [ currentJobDir, logsDirectory, curlDirectory, parmsDirectory, dumpDirectory]:
       os.makedirs( directory, exist_ok=True)
   [shutil.copy2(os.path.join(defaultParmsDir, f), parmsDirectory) for f in os.listdir(defaultParmsDir) if f.startswith('_')]   
   shutil.copy( f"{defaultTempltDir}/curl.template", currentJobDir)         # Copy template
   print( f"New Job \"{job}\" and associated directories have been created.")
   print( f"Default parameter files have been copied to \"{parmsDirectory}\".")

#def print_vars():
#    for var_name in globals():
#        if not var_name.startswith('_'):
#            print(f'{var_name}: {globals()[var_name]}')


