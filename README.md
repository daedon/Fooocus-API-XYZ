### A Fooocus image generator front end for Fooocus-API
Reads Fooocus-API parameters and generates images for all permutations

Similar to Stable Diffusion Plot-XYZ

#### Quick start
get it 
```
git clone https://github.com/daedon/Fooocus-API-XYZ
```
run it
```
cd Fooocus-API-XYZ
python3 xyz.py <jobName>
```
The first time you use a jobName, 
* A directory with the job's name will be created in "Fooocus-API-XYZ/jobs"
* Associated sub-directories will be created
* Default files will be copied to "jobs/myJobName"

You can then go into "jobs/myJobName/parms" and modify parameter values
#### Preamble
* My first github project.
* My first python project.
* Linux only at this time
* First ancestor of xyz started out as 6 lines of bash. Grew grew grew.

#### Details
* Generates images using Fooocus-API
* Requires Fooocus-API to be running
* Reads parameter files in a job's "parms" subdirectory
* Each file represents a Fooocus parameter: eg, ___steps, ___resolution, ___prompt, ___base_model
* Files are stored in "jobs/myJobName"
* The 1st character of each file must be an "_"
* The 1st 3 characters of each file are used for documentation and/or sorting purposes
* The 1st 3 characters of each file are discarded
* The files are read in alphabetical order, hence the first 3 characters decide the order of the permutations
* An array variable is created for each parameter with the same name.
* The contents of each parameter file is read line by line into the elements of the cooresponing array/list
* Empty lines are ignored
* Lines beginning with a "#" are comments and ignored
* No parameter values are read after a line with a "."
* Fooocus-API-XYZ generates all permutations of the parameter values in the order they were read.
* For each permutation of all the values, Fooocus-API-XYZ makes a curl call to fooocus-API.



============= reminder notes ==========================
example:
* Example contents of "___refiner_switch"
juggernautXL_v8Rundiffusion.safetensors
realisticStockPhoto_v20.safetensors
"XYZ" because this is simlar to 1111's "plotxyz"
(Getting to that 1st push was painful)
config.py
Adding your own parameters
