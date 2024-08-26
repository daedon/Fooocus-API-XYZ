### Fooocus-API-XYZ: Variable Parameter Image Generator for Fooocus-API
Generates a series of Fooocus images with unrestricted parameter variations. 

`Requires Fooocus-API installed and running.`


#### Quick Start


Get it:
```
git clone https://github.com/daedon/Fooocus-API-XYZ
```
Run it:
```
cd Fooocus-API-XYZ
python3 xyz.py myJob

```
Create a new job:
```
cd Fooocus-API-XYZ
python3 xyz.py jobName

```
The first time you use a jobName:
* A directory with the job's name will be created in "Fooocus-API-XYZ/jobs".
* Associated sub-directories will be created.
* Default files will be copied to "jobs/jobName".
* Add, Modify, Delete parameters in "jobs/jobName/parms".
* To set default parameters for all future jobs, edit the `defaults` directories.

##### A simple example with 3 parameter files that have more than 1 value is included in myJob.

Parameter files are located in the `../Fooocus-API-XYZ/jobs/myJob/parms` directory. The following table contains 5 samples from the demo job.
The characters in the first 3 positions of the file name serve to sort and determine the order the parameters will be processed.
In the example below, only the base_model, resolution and guidance_scale will be used to build the image file name since only they vary.
xyz will generate all permutations of the following parameters and make curl calls to Fooocus-API.

| FILE NAME       | _0_steps         | _1_base_model    | _2_resolution   |_3_guidance_scale|  ___image_number |
| ----------------| ---------------- | ---------------- |---------------- |----------------|---------------- |
| line 1 in file  | 22               | juggernautXL_v8  | 512*640         | 2.0             | 1               |  
| line 2 in file  |                  | realisticPhoto   | 640*640         | 3.0             |                  |                 
| line 3 in file  |                  |                  | 1024*1024       |                 |                  |                 

The parameters in the table above should produce the following output:
```
Job "myJob" has 13 parameters:
  ['steps', 'base_model', 'resolution', 'guidance_scale', 'image_number', 'negative_prompt', 'performance', 'prompt', 'refiner_model', 'refiner_switch', 'seed', 'sharpness', 'style']
The following parameters have more than one value:
  base_model[2] 
  resolution[3] 
  guidance_scale[2] 
Fooocus "image_number" is set to 1 image per Curl call
12 Curl calls will be made.
12 images will be generated (2 * 3 * 2 * 1)
Generate the 12 images now ? (y/n) y
"myJob_0001_steps_25_base_model_juggernautXLv8_resolution_512x512_guidance_scale_2.0_082317"
"myJob_0002_steps_25_base_model_juggernautXLv8_resolution_512x512_guidance_scale_3.0_082317"
"myJob_0003_steps_25_base_model_juggernautXLv8_resolution_640x640_guidance_scale_2.0_082317"
"myJob_0004_steps_25_base_model_juggernautXLv8_resolution_640x640_guidance_scale_3.0_082317"
"myJob_0005_steps_25_base_model_juggernautXLv8_resolution_1024x1024_guidance_scale_2.0_082317"
"myJob_0006_steps_25_base_model_juggernautXLv8_resolution_1024x1024_guidance_scale_3.0_082317"
"myJob_0007_steps_25_base_model_realisticPhotov20_resolution_512x512_guidance_scale_2.0_082317"
"myJob_0008_steps_25_base_model_realisticPhotov20_resolution_512x512_guidance_scale_3.0_082317"
"myJob_0009_steps_25_base_model_realisticPhotov20_resolution_640x640_guidance_scale_2.0_082317"
"myJob_0010_steps_25_base_model_realisticPhotov20_resolution_640x640_guidance_scale_3.0_082317"
"myJob_0011_steps_25_base_model_realisticPhotov20_resolution_1024x1024_guidance_scale_2.0_082317"
"myJob_0012_steps_25_base_model_realisticPhotov20_resolution_1024x1024_guidance_scale_3.0_082317"
```
The save_name (image file name) can be configured with saveNameCFG in config.py:
```
saveNameCFG = 0: Image file name contains no parameters, only jobName, image # and time stamp. 
saveNameCFG = 1: Image name contains only the parameter value.
saveNameCFG = 2: Image name contains both parameter name and value.

0: myJob_0001_024844
1: myJob_0001_juggernautXLv8_1024x1024_18_024844
2: myJob_0001_base_model_juggernautXLv8__resolution_1024x1024__steps_18_024844
```

If `saveNameCFG` is 1 or 2, parameters with more than 1 value will automatically be included in the file name.

To force the inclusion of a parameter with only one value, terminate the parameter's file name with an "_", eg `___seed_`.

Separators can be modified in `config.py`, for example, the above file names could have been:
```
"myJob_0012----base_model=realisticPhotov20----resolution=1280x1280----steps_20_024844"
```
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
```
"sampler_name": "___sampler_name",
```
* In your parms directory, create a file named `___sampler_name` containing your sampler_name values.
* Generate your images.
* To have sampler_name in all your jobs, make the above changes to the defaults directories.

#### What's next ?

A Gradio interface for this project.

#### Miscellaneous
* This project started out as 6 lines of bash.
* Linux only ()at this time.)
* My first git project.
* Still learning ~~markup~~ markdown.
* My first github project.
* My first python project.
* Getting to that 1st push was painful, wish I knew about this sooner:
`git remote set-url origin https://_my_token_@github.com/daedon/Fooocus-API-XYZ.git`






















