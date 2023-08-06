# cilantro
> Python Robot API for the CamJam Edukit 3

## Example usage

```python
from cilantro import Robot
from time import sleep

# Create instance of robot
robot = Robot()

# Go forward for 5 seconds then stop
robot.motors.m0 = 100
robot.motors.m1 = 100
sleep(5)
robot.motors.m0 = 0
robot.motors.m1 = 0
```


## Distribute
Create source distribution
```
python setup.py sdist
```

Create wheel
```
python setup.py bdist_wheel
```

Upload to pypi
```
twine upload dist/*
```