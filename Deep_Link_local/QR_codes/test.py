import geopandas
from shapely.ops import polygonize

f = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            25.396206335919032,
            7.731791691504597
          ],
          [
            25.03308556783739,
            2.4591500709576337
          ],
          [
            29.218071450951328,
            5.723549349690316
          ]
        ],
        "type": "LineString"
      }
    }
gdf = geopandas.GeoDataFrame.from_features(f)

polygons = geopandas.GeoSeries(polygonize(gdf.geometry))

polygons.plot()