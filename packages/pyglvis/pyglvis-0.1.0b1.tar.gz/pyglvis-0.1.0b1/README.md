pyglvis
=======

Interactive finite element visualization widget for the Jupyter Notebook, built from [GLVis](https://glvis.org).

Installation
------------

To install use pip:

    $ pip install pyglvis
    $ jupyter nbextension enable --py --sys-prefix pyglvis


For a development installation (requires npm),

    $ git clone https://github.com/glvis/glvis-widget.git
    $ cd pyglvis
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix pyglvis
    $ jupyter nbextension enable --py --sys-prefix pyglvis


Built using the [widget-cookiecutter](https://github.com/jupyter-widgets/widget-cookiecutter).
