# npspellcheck  

**spell checking jupyter notebooks**

Writing correctly should be a priority, even for programmers and scientists. 

But this is not easy in jupyter notebooks. 

In english, a good solution is to make use of the spellchecker notebook extension, which highlights incorrect text: 

```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
jupyter nbextension enable spellchecker/main
```

However, this extension is currently not able to suggest corrections, and is only available for English. 

Since I write blog posts based on jupyter notebooks in French, I came up with a small script for spell checking. 

Installation: 

```
pip install nbspellcheck
```

Example of use:

```
nbspellcheck.py my_jupyter_notebook.ipynb -l fr
```

A big thank you to the developers of 

* [nltk](http://www.nltk.org/) : python natural language toolkit
* [pyspellchecker](https://pypi.org/project/pyspellchecker/) : python spell checker

that are doing all the heavy lifting. 

I made this real fast, and the user interface can be improved. Please don't hesitate to send a PR. 

