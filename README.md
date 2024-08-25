### Fooocus-API-XYZ: Variable Parameter Fooocus Image generator
#### Generates Fooocus Images with unrestricted parameter variations.

Reads values from parameter files and generates images for every permutation.

(more details below, see simple example after Quick Start)

#### Quick Start

Requires Fooocus-API installed and running.

Get it 
```
git clone https://github.com/daedon/Fooocus-API-XYZ
```
Run it
```
cd Fooocus-API-XYZ
python3 xyz.py myJob    # Sample job included
 or 
python3 xyz.py newJobName

```
The first time you use a jobName:
* A directory with the job's name will be created in "Fooocus-API-XYZ/jobs".
* Associated sub-directories will be created.
* Default files will be copied to "jobs/newJobName".
* Add,Modify,Delete parameters in "jobs/myJob/parms".
* Set default parameters for all future jobs in `defaults` directories.

#### A simple example with 3 Parameter files (included in sample myJob)
xyz will generate all permutations of the following parameters and make curl calls to Fooocus-API.
The following parameters will generate 12 curl calls and 12 images ('image_number' = 1).
Parameter files are located in the `../Fooocus-API-XYZ/jobs/myJob/parms` directory.

`FILE: _1_base_model`
```
# 2 Base Models
juggernautXL_v8Rundiffusion.safetensors
realisticStockPhoto_v20.safetensors
```
`FILE: _2_resolution`
```
# 2 Resolutions
1024*1536
1536*1024
```
`FILE: _3_steps`
```
# 3 Steps
18
19
20
```

Note that the characters in the 1st 3 positions of the file names determine the order the images will be generated. 

The above parameter files will generate the following output. 
```
Job "myJob" has 13 parameters:
  ['base_model', 'resolution', 'steps', 'guidance_scale', 'image_number', 'negative_prompt', 'performance', 'prompt', 'refiner_model', 'refiner_switch', 'seed', 'sharpness', 'style']
The following parameters have more than one value:
  base_model[2]     # juggernautXL_v8Rundiffusion.safetensors, realisticStockPhoto_v20.safetensors
  resolution[2]     # 1024*1536, 1536*1024
  steps[3]          # 18, 19, 20
Fooocus "image_number" is set to 1 image per Curl call
12 Curl calls will be made.
12 images will be generated (2 * 2 * 3 * 1)
Generate the 12 images now ? (y/n) y
"myJob_0001__base_model_juggernautXLv8Rundiffusion__resolution_1024x1024__steps_18_024844"
"myJob_0002__base_model_juggernautXLv8Rundiffusion__resolution_1024x1024__steps_19_024844"
"myJob_0003__base_model_juggernautXLv8Rundiffusion__resolution_1024x1024__steps_20_024844"
"myJob_0004__base_model_juggernautXLv8Rundiffusion__resolution_1280x1280__steps_18_024844"
"myJob_0005__base_model_juggernautXLv8Rundiffusion__resolution_1280x1280__steps_19_024844"
"myJob_0006__base_model_juggernautXLv8Rundiffusion__resolution_1280x1280__steps_20_024844"
"myJob_0007__base_model_realisticStockPhotov20__resolution_1024x1024__steps_18_024844"
"myJob_0008__base_model_realisticStockPhotov20__resolution_1024x1024__steps_19_024844"
"myJob_0009__base_model_realisticStockPhotov20__resolution_1024x1024__steps_20_024844"
"myJob_0010__base_model_realisticStockPhotov20__resolution_1280x1280__steps_18_024844"
"myJob_0011__base_model_realisticStockPhotov20__resolution_1280x1280__steps_19_024844"
"myJob_0012__base_model_realisticStockPhotov20__resolution_1280x1280__steps_20_024844"
```
The save_name (image file name) can be configured with saveNameCFG in config.py:
```
saveNameCFG = 0: Image file name contains no parameters, only jobName, image # and time stamp. 
  myJob_0001_024844

saveNameCFG = 1: Image name contains only the parameter value.
  myJob_0001_juggernautXLv8Rundiffusion_1024x1024_18_024844

saveNameCFG = 2: Image name contains both parameter name and value.
  myJob_0001_base_model_juggernautXLv8Rundiffusion__resolution_1024x1024__steps_18_024844
```
Separators can be modified in `config.py`, for example, the above file names could have been:
```
"myJob_0012----base_model=realisticStockPhotov20----resolution=1280x1280----steps_20_024844"
```


#### Miscellaneous
* This project started out as 6 lines of bash.
* Linux only at this time.
* My first git project.
* Still learning markup.
* My first github project.
* My first python project.
* Getting to that 1st push was painful, wish I knew about this sooner:
`git remote set-url origin https://_my_token_@github.com/daedon/Fooocus-API-XYZ.git`

#### Summary
* Requires `Fooocus-API` to be running.
* Reads parameter files in a job's "parms" subdirectory.
* Files are stored in "jobs/myJobName".
* Each file represents a Fooocus parameter: eg, `___steps`, `___resolution`, `___prompt`, `___base_model`.
* Each parameter file line represents 1 value for that a parameter.
* The 1st character of each file name must be an underscore "_".
* The 1st 3 characters of each file name are used for documentation and/or sorting purposes only.
* The 1st 3 characters of each file are discarded.
* The files are read in alphabetical order, hence the first 3 characters decide the order of the permutations.
* An array variable is created for each parameter with the same name.
* The contents of each parameter file is read line by line into the elements of the corresponding array/list.
* Empty lines are ignored.
* Lines beginning with a "#" are comments and ignored.
* No parameter values are read after a line with a "."
* Fooocus-API-XYZ generates all permutations of the parameter values in the order they were read.
* For each permutation of all the values, Fooocus-API-XYZ makes a curl call to fooocus-API.
* For each permutation, substitutes all `___parameters` in `curl.template`, writes to and executes `runCURL`.

#### Configuring

Directory locations and other parameters can be changed in `config.py`.

If `image_number` is set to N, Fooocus will generate N images per curl call with sequential seed numbers.

To reduce repetiion in large permuations and create N images with random seeds, insert N lines in `___seed` each with a `-1`.


#### Customizing

The curl template has close to 100 parameters, only a dozen or so are set up by default.

For example, "sampler_name" is hard coded in the curl job template. 

```
"sampler_name": "dpmpp_2m_sde_gpu",
```

To make sampler_name one of your variable parameters:
* Edit curl.template and replace `dpmpp_2m_sde_gpu` with `___sampler_name` (keep the quotes).
* In your parms directory, create a file named `___sampler_name` containing your sampler name values.
* Generate images.
* To have sampler_name in all your jobs, do the above to the defaults directories.

#### What's next ?

A Gradio interface for this project.

