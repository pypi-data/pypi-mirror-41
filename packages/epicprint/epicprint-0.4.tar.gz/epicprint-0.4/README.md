# epicprint
Custom print with super powers

## installation
```
pip install epicprint
```

## usage
```
from epicprint.Print import Print

print = Print()

print.info("Welcome").group()
print.success("Now we can").group()
print.success("Indent stuff").success("Use colors").success("Chain")
print.ungroup().warning("This is my first package")
print.reset().fail("Ending with a fail message. Bye.")
```
Result: 

<img src="epicprint.png">

### How to prepare it for upload (note to future self)
```
# upgrade the version in setup.py
setup.py sdist bdist_wheel
python -m twine upload dist/*
 ```
When installing you might want to uninstall or ignore cache
```
pip uninstall epicprint
pip install epicprint --no-cache-dir
```