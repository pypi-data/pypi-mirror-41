This installation was previously tested only with Linux, but should also work under Windows.  

## Installation Description (PyPi)  
https://pypi.org/project/extractTool/  
```bat 
pip install extractTool
```  
   
(you can write this command in your console and follow the installation description on the webside OR    you can download the file and install the CLI tool local: )   
## Installation Description (local)
 
pip for pip install is required.   

**After downloading our Tool from PyPi** 
To run our CLI tool, the following file must be executed in the project folder:   
     
```bat 
pip install -r requirements.txt --user (or sudo pip install -r requirements.txt) 
```
   
In this file all required plugins are listed, which we use in our tool.      

Because sometimes there are some problems with the installation you must follow these next steps:   
First, ensure you have gdal installed. I just run the following:
```bat 
sudo apt-get install libgdal1i libgdal1-dev libgdal-dev
```
To get the version that apt-get provided you please run: 
```bat
gdal-config --version
``` 
For example I get 2.2.3 so my pygdal version will be 2.2.3.3. (but replace the version with your version)
```bat
pip install pygdal==2.2.3.3
```
If you get some error you may look [here](https://stackoverflow.com/questions/32066828/install-gdal-in-virtualenvwrapper-environment)

Next step:
```bat 
pip install pytest   
```      
Then you can navigate in any common console in the folder of the tool (*"extractTool"*) and
there, the following command must be executed   

```bat 
python extractTool.py --path='[filepath]' --detail=[bbox|convexHull] --time
```
 for `filepath` you must insert a filepath to your testdata
 
`--bbox` &larr; for the bounding box of the file/folder (set as default)  
`--convexHull` &larr; to get all the covexHull of the file/folder   
`--time` &larr; (optionally) You can add this parameter to get additionally the timeextend   

### some examples
```bat
python extractTool.py --path='/home/maxmusterman/test1.geojson' --detail=bbox --time   
python extractTool.py --path='/home/maxmusterman/test2.nc' --detail=convexHull
python extractTool.py --path='/home/maxmusterman/testdict' --time
```
