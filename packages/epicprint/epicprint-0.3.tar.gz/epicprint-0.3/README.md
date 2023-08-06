# epicprint
Custom print with super powers

## usage
```
from Print import Print

print = Print()

print.info("Welcome").group()
print.success("Now we can:", ["Indent stuff", "Use colors", "Attach semantic to the print statements"])
print.warning("Nothing more to say")
print.reset().fail("Ending with a fail message. Bye.")
```
Result: 

<img src="epicprint.png">

### How to prepare it for upload (note to future self)
```
setup.py sdist bdist_wheel
python -m twine upload dist/*
 ```