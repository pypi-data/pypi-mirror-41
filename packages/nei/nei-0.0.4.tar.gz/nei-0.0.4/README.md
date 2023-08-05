# NEI

**Notebook Emacs Integration.**


<img src="https://s3-eu-west-1.amazonaws.com/misc-static-assets/labmode-README.gif" width="90%"><img>

The goal of NEI is to allow Python [Jupyter
notebooks](https://jupyter.org/) to be edited efficiently as plaintext,
allowing you to use all the text and code editing tools you are familiar
with to work as effectively with notebooks as with regular code files.

The above GIF shows a demo of NEI being used in emacs on the
left-hand side while the results reflected live on the right-hand side
in Firefox. The file in emacs is a regular Python file using vanilla
Python syntax - the yellow code prompts are simply pretty printed for
clarity. For instance, the yellow ``In[1]`` is simply the visual
representation of the comment ``# In[1]``.

## Motivation

There are several projects offering alternatives to the [Jupyter
notebook](https://jupyter.org/) interface such as
[hydrogen](https://github.com/nteract/hydrogen) and
[nteract](https://github.com/nteract/nteract). Emacs users can already
make use of the
[EIN](https://github.com/millejoh/emacs-ipython-notebook) project so why
use NEI?

Unfortunately EIN cannot display HTML and JavaScript output as there is
no way to inline such content. Emacs is not based on web technologies
(thankfully!) which means it does not have access to the required
rendering engines. This limitation greatly reduces the utility of EIN if
you have to work with interactive visualizations such as those generated
by [holoviews](http://holoviews.org/) and
[bokeh](https://bokeh.pydata.org/en/latest/).

The core features are NEI are:

1. Work with Jupyter Notebooks containing interactive visualizations
   without leaving your editor.
2. Freeform text editing without hard cell boundaries. Notebooks can now
   be edited and worked with as regular, plaintext Python files.
3. Editor agnostic by design, with robust Emacs support.

To use NEI you will need to have both your editor and browser
visible simultaneously as shown in the GIF above. This is no problem for
people working on multiple monitors and laptop users should have no
trouble splitting the screen, especially if they can easily tile windows
e.g OSX users can use
[spectacle](https://github.com/eczarny/spectacle). The partially
decoupled view in the web browser avoids the problem of having code
change position as output is generated and will allow NEI to view
select portions of the overall notebook as you work.

NEI is composed of three components, (1) a Python server using
[tornado](http://www.tornadoweb.org/en/stable/) which receives commands
from the editor via websockets, (2) HTML and Javascript that runs in the
browser, and (3) the code used to integrate with the editor. Currently
this last component is written in elisp as the first editor to be
supported is [emacs](http://emacs.org). As the server and web component
are editor agnostic, there is no reason NEI cannot be extended to
support any text editor that has support for websockets.

**NEI is currently an experimental prototype and should not be
considered stable.**

## Python dependencies

You can conda install the four python dependencies as follows:

```
conda install tornado ansi2html jupyter_client
```

The ``ansi2html`` dependency will soon not be necessary and the
``cssutils`` dependency is only used to apply theming to holoviews bokeh
plots. This dependency will be made optional but for now it is required:

```
pip install cssutils
```

## Browser configuration

NEI is written in ES6 and is not yet configured to compile to ES5
with babel. This means you will need a recent browser and you may need
to enable JavaScript module support in your browser:

Firefox 58: Go to [about:config](about:config) and set
``dom.moduleScripts.enabled`` to ``true``.

Chrome: Go to [chrome://flags/](chrome://flags]) and set
``enable-javascript-harmony`` to 'Enabled'.

These steps will not be necessary as browsers start to enable these
settings by default and once NEI offers an ES5 version of the
Javascript code.

## Tips

NEI currently supports [miniconda3](https://conda.io/miniconda.html)
environments. You can make a python file automatically enable NEI
and switch to a miniconda3 environment (here ``"example-env"``) by
putting this line at the top of your Python file:

```
# -*- mode: python; nei-env : "example-env"; eval: (nei-mode)-*-
```

The environment used will have to satisfy the Python dependencies listed
above. If you don't use miniconda you will need to set the
``nei-python-path`` elisp variable.

## Emacs configuration

NEI does not yet have an emacs package but it only has two elisp
dependencies given a recent version of emacs:
[``s``](https://melpa.org/#/s) and
[``websocket``](https://melpa.org/#/websocket). These can be easily
installed using the ``package-list-packages`` command if you have
pointed to a suitable elisp package repository such as
[MELPA](https://melpa.org/).

You will also need to add NEI to your ``.emacs`` file by pointing to
the ``emacs`` subdirectory of this repository:

```elisp
(add-to-list 'load-path "~/nei/emacs")
(require 'nei-mode)
```

Eventually a MELPA package will be offered for NEI.

### Usage

To get started, the most important keybindings are ``C-c v`` to open a
view of the buffer in the selected browser (Firefox by default), ``C-c
c`` to insert a code cell, ``C-c m`` to add a markdown cell and ``C-c
e`` to execute a cell.


```elisp
  (define-key map (kbd "C-c W") 'nei-write-notebook)
  (define-key map (kbd "C-c I") 'nei-insert-notebook)
  (define-key map (kbd "C-c E") 'nei-exec-by-line)
  (define-key map (kbd "C-c L") 'nei-clear-all-cell-outputs)
  (define-key map (kbd "C-c C") 'nei-update-css)

  (define-key map (kbd "C-c w") 'nei-move-cell-up)
  (define-key map (kbd "C-c s") 'nei-move-cell-down)
  (define-key map (kbd "C-c <down>") 'nei-move-point-to-next-cell)
  (define-key map (kbd "C-c <up>") 'nei-move-point-to-previous-cell)
  (define-key map (kbd "C-c c") 'nei-insert-code-cell)
  (define-key map (kbd "C-c m") 'nei-insert-markdown-cell)
  (define-key map (kbd "C-c e") 'nei-exec-by-line-and-move-to-next-cell)
  (define-key map (kbd "C-c i") 'nei-interrupt-kernel)
  (define-key map (kbd "C-c r") 'nei-restart-kernel)
  (define-key map (kbd "C-c l") 'nei-clear-cell-by-line)
  (define-key map (kbd "C-c n") 'nei-clear-notebook-and-restart)

  (define-key map (kbd "C-c v") 'nei-view-browser)
  (define-key map (kbd "C-c V") 'nei-view-notebook)
```

The elisp variable ``nei-browser`` can be set from 'firefox' to
'chrome' if you prefer to view the notebooks in the Chrome browser.


## Scope of the project

A few notes on the current scope of the project. As the project progress, support for features currently out of scope will be considered.

* At this time, NEI only aims to support Python and IPython syntax.
* The primary focus is currently on ensuring robust emacs support but contributions to support other editors are welcome.
* One key objective is to support rich interactive visualization with [holoviews](http://holoviews.org/), which means supporting [bokeh](https://bokeh.pydata.org/en/latest/) plots. 
* Support for other complex Javascript components such as ipywidgets can be added if contributors volunteer to maintain and test those aspects of the project.
