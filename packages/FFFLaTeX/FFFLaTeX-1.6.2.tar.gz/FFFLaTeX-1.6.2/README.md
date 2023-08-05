
#### Project release informations

[![](https://img.shields.io/pypi/v/FFFLaTeX.svg)](https://pypi.org/project/FFFLaTeX/)
![](https://img.shields.io/pypi/pyversions/FFFLaTeX.svg)
![](https://img.shields.io/github/languages/code-size/helldragger/FactorioFridayFactsLaTeX.svg)

#### Activity
[![](https://img.shields.io/pypi/dm/FFFLaTeX.svg)](https://pypi.org/project/FFFLaTeX/)
![](https://img.shields.io/github/commit-activity/y/helldragger/FactorioFridayFactsLaTeX.svg)
![](https://img.shields.io/github/last-commit/helldragger/FactorioFridayFactsLaTeX.svg)

#### Licensing
![](https://img.shields.io/github/license/helldragger/FactorioFridayFactsLaTeX.svg)

## Installation
You will need python 3.6+ and pip

```bash
> pip install --upgrade FFFLaTeX
```

## Usage

``` bash
> FFFLaTeX [<Number of the relevant FFF>|latest]
```

## Output tex file

The tex file for the FFF XXX will be located under a new folder FFFXXX where you used the FFFLaTeX command, as FFFXXX.tex

This lets you directly modify and compile the tex file under its own folder without dealing with multiple outputs

```bash
> FFFLaTeX
....
> 277
....
> ls
....... ./FFF277/
```

You can also use the command line directly as of 1.4

```bash
> FFFLaTeX 277
....
> ls
....... ./FFF277/
```

You can also just generate the latest FFF now (xxx being the latest fff version on the factorio.com/blog/ listing)

```bash
> FFFLaTeX latest
....
> ls
....... ./FFFXXX/
```

## Configuration

You can now configure both the LaTeX templates per tag but also use an hybrid scripting system!

This hybrid system lets you call any registered python function from the configSymbol.py file at specific points in your LaTeX templates, allowing you to generate your document dynamically!

![Config scheme](Config.PNG)

The LaTeX templates can be modified in the configLaTeX.py file

The linking and function declarations can be modified in the configSymbol.py
