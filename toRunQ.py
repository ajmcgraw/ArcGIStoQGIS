#######################################################################
#    
#	Export Shapefile from ArcGIS to QGIS (1.0)
#   
#   Anna J. McGraw
#   5/08/2019
#
#
#	This script adds a layer to QGIS. 
#	The second version of this script will read the Arc Mapframe, get all the layers, and add them into QGIS
#	An additional script will read the map layers of a QGIS project and there location and export them back to ArcGIS Pro
#
########################################################################

import os
import arcpy

#this links to the python qgis. This may have to be changed for each computer it is run on.
x = "C:\\OSGeo4W64\\bin\\python-qgis.bat" 

#these are where qgis is located
qapp = str(arcpy.GetParameterAsText(0)).replace('\\','/')#### 'C:\OSGeo4W64'

#where the project is that you would like to modify
qproj = str(arcpy.GetParameterAsText(1)).replace('\\','/')##'C:/Users/annam/Desktop/test.qgz'

#where the shapefile is that you would like to add
qlayer = str(arcpy.GetParameterAsText(2)).replace('\\','/')###'C:/Users/annam/Downloads/waterbodies/arcimports/kerr_225.shp'

space = arcpy.env.scratchFolder
fileShp = str(qlayer) +'.shp'
#had to add this here, without it, I couldn't find the shapefile path
arcpy.FeatureClassToFeatureClass_conversion(qlayer,space, fileShp )

#full path of the shapefile
fullPath = space +'/' +fileShp

#need to replace the // because it keeps exiting the string
fullPath = fullPath.replace('\\','/')

#this will be the script that runs in the qgis python command line
script = """import sys
from qgis.core import *
from qgis.gui import *
import qgis.utils
from qgis.core import QgsApplication


def addLayers(qgis_path, project_location, vectorLayer):

	qgis_path = qgis_path
	QgsApplication.setPrefixPath(qgis_path, True)
	qgs = QgsApplication([], False)
	qgs.initQgis()   #this initilizes QGIS

	project = QgsProject.instance() #this starts the project instance

	project.read(project_location) #this reads the project

	layer = QgsVectorLayer(vectorLayer, 'newLayer', 'ogr') #this defines our vector layer as a vector layer readble by qgis

	project.addMapLayer(layer) #adds it to the project

	project.write() #saves the project
	
	qgs.exitQgis() #closes the qgis application

	
addLayers('""" +qapp +"','"+ qproj +"','"+ fullPath + "')"

#this creates a the python script to run and writes the sctring 'text' to it
with open('script.py', 'w') as writer:
	writer.write(script)

v = x +' script.py'

#this calls the bat file, and then runs the script in the other python window.
os.system(v)

#this removes the python script we created. Whoever is using the tool does not need to see it.
# if os.path.exists('script.py'):
#   os.remove('script.py')