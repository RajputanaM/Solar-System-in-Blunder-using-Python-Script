import bpy
import math

# Function to create a sphere
def create_sphere(name, location, scale, color, radius):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=radius, location=location)
    sphere = bpy.context.active_object
    sphere.name = name
    sphere.scale = scale
    mat = bpy.data.materials.new(name + "_material")
    mat.diffuse_color = (*color, 1.0)  # Add an alpha value of 1.0 for full opacity
    sphere.data.materials.append(mat)

# Function to create an orbit
def create_orbit(name, radius, width):
    bpy.ops.mesh.primitive_circle_add(vertices=100, radius=radius, location=(0, 0, 0))
    orbit = bpy.context.active_object
    orbit.name = name
    orbit.rotation_euler = (0, 0, 0)  # Set rotation to zero for a flat circle
    bpy.ops.object.convert(target='CURVE')
    bpy.context.object.data.fill_mode = 'FULL'
    bpy.context.object.data.bevel_depth = width  # Adjust the width of the orbit
    bpy.context.object.data.bevel_resolution = 10
    mat = bpy.data.materials.new(name + "_material")
    mat.diffuse_color = (1, 1, 1, 1)  # White color for orbits
    orbit.data.materials.append(mat)

# Clear existing mesh objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create the sun
create_sphere("Sun", (0, 0, 0), (2, 2, 2), (1, 1, 0), 2)  # Adjust the radius for the Sun

# Create orbits and planets
planet_data = [
    ("Mercury", 7, 0.1, (0.8, 0.8, 0.8), 1),
    ("Venus", 10, 0.1, (0.8, 0.8, 0.7), 2),
    ("Earth", 14, 0.1, (0, 1, 1), 3),
    ("Mars", 18, 0.1, (0.8, 0.8, 0.8), 2),
    ("Jupiter", 25, 0.1, (0.3, 0, 0.67), 2),
    ("Saturn", 32, 0.1, (0.9, 0.8, 0.5), 1.5),
]

for planet in planet_data:
    create_orbit(planet[0] + "_Orbit", planet[1], planet[2])
    create_sphere(planet[0], (0, planet[1], 0), (0.5, 0.5, 0.5), planet[3], planet[4])