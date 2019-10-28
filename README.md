<p align="center">
  <a href="" rel="noopener">
 <img width=960px height=540px src="img/logo.png" alt="Project logo"></a>
</p>

<h1 align="center">Python Utility Functions</h1>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/rednafi/meta-utils/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/rednafi/meta-utils/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---
## ⚙️ Installation

Run
```bash
pip install pyfoster
```
## 💡 Usage
Let's say you want to log the exception of a specific function. To do so:
```python
from pyfoster.custom_logger import logfunc

# define the function with logfunc decorator
@logfunc
def zero_div(a, b=0):
    return a // b

# run the function
if __name__ == "__main__":
  print(zero_div(5))
```

This will show the exception with the function name in the console and send that to `logs/logs.log` file.

```bash
pyfoster.custom_logger - ERROR - There was an exception in  zero_div
Traceback (most recent call last):
  File "/home/redowan/code/pyfoster/pyfoster/custom_logger.py", line 74, in wrapper
    value = func(*args, **kwargs)
  File "/home/redowan/code/pyfoster/example.py", line 7, in zero_div
    return a // b
ZeroDivisionError: integer division or modulo by zero
None
```


## ✍️ Authors <a name = "authors"></a>
- [@rednafi](https://github.com/rednafi) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/rednafi/contributors) who participated in this project.

## 🎉 Acknowledgements & References <a name = "acknowledgement"></a>

### Decorators
  * [Primer on Python Decorators - Real Python](https://realpython.com/primer-on-python-decorators/)
  * [Python: How to Create an Exception Logging Decorator](http://www.blog.pythonlibrary.org/2016/06/09/python-how-to-create-an-exception-logging-decorator/)

### Logging
  * [Logging in Python -Real Python](https://realpython.com/python-logging/)
  * [Python Logging: A Stroll Through the Source Code -Real Python](https://realpython.com/python-logging-source-code/)
