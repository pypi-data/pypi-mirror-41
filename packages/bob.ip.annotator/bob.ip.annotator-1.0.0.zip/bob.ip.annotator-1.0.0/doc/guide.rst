.. -*- coding: utf-8 -*-

=================
 Annotator Guide
=================

This guide explains step by step, how to annotate images using the built-in
annotation app.  We will use an example image from Lenna_ for this tutorial.
The annotator app is agnostic to images and can load anything that is supported
by :py:mod:`bob.io.image`.


Image annotation
----------------

The application is launched via command-line, which means you need a command
prompt, pre-configured with the conda_ environment containing this package.
Open such prompt (e.g. via a *Terminal* application) and pass the root path
containing the image you would like to annotate:

.. code-block:: sh

   $ conda activate myenv
   (myenv) $ bob annotate -vv /path/to/images /path/to/annotations


The output path, marked on the above example with ``/path/to/annotations`` is
the directory where annotated points will be written to.  This path is created
if it does not exist.  If it does exist, annotations are preloaded for each
image inside ``/path/to/images`` if they exist and annotation is resumed from
the point it was stopped.

The app will scan for image files with a given extension name (``.png`` by
default) on the input path provided (e.g.: ``/path/to/images``).  Images will
then be sorted and displayed in alphabetical order, one after the other so you
can annotate or review their annotation.  Annotations are saved to the output
directory copying the *same folder structure* found on the input path.  For
example, if the images were lying like this on the input path:

.. code-block:: text

   /path/to/images/subfolder1/image.png
   /path/to/images/subfolder2/image.png
   /path/to/images/subfolder3/subfolder/image.png


Then, the output path will contain the following files, after the user
annotated all images:

.. code-block:: text

   /path/to/annotations/subfolder1/image.json
   /path/to/annotations/subfolder2/image.json
   /path/to/annotations/subfolder3/subfolder/image.json


Annotation format
-----------------

Annotations are saved in JSON_ format, which is easily readable and loadable in
a variety of programming environments.  The specific format used by the
annotator application may change, but it essentially just lists annotated
points, in the order objects are created.


Zoom
----

You may alternatively control the size of the image being annotated by passing
a *zoom* parameter (floating point number within the range ``]0,+inf[``).  A
zoom of ``1.0`` (the default), displays images as they are.  A zoom larger than
``1.0`` upscales the input image making it look bigger than they originally
are.  A zoom factor smaller than ``1.0`` does the inverse, scaling down the
input image.  Annotations recorded on the image are *independent* of the zoom
factor and compensated upon saving operations.  To change the zoom factor, use
the ``--zoom`` parameter of the annotator app, while starting the application.
For example, to start the application with a zoom factor of ``2.0`` do:

.. code-block:: sh

   (myenv) $ bob annotate -vv --zoom=2.0 /path/to/images /path/to/annotations


.. tip::

   You should try to use a zoom factor which is the largest possible given your
   screen resolution.  The image should fit comfortably on the screen without
   resizing the drawing window.  The higher the zoom factor, the more precise
   will be your annotation.  Conversely, the lower, the less precise.

   The application supports automatic resizing of the canvas to fill all the
   available application area, without distorting the image or the annotations.
   Use this feature to select the largest possible annotation area (typically
   by fully maximizing the annotation window), which will give you the best
   possible precision.


Further help
------------

Use the flag ``--help`` to list all options and examples from the annotation
app:

.. code-block:: sh

   (myenv) $ bob annotate --help


Read the annotator application help message, which lists all known keyboard and
pointer/mouse bindings.  Familiarise yourself with these shortcuts as that
improves annotation performance, reducing the time you spend annotating images.
You can check the contents of the help dialog through this documentation,
looking at the docstring of the :py:mod:`bob.ip.annotator.gui` module.


.. include:: links.rst
