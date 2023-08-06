Superslug - make URL slugs from arbitrary strings
==================================================


Superslug elegantly handles punctuation, unicode characters, apostrophes,
and stop words to produce url friendly slugs.

Example:

.. code:: python

    from superslug import slugify

    # Will return 'one-two-threeeee'
    slug = slugify('one! - two! thréééee!')


