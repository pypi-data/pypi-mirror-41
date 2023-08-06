# VectorFields
Scripts to create vector fields that can be used in game engines like Unreal Engine 4 and Unity 3D.  
Have a look at UE4's [documentation](https://docs.unrealengine.com/en-us/Engine/Rendering/ParticleSystems/VectorFields).

## Installation
### via Python Package Index
`pip install vectorfields`
### Bleeding Edge
* To install using development mode:  
`pip install -e git+https://github.com/OlafHaag/vectorfields.git@master#egg=vectorfields`
* To install using regular mode (building the package):  
`pip install https://github.com/OlafHaag/vectorfields/archive/master.zip`

## Usage
You have to know a bit of python and math.

The abstract base classes VectorField and VectorField2D can't be instantiated.

Instantiate a specific vector field, like ElectricDipole2D.  
You can use the __*save* method to write the vector field to disk in FGA or VF format__. To be able to save in vf format, you have to turn instances of VectorField2D subclasses into 3D vector fields with the *to_3d* method. If I'm not mistaken Unity expects *cubic* vector fields with resolution x=y=z.

It's best to preview your vector field directly in engine. Saving to disk usually reloads the file in Unity.  
For other purposes you can use the plot-method of the Vectorfield2D to get a preview.

### Special classes
#### ElectricDipole2D
ElectricDipole2D has 2 special methods to either normalize the vectors and lose all information on field strength or to clamp the field strength to a maximum value. This was necessary, because the physical properties of this field aren't visually pleasing.

#### Belt2D
With this you can place rotating areas in the field that more or less merge together, hence creating the impression of a belt running over pulleys.   
Besides their x and y coordinates each *pulley* has a radius, thickness and speed (negative speed to change direction).

#### CustomUVW
This is a class for quick prototyping and generation of vector fields.

You provide custom functions to the constructor for creating the U, V and W vector components.  
These functions must take 3 parameters that will be substituted for the class' data members grid_x, grid_y, grid_z.  
The return value must be an array of the same shape as grid_x, grid_y or grid_z respectively.

#### CustomUV2D
This is a class for quick prototyping and generation of 2D vectorfields.

You provide custom functions to the constructor for creating the U and V vector components.  
These functions must take 2 parameters that will be substituted for the class' data members grid_x and grid_y.
The return value must be an array of the same shape as grid_x or grid_y respectively.

__2D Examples:__

non-square sine vector field
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.ones(x.shape)  # Flow in one direction.
vfunc = lambda x,y: np.sin(x)
vf = CustomUV2D(ufunc, vfunc, size=[8,2], resolution=[32,8])
vf.plot()
```
regular cosine whirls
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.cos(y)
vfunc = lambda x,y: np.cos(x)
vf = CustomUV2D(ufunc, vfunc, size=16)
vf.plot()
```
"flowers"
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.sin(y + x)
vfunc = lambda x,y: np.cos(x - y)
vf = CustomUV2D(ufunc, vfunc, size=12, resolution=48)
vf.plot()
```
some diagonal flow thingy
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.cos(np.sqrt(np.abs(x)))  
vfunc = lambda x,y: np.cos(np.sqrt(np.abs(y)))  
vf = CustomUV2D(ufunc, vfunc)
vf.plot()
```  
[anvaka's](https://github.com/anvaka/fieldplay) square flow tiles (seriously, it's hard to find names for this stuff)
```python
import numpy as np
from vectorfields import CustomUV2D  
ufunc = lambda x,y: 2.0 * np.mod(np.floor(-y), 2.0) - 1.0
vfunc = lambda x,y: 2.0 * np.mod(np.floor(-x), -2.0) + 1.0
vf = CustomUV2D(ufunc, vfunc, size=5.9, resolution=24)
vf.plot()
```
beautiful twirls
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.cos(np.linalg.norm(np.dstack((x, y)), axis=2))[:,:,np.newaxis]
vfunc = lambda x,y: np.cos(x-y)
vf = CustomUV2D(ufunc, vfunc, size=16)
vf.plot()
```
twirl column
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.sin(y)
vfunc = lambda x,y: x
vf = CustomUV2D(ufunc, vfunc, size=[12, 16], resolution=[24, 32])
vf.plot()
```
something a little bit more complex, "translated" from [anvaka's gallery](https://anvaka.github.io/fieldplay/?dt=0.02&fo=0.998&dp=0.009&cm=1&cx=0.21419999999999995&cy=-0.7710999999999997&w=55.970200000000006&h=55.970200000000006&code=v.x%20%3D%20min%28sin%28exp%28p.x%29%29%2Csin%28length%28p%29%29%29%3B%0Av.y%20%3D%20sin%28p.x%29%3B%0A%20%20)
```python
import numpy as np
from vectorfields import CustomUV2D
def ufunc(x,y):
    grid_norms = np.linalg.norm(np.dstack((x, y)), axis=2)[:,:,np.newaxis]
    return np.minimum(np.sin(np.exp(x)),np.sin(grid_norms))

vfunc = lambda x,y: np.sin(x)
vf = CustomUV2D(ufunc, vfunc)
vf.plot()
```
How much time would it take to do that with effectors and forces?
```python
import numpy as np
from vectorfields import CustomUV2D
ufunc = lambda x,y: np.cos(y**2)
vfunc = lambda x,y: np.cos(y*x)
vf = CustomUV2D(ufunc, vfunc, size=[24, 16], resolution=[48,32])
vf.plot()
```

## History
This little project started at a little game jam with the topic "electricity". I wanted to do something with particles and controlling their flow with formulas, but the available methods for creating vector fields at the time where either too complicated for this small task, or too time consuming or bound to purchasing a software license. Of course, this cannot compete with GUI software like VectorayGen, but it's free and open source.

## Development
Since it did what I needed it got stuck in early development stage. For example, there's a lack of three-dimensional vector field examples and there are no unit-tests.

I'd like to see people creating other vector fields with this and improve and advance the code.
