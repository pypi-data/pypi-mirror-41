# CFGeom Tutorial

## Installation

On Windows:

1. Download the Shapely wheel for your version of Python from [Christoph
   Gohlke's Unofficial Windows
   Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely).
2. In a command window, browse to your downloads folder and install Shapely
   using pip, e.g., `pip install Shapely‑1.6.4.post1‑cp27‑cp27m‑win32.whl`
3. Install CFGeom with `pip install cfgeom`

On other operating systems:

1. `pip install cfgeom`

## Create a geometry container with line geometries

In CFGeom, a GeometryContainer object contains one or more geometries. Each
geometry contains one or more parts. Using a polygon with a hole as an example,
the outer ring of the polygon would be one part, and the hole would be a second
part.  It is the geometry part which stores a geometry's x, y, and z
coordinates. Use the following code to create a geometry container with a couple
of line geometries.

```python
from cfgeom import Part, Geometry, GeometryContainer

# Geometries are comprised of one or more parts
# The part holds the node coordinates
x1 = [10, 5, 0]
y1 = [0, 5, 0]
part1 = Part(x1, y1)
# Set the geometry type when you create the geometry
line1 = Geometry('line', part1)  # or 'point' or 'polygon'

# Make another line, this time with z values
x2 = [9, 5, 1]
y2 = [1, 4, 1]
z2 = [1, 1, 1]
line2 = Geometry('line', Part(x2, y2, z2))

# In NetCDF-CF, geometries belong to a geometry container
geometries = [line1, line2]
line_container = GeometryContainer(geometries)

print(len(line_container.geoms))  # 2
```

## Create a polygon with holes

We'll reuse the x and y coordinates from the line example to create a polygon.
A polygon is similar to a line, except that the first and last nodes are assumed
to be connected. Some polygon conventions require the first and last node to be
spatially coincident. This would mean adding a fourth x and y value to each
list, identifical to the first value in the list.  The CF conventions allow this
but do not require it, and so CFGeom does not require this either.

```python
# For polygons, parts can be created as holes
exterior = Part(x1, y1)  # i.e., the part that isn't a hole
hole = Part(x2, y2, is_hole=True)
parts = [exterior, hole]  # The hole comes second
polygon = Geometry('polygon', parts)
polygon_container = GeometryContainer(polygon)

part = polygon_container.geoms[0].parts[1]
print(part.is_hole)  # True
print(part.x)  # [9, 5, 1]
```

## Write and read netCDF

Thus far we've been working purely in Python.  Next let's try reading and
writing geometries to a netCDF file.

Note that CF does require nodes for exterior polygon rings to be listed in
anticlockwise (or counterclockwise in American English), and holes to be in
clockwise order. Even though the nodes we added for the hole earlier were in
anticlockwise order, they are reversed to be placed in clockwise order when
writing to a netCDF file, as demonstrated below.

```python
from cfgeom import read_netcdf

path_to_netcdf_file = 'test_file.nc'
# The next line creates a geometry container named 'geometry_container' by
# default, along with related node variables.  The use_vlen flag indicates
# whether we want to use netCDF classic (False) or netCDF enhanced (True).
# Note that the enhanced approach uses variable length arrays to store the
# node coordinates, which is not covered under CF 1.8.
polygon_container.to_netcdf(path_to_netcdf_file, use_vlen=False)
# There could be several geometry containers in a file
containers = read_netcdf(path_to_netcdf_file)
# Get the container named 'geometry_container'
container_from_nc = containers['geometry_container']['container']

# Nodes for polygon holes are oriented clockwise when writing to netCDF
print(container_from_nc.geoms[0].parts[1].x)  # [1.0, 5.0, 9.0]
```

In this example, we just write the geometries without a data variable. CF
requires a data variable to be in the file if you have geometries, and you can
add a data variable or read an existing data variable using the
[netCDF4](http://unidata.github.io/netcdf4-python/) package, which is outside
the scope of this tutorial. If you already had a data variable in the file, then
to be CF compliant you would just need something like the following code. NOTE:
this code is just example code. It will not work unless you have an existing
'test_file.nc' that already has a streamflow variable in it.

```python
from netCDF4 import Dataset

with Dataset('test_file.nc', 'a') as nc:
   # The data variable is named 'streamflow'
   nc.variables['streamflow'].geometry = 'geometry_container'
```

Want to inspect test_file.nc outside of Python?  You could try [Panoply](https://www.giss.nasa.gov/tools/panoply/download/).

## Write and read Shapely

Shapely is one other most commonly used packages for working with geometries in
Python. CFGeom includes utiilties to convert between CF geometries and Shapely
geometries. Below we continue with the lines from prior examples.

```python
from cfgeom import read_shapely

shapely_lines = line_container.to_shapely()

print(len(shapely_lines))  # 2
print(shapely_lines[0])  # LINESTRING (10 0, 5 5, 0 0)

container_from_shapely = read_shapely(shapely_lines)

print(container_from_shapely.geom_type)  # line
print(container_from_shapely.geoms[0].parts[0].x)  # [10.0, 5.0, 0.0]
```

Want to write your own converter?  Pull requests are welcome!
