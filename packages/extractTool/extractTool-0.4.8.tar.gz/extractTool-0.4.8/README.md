# Use as CLI-Tool
   
## Install
   
`pip install extractTool`

In addition, the following commands must be executed (if necessary with sudo):   
`apt-get install python-gdal`     
`apt-get install gdal-bin`   

`pip install pytest`

## Usage

`python detailebenen.py --path="<filepath>"`

behind it can still be added specifications:

Options:   
`--bbox` &larr; for the bounding box of the file (is also set as default)      
`--convexHull` &larr; to get all the coordinates of the file      
`--time` &larr; to get the time of a file      
