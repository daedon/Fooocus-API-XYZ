### A Fooocus image generator front end for Fooocus-API
Reads Fooocus-API parameters and generates images for all permutations

Similar to Stable Diffusion Plot-XYZ

#### Quick start
Get it 
```
git clone https://github.com/daedon/Fooocus-API-XYZ
```
Run it
```
cd Fooocus-API-XYZ
python3 xyz.py <jobName>
```
The first time you use a jobName:
* A directory with the job's name will be created in "Fooocus-API-XYZ/jobs"
* Associated sub-directories will be created
* Default files will be copied to "jobs/myJobName"

You can then go into "jobs/myJobName/parms" and modify parameter values


#### 3 Parameter files included in sample myJob

Parm file: "../parms/_1_base_model"
```
juggernautXL_v8Rundiffusion.safetensors
realisticStockPhoto_v20.safetensors
```
Parm file: "../parms/_2_resolution"
```
1024*1536
1536*1024
```
Parm file: "../parms/_3_steps"
```
18
19
20
```
The above parameter files will result in 12 curl calls and 12 images ('image_number' is set to one in the example)

```
Job "myJob" has 13 parameters:
  ['base_model', 'resolution', 'steps', 'guidance_scale', 'image_number', 'negative_prompt', 'performance', 'prompt', 'refiner_model', 'refiner_switch', 'seed', 'sharpness', 'style']
The following parameters have more than one value:
  resolution[2] 
  steps[3] 
  refiner_model[2] 
Fooocus "image_number" is set to 1 image per Curl call
12 Curl calls will be made.
12 images will be generated (2 * 3 * 2 * 1)
Generate the 12 images now ? (y/n) y
"myJob_0001_resolution_1024x1024_steps_18_refiner_model_realisticStockPhotov20_023332"
"myJob_0002_resolution_1024x1024_steps_18_refiner_model_juggernautXLv8Rundiffusion_023332"
"myJob_0003_resolution_1024x1024_steps_19_refiner_model_realisticStockPhotov20_023332"
"myJob_0004_resolution_1024x1024_steps_19_refiner_model_juggernautXLv8Rundiffusion_023332"
"myJob_0005_resolution_1024x1024_steps_20_refiner_model_realisticStockPhotov20_023332"
"myJob_0006_resolution_1024x1024_steps_20_refiner_model_juggernautXLv8Rundiffusion_023332"
"myJob_0007_resolution_1280x1280_steps_18_refiner_model_realisticStockPhotov20_023332"
"myJob_0008_resolution_1280x1280_steps_18_refiner_model_juggernautXLv8Rundiffusion_023332"
"myJob_0009_resolution_1280x1280_steps_19_refiner_model_realisticStockPhotov20_023332"
"myJob_0010_resolution_1280x1280_steps_19_refiner_model_juggernautXLv8Rundiffusion_023332"
"myJob_0011_resolution_1280x1280_steps_20_refiner_model_realisticStockPhotov20_023332"
"myJob_0012_resolution_1280x1280_steps_20_refiner_model_juggernautXLv8Rundiffusion_023332"
```




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
