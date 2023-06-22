It contains the instructions for using Attached file.

Setting up Google Earth Engine in Anaconda For the first time
1. Open Anaconda Powershell prompt
2. conda create --name gee
3. y
4. conda env list                             #To check whether the gee is installed or not
5. conda activate gee                         #Sets the environment to gee
6. conda install -c anaconda jupyter
7. y
8. conda install -c conda-forge geemap
9. y
10. conda install -c conda-forge pytest-shutil
11. conda install -c anaconda requests
12. conda install -c conda-forge retry
13. jupyter notebook                           #Opens the jupypter notebook

Getting Started
1. Goto website https://export.hotosm.org/en/v3/exports/new/describe
2. Specify the feature of interest from specific region.
3. Select .shp file as the required extension to export. 
Provide the .geojson file for clipping the region of interest (It can be extracted from https://github.com/mesaugat/geoJSON-Nepal and splitting the required boundary by opening the text from notepad and saving the clipped region as geojson)
4. Extract the downloaded file.
5. Open https://code.earthengine.google.com
6. Log In or Create Id if required.
7. Goto Assets Tab
8. Click New > Shape Files
9. Select .dbf, .shp, .shx and .prj files that is recently downloaded. If Multiple files with same extension then larger file preference needs to be given.
10. Specify Asset name and Upload selected files.
11. Uploading may be time consuming. Upload process can be observed from Tasks tab in top right corner.
12. After completion, Click on recently added Asset name under Asset Tab.
13. Under Table ID the text is the required parameter that need to be placed inside parenthesis of ee.FeatureCollection(), every time the code is launced.

Instructions of Use
1. Download the coded files .ipynb as attached.
2. Open with jupyter notebook.
3. Adjust the parameters in it if needed.
4. Run all of the code inside file.
