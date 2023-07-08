# Python Memory Profiler

## Description

This is a cool python package that show the memory usage of your script. This is super helpful when you are trying to optimize your data pipeline code.

## Setup

```
poetry add memory_profiler matplotlib
```



You can run your script with the memory profiler by executing the following command. It will generate a .dat file with the memory usage information:


```
poetry run mprof run main.py
```

You can plot the data in the .dat file. The following command will generate a PNG file with the memory usage:

```
poetry run mprof plot
```



![](./app/images/result.png)

## References

- https://pypi.org/project/memory-profiler/