# dcase2021_task2_ar_frame_seq_model

## Before running any of the scripts
Make sure to change the locations of the datasets and destination results and model folders in the yaml files

## Modification Warning
This code is modified to augment the dataset using pitch shifting.
After running this code add the augmented dataset to your original dataset then return to the original code by
replacing the code in the basedata file by original basedata file all found in data folder, 
then change line 523 in pptunetf-final.py to "dict(aug_count=0, aug_gadd=0.0, aug_wcut=0,),".
This will make you run the original code and proceed with the rest of instructions.

## How to run the script
To run the script, type the following into Powershell:
```
git clone https://github.com/AbdoM23/bachelor.git
cd bachelor
$env:PYTHONPATH = "."
python -u .\run\pptunetf\pptunetf-final.py
```
After execution, if the .csv extension is associated with MS Excel,
MS Excel will display a csv file summarizing the experimental results.

## Precautions for execution
### Long filename
For Windows, long filenames must be enabled.
File names tend to be long because they include strings of hyperparameters.
File names that exceed 260 characters are more likely to cause file errors.
It is recommended to enable long filenames to reduce the occurrence of such cases.

### Not directly use
The following scripts in the top folder are not intended for direct use.
```
_00_train.py
_01_test.py
_03_collect_results.py
_04_run_job.py
```
These scripts are indirectly called from the scripts under the run folder (for example, "run\pptunetf\pptunetf-final.py").
You can call them directly, but in that case you are responsible for giving full command line arguments by hands.
To reduce the pain, it is recommended to use the scripts under the run folder.

## How to control the model dependencies on the machine_type, section and target.
The model dependencies can be controled by editing the following lines in the script ".\run\pptunetf\pptunetf-final.py".
```
# .\run\pptunetf\pptunetf-final.py
    t0 = time.time()
    #run_job(**hyper_params) # pos-enc == 'none'
    #run_job(**hyper_params_v2)
    #run_job(**hyper_params_v3)
    #run_job(**hyper_params_v4) # data_size==-2, (f_machine=1, f_section=0, f_target=0)
    run_job(**hyper_params_v4a) # data_size==-2, (f_machine=1, f_section=0, f_target=0)
    #run_job(**hyper_params_v5) # model_for=(f_machine=1, f_section=1, f_target='pp-raw-tf6')
```
where, the "hyper_params_v4a" variable is defined in the same script as:
```
# .\run\pptunetf\pptunetf-final.py
hyper_params_v4a = dict(
  model_for=[
            ...,
            dict(f_machine=1, f_section=0, f_target=0),
            ...,
            ],
)
```
In the above example, the model depends on the machine_type but not on the section and target.

- The below summarizes the possible combinations of dependencies on the machine_type, section and target.
```
dict(f_machine=0, f_section=0, f_target=0) # -> machine_type independent (a single whole model)
dict(f_machine=1, f_section=0, f_target=0) # -> dependent on machine_type (independent of section and target)
dict(f_machine=1, f_section=1, f_target=0) # -> dependent on machine_type and section (independent of target)
dict(f_machine=1, f_section=0, f_target=1) # -> dependent on machine_type and target (independent of section, transfer learning)
dict(f_machine=1, f_section=1, f_target=1) # -> dependent on machine_type, section and target (transfer learning)
```
