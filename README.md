# Megabus Scraper

This project is a web spider made with the scrapy framework that searches megabus from today until the latest day tickets are posted, and outputs a json with all of the ticket prices. (the current version only looks at philly-ny, can be changed)

### Set up Environment

To use this project you need to have pythom, pip, and scrapy.

#### Install Python

First check if python is installed with:

```
which python
```

you should see some output with a filepath to python on your computer. If you see no output, install python [here](https://www.python.org/downloads/).

#### Install pip

First check if pip is installed with:

```
which pip
```

you should see some output with a filepath to pip on your computer. If you see no output, install pip [here](https://pip.pypa.io/en/stable/installing/).

#### Install Scrapy

First check if scrapy is installed with:

```
which scrapy
```

If you don't see that scrapy is installed install it with:

```
pip install Scrapy
```

### Running the Project

Once your environment is set up, navigate to the project directory and run:

```
scrapy runspider megabus
```

If you want to save the output to a file called megabus.json use:

```
scrapy runspider -o megabus.json megabus
```


