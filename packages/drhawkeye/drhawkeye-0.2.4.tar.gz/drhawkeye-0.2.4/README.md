# drhawkeye
Check the health of your program outputs

## About
This package can be used to check the outputs of a program that outputs
following a consistent directory structure. The motivation was to check
the NetCDF outputs of the Automated Water Supply Model [(AWSM)], which
can output snowpack and energetics files every day.

### Usage
Look at the ```examples/test_config.ini```, used in ```examples/test.py```.
In the config file, a *pattern* and *file* must be given. The pattern is the
directory path with asterisks where the pattern should be inferred. The file
is the file name, not the path (i.e. ```snow.nc```).

The ```min_size``` is the minimum file size that any file should be in kB.
The ```netcdf_vars``` is a list of variables to check for in the NetCDF file.

The ```check_vars```, ```check_file```, and ```check_size``` are True or False
values used to turn the checks on or off

The results of the checks will print out in a standard inicheck report. If the
test passed, it will not appear in the inicheck log.

## Current Status
The project is in its early stages. The check functionality will use
the [inicheck] framework to run tests on outputs from any application following
a consistent directory tree pattern. Checks will include file existence,
file size, and file variables if the file is a NetCDF.

[inicheck]: https://inicheck.readthedocs.io/en/latest/
[(AWSM)]: https://github.com/USDA-ARS-NWRC/awsm
