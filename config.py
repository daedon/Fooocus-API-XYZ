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
dirs = { 'job'  : f"jobs/{job}", 
         'parms': f"jobs/{job}/parms", 
         'logs' : f"jobs/{job}/logs", 
         'dump' : f"jobs/{job}/dump", 
         'curls': f"jobs/{job}/curls"}

# Initialize directories and parameters if New job
if not os.path.exists( dirs['parms']):
   for directory in [ dirs['job'], dirs['logs'], dirs['curls'], dirs['parms'], dirs['dump']]:
       os.makedirs( directory, exist_ok=True)
   [shutil.copy2(os.path.join(defaultParmsDir, f), dirs['parms']) for f in os.listdir(defaultParmsDir) if f.startswith('_')]   
   shutil.copy( f"{defaultTempltDir}/curl.template", dirs['job'])         # Copy template
   print( f"New Job \"{job}\" and associated directories have been created.")
   print( f"Default parameter files have been copied to \"{dirs[ 'parms']}\".")

#def print_vars():
#    for var_name in globals():
#        if not var_name.startswith('_'):
#            print(f'{var_name}: {globals()[var_name]}')


#  for key, value in dictionary.items():
#        print(f"{key}: {value}")


