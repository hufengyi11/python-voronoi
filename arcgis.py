import arcpy
arcpy.env.workspace = "C:/data/data.gdb"
arcpy.analysis.CreateThiessenPolygons("schools", "c:/output/output.gdb/thiessen1", "ALL")