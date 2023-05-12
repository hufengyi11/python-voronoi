import geopandas as gpd
from longsgis import voronoiDiagram4plg

#https://github.com/longavailable/voronoi-diagram-for-polygons

builtup = gpd.read_file('data/EPN/epn_bsp.geojson'); builtup.crs = 32650
boundary = gpd.read_file('data/EPN/epn_ops_boundaries.geojson'); boundary.crs = 32650
vd = voronoiDiagram4plg(builtup, boundary)
vd.to_file('data/EPN/epn_polygon_output.geojson', driver='GeoJSON')
