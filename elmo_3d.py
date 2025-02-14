from build123d import *
from ocp_vscode import show_object

# Create a simple sphere
sphere = Sphere(radius=5)

# Show the model
show_object(sphere, name="sphere", options=dict(alpha=0.5))