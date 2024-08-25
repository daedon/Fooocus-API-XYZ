A Fooocus image generator front end for Fooocus-API

###Quick start
get it 
 '''
 git clone https://github.com/daedon/fapi
 '''
run it
 '''
 cd xyz
 python3 xyz.py <jobName>
 '''

The first time you use a jobName, 
* A directory with the job's name will be created in"jobs"
* Associated sub-directories will be created
* Default files will be copied to job

You can then go into "jobs/<jobName>/parms" and modify the parameter values
### Preamble
My first github project.
My first python project.
First ancestor of xyz was written in bash.



### Details
fapi 
* will get a name upgrade
* fapi requires Fooocus-API to be running
* Generates images 
* Linux only for now
* Reads all the files in a job sub-directory
* Each file represents a Fooocus-API parameter
* Files are stored in "jobs/<jobName>"
* The 1st characters of each file must be an "_"
* The 1st 3 characters of each file are used for documentation and/or sorting
* The 1st 3 characters of each file are discarded
* The files are read in alphabetical order, hence the first 3 characters
* An array variable is created for each parameter with the same name.
* The contents of each parameter file is read line by line into the elements of the cooresponing array variable
* Empty lines are ignored
* Lines beginning with a "#" are ignored (comments)
* A line beginning with a "." ends the reading of values for the current parameter
* fapi generates all permutations of the parameter values in the order they were read.
* For each permutation of all the values, fapi makes a curl call to fooocus-API.



============= reminder notes ==========================
example:
* Example contents of "___refiner_switch"
juggernautXL_v8Rundiffusion.safetensors
realisticStockPhoto_v20.safetensors
"XYZ" because this is simlar to 1111's "plotxyz"
(Getting to that 1st push was painful)
config.py
Adding your own parameters
