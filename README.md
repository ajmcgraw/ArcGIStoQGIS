# ArcGIStoQGIS
Python tools to export ArcGIS vector layers to QGIS


### Exporting Vector Layers to QGIS

This tool was built with ArcPy 3.6 and QGIS Version 3.6. 

### Tool Use

This tool is a script for ArcGIS Pro it is made to export vector layers to QGIS. There are many tools available within ArcGIS Pro, but sometimes the user does not have all the licenses available to use them and needs to use a tool that is available in QGIS. Although it doesn’t take a lot of time to open a vector layer that you have been working on in ArcGIS in QGIS, it can be annoying to have to do multiple times a day. Where I work, I need to use the polygon to line tool multiple times a day, and then use Topo to Raster within ArcGIS on those lines. We do not have access to the Polygon to Line tool in ArcGIS, so I find myself transferring the files between ArcGIS and QGIS frequently. 

### Prerequisites

Before using this tool, you must have QGIS installed though OSGeo4W. If you have QGIS installed a different way, the tool will not be able to access the python that it needs to in this script. The OSGeo4W version of QGIS can be downloaded from the QGIS website. 
This tool will not create a QGIS Project for you. You will need to create one before the tool is used.

### Contents of this Tool Package
•	ArcGIS Pro Toolbox containing the tool

•	toRunQ.py script

•	‘python-qgis.bat’

This package contains this file on what the script does and how to use it, a .py script, and the tool that has already been imported in QGIS. It also contains a file called ‘python-qgis.bat’ this is a file that is referenced in our Python script. This file is automatically downloaded when the user downloads the OSGeo4W version of QGIS, but I have supplied this one just for reference. This file should be stored in ‘C:/OSGeo4W64/bin’ for this tool to work. If OSGeo4W64 is in this location the tool should work without a problem.

### Installing 
1.	Open ArcGIS Pro
2.	Go to the Catalog and right click on Toolboxes
3.	Click ‘+Add Toolbox’ 
4.	Navigate to the folder that you download 
5.	Click on the Toolbox and click OK
6.	You are now ready to Export Vector Layers to QGIS!

### How to Use
#### Parameters:

##### Location Of QGIS:

This will be the location of OSGeo4W. Mine is 'C:\OSGeo4W64' and it will likely be yours as well.

##### QGIS Project:

This is any QGIS Project that you have created.

##### Feature Layer:

You can drag in any Feature layer that it on your map here.

Once these parameters are filed out, open your QGIS Project and your shapefile will be there. If your QGIS Project is already open, you will have to open it again. A QGIS Project does not automatically update the layers when new ones are added through Python

### Future Work and Tools

This tool, ‘Export Vector to QGIS’, will be expanded to be able to export multiple layers at once from ArcGIS Pro. It will also be expanded to accept feature classes. This is just the first tool in this tool set. An additional ArcGIS tool, ‘Import Vector from QGIS’, will be made to read the layers that are in a QGIS project and add them to an ArcGIS Pro project. I will also be making a GitHub page for this project within the next week.
