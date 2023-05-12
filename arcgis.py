# Name: CreateThiessenPolygons_Example2.py
# Description: Creates Thiessen polygons
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/create-thiessen-polygons.html
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/data.gdb"
 
# Set local variables
# The point input features from which Thiessen polygons will be generated. As feature layer
inFeatures = "schools"
outFeatureClass = "c:/output/output.gdb/thiessen1"
outFields = "ALL"
 
# Run CreateThiessenPolygons
arcpy.analysis.CreateThiessenPolygons(inFeatures, outFeatureClass, outFields)