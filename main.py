import geopandas as gpd
from longsgis import voronoiDiagram4plg

builtup = gpd.read_file('data/npg-northeast/substation_sites_list.geojson'); 
# builtup.crs = 32650
boundary = gpd.read_file('data/npg-northeast/northern-powergrid-areas.geojson'); 
# boundary.crs = 32650
vd = voronoiDiagram4plg(builtup, boundary)
vd.to_file('data/npg-yorkshire/npg-yorkshire-polygon.geojson', driver='GeoJSON')
