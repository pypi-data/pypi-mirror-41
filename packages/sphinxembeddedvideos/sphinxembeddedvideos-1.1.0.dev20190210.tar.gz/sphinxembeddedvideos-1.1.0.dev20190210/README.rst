sphinxembeddedvideos
====================

Embed videos in your Sphinx-generated documentation.

.. code::

   pip install sphinxembeddedvideos

Supported platforms:

- PeerTube (@peertube.social)
- YouTube


Usage
-----

Enable the Sphinx extension(s) in your ``conf.py`` file:

.. code:: python

   extensions = [
       '...',
       'sphinxembeddedvideos.peertube',
       'sphinxembeddedvideos.youtube',
   ]

You can then use the corresponding directives (`peertube`, `youtube`) to embed
a video given its ID::

   .. peertube:: da2e6b0c-d2ed-4799-8bca-bf24ff2abe45

Or, for a YouTube video::

   .. youtube:: oHg5SJYRHA0

The referenced video will be embedded into HTML output. By default, the
embedded video will be sized for 720p content. To control this, the
parameters "aspect", "width", and "height" may optionally be provided::

    ..  youtube:: oHg5SJYRHA0
        :width: 640
        :height: 480

    ..  youtube:: oHg5SJYRHA0
        :aspect: 4:3

    ..  youtube:: oHg5SJYRHA0
        :width: 100%

    ..  youtube:: oHg5SJYRHA0
        :height: 200px
