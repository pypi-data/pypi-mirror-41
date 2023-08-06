
HTRC-Features |Build Status| |PyPI version| |Anaconda-Server Badge|
===================================================================

Tools for working with the `HTRC Extracted Features
dataset <https://sharc.hathitrust.org/features>`__, a dataset of
page-level text features extracted from 13.7 million digitized works.

This library provides a ``FeatureReader`` for parsing files, which are
handled as ``Volume`` objects with collections of ``Page`` objects.
Volumes provide access to metadata (e.g. language), volume-wide feature
information (e.g. token counts), and access to Pages. Pages allow you to
easily parse page-level features, particularly token lists.

This library makes heavy use of `Pandas <pandas.pydata.org>`__,
returning many data representations as DataFrames. This is the leading
way of dealing with structured data in Python, so this library doesn't
try to reinvent the wheel. Since refactoring around Pandas, the primary
benefit of using the HTRC Feature Reader is performance: reading the
json structures and parsing them is generally faster than custom code.
You also get convenient access to common information, such as
case-folded token counts or part-of-page specific character counts.
Details of the public methods provided by this library can be found in
the `HTRC Feature Reader
docs <http://htrc.github.io/htrc-feature-reader/htrc_features/feature_reader.m.html>`__.

**Table of Contents**: `Installation <#Installation>`__ \|
`Usage <#Usage>`__ \| `Additional Notes <#Additional-Notes>`__

**Links**: `HTRC Feature Reader
Documentation <http://htrc.github.io/htrc-feature-reader/htrc_features/feature_reader.m.html>`__
\| `HTRC Extracted Features
Dataset <https://sharc.hathitrust.org/features>`__

**Citation**: Peter Organisciak and Boris Capitanu, "Text Mining in
Python through the HTRC Feature Reader," *Programming Historian*, (22
November 2016),
http://programminghistorian.org/lessons/text-mining-with-extracted-features.

Installation
------------

To install,

.. code:: bash

        pip install htrc-feature-reader

That's it! This library is written for Python 2.7 and 3.0+. For Python
beginners, you'll need
`pip <https://pip.pypa.io/en/stable/installing/>`__.

Alternately, if you are using
`Anaconda <https://www.continuum.io/downloads>`__, you can install with

.. code:: bash

        conda install -c htrc htrc-feature-reader

The ``conda`` approach is recommended, because it makes sure that some
of the hard-to-install dependencies are properly installed.

Given the nature of data analysis, using iPython with Jupyter notebooks
for preparing your scripts interactively is a recommended convenience.
Most basically, it can be installed with
``pip install ipython[notebook]`` and run with ``ipython notebook`` from
the command line, which starts a session that you can access through
your browser. If this doesn't work, consult the `iPython
documentation <http://ipython.readthedocs.org/>`__.

Optional: `installing the development
version <#Installing-the-development-version>`__.

.. |Build Status| image:: https://travis-ci.org/htrc/htrc-feature-reader.svg?branch=master
   :target: https://travis-ci.org/htrc/htrc-feature-reader
.. |PyPI version| image:: https://badge.fury.io/py/htrc-feature-reader.svg
   :target: https://badge.fury.io/py/htrc-feature-reader
.. |Anaconda-Server Badge| image:: https://anaconda.org/htrc/htrc-feature-reader/badges/installer/conda.svg
   :target: https://anaconda.org/htrc/htrc-feature-reader

Usage
-----

*Note: for new Python users, a more in-depth lesson is published by
Programming Historian: `Text Mining in Python through the HTRC Feature
Reader <http://programminghistorian.org/lessons/text-mining-with-extracted-features>`__.
That lesson is also the official citation associated the HTRC Feature
Reader library.*

Reading feature files
~~~~~~~~~~~~~~~~~~~~~

The easiest way to start using this library is to use the
`FeatureReader <http://htrc.github.io/htrc-feature-reader/htrc_features/feature_reader.m.html#htrc_features.feature_reader.FeatureReader>`__
interface, which takes a list to Extracted Features files.

.. code:: python

    import glob
    import pandas as pd
    from htrc_features import FeatureReader
    paths = glob.glob('data/PZ-volumes/*.json.bz2')
    # Here we're loading five paths, for brevity
    fr = FeatureReader(paths[:5])
    for vol in fr.volumes():
        print("%s - %s" % (vol.id, vol.title))


.. parsed-literal::

    hvd.32044010273894 - The ballet dancer, and On guard,
    hvd.hwquxe - The man from Glengarry : a tale of the Ottawa / by Ralph Connor.
    hvd.hwrevu - The lady with the dog, and other stories,
    hvd.hwrqs8 - Mr. Rutherford's children. By the authors of "The wide, wide world," "Queechy,", "Dollars and cents," etc., etc.
    mdp.39015028036104 - Russian short stories, ed. for school use,


Iterating on ``FeatureReader`` returns ``Volume`` objects. This is
simply an easy way to access ``feature_reader.volumes()``. Wherever
possible, this library tries not to hold things in memory, so most of
the time you want to iterate rather than casting to a list. In addition
to memory issues, since each volume needs to be read from a file and
initialized, it will be slow. *Woe to whomever tries
``list(FeatureReader.volumes())``*.

The method for creating a path list with 'glob' is just one way to do
so. For large sets, it's better to just have a text file of your paths,
and read it line by line.

In addition to iterating on ``feature_reader.volumes()``, there is a
convenient function to grab the first volume in a feature reader. This
helps in testing code, and is what we'll do to continue this
introduction:

.. code:: python

    vol = fr.first()
    vol




.. parsed-literal::

    <htrc_features.feature_reader.Volume at 0x24d7b8b7390>



Online downloading by volume id (new in v.1.90)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FeatureReader can also download files at read time, by reference to
a HathiTrust volume id. For example, if I want `both of volumes of Pride
and Prejudice <https://catalog.hathitrust.org/Record/100323335>`__, I
can see that the URLs are
babel.hathitrust.org/cgi/pt?id=\ **hvd.32044013656053** and
babel.hathitrust.org/cgi/pt?id=\ **hvd.32044013656061**. In the
FeatureReader, these can be called with the ``ids=[]`` argument, as
follows:

.. code:: python

    fr = FeatureReader(ids=["hvd.32044013656053", "hvd.32044013656061"])
    
    for vol in fr:
        print(vol.title)


.. parsed-literal::

    Pride and prejudice.
    Pride and prejudice.


This downloads the file temporarily, using the HTRC's web-based download
link (e.g.
https://data.analytics.hathitrust.org/features/get?download-id={{URL}}).
One good pairing with this feature is the `HTRC Python
SDK <https://github.com/htrc/HTRC-PythonSDK>`__'s functionality for
downloading collections.

For example, I have a small collection of knitting-related books at
https://babel.hathitrust.org/cgi/mb?a=listis&c=1174943610. To read the
feature files for those books:

.. code:: python

    from htrc import workset
    volids = workset.load_hathitrust_collection('https://babel.hathitrust.org/cgi/mb?a=listis&c=1174943610')
    FeatureReader(ids=volids).first().title




.. parsed-literal::

    'A good yarn / Debbie Macomber.'



Remember that for large jobs, it is faster to download your dataset
beforehand, using the ``rsync`` method.

Volume
~~~~~~

A
`Volume <http://htrc.github.io/htrc-feature-reader/htrc_features/feature_reader.m.html#htrc_features.feature_reader.Volume>`__
contains information about the current work and access to the pages of
the work. All the metadata fields from the HTRC JSON file are accessible
as properties of the volume object, including *title*, *language*,
*imprint*, *oclc*, *pubDate*, and *genre*. The main identifier *id* and
*pageCount* are also accessible, and you can find the URL for the Full
View of the text in the HathiTrust Digital Library - if it exists - with
``vol.handle_url``.

.. code:: python

    "Volume %s is a %s page text written in %s. You can doublecheck at %s" % (vol.id, vol.page_count,
                                                                              vol.language, vol.handle_url)




.. parsed-literal::

    'Volume hvd.32044010273894 is a 284 page text written in eng. You can doublecheck at http://hdl.handle.net/2027/hvd.32044010273894'



As a convenience, ``Volume.year`` returns ``Volume.pub_date``:

.. code:: python

    "%s == %s" % (vol.pub_date, vol.year)




.. parsed-literal::

    '1901 == 1901'



``Volume`` objects have an page genrator method for pages, through
``Volume.pages()``. Iterating through pages using this generator only
keeps one page at a time in memory, and again it is preferable to
reading all the pages into the list at once. Unlike volumes, your
computer can probably hold all the pages of a single volume in memory,
so it is not dire if you try to read them into a list.

Like with the ``FeatureReader``, you can also access the page generator
by iterating directly on the object (i.e. ``for page in vol``). Python
beginners may find that using ``vol.pages()`` is more clear as to what
is happening.

.. code:: python

    # Let's skip ahead some pages
    i = 0
    for page in vol:
        # Same as `for page in vol.pages()`
        i += 1
        if i >= 16:
            break
    print(page)


.. parsed-literal::

    <page 00000016 of volume hvd.32044010273894>


If you want to pass arguments to page initialization, such as changing
the page's default section from 'body' to 'group' (which returns
header+footer+body), it can be done with
``for page in vol.pages(default_section='group')``.

Finally, if the minimal metadata included with the extracted feature
files is insufficient, you can fetch HT's metadata record from the Bib
API with ``vol.metadata``. Remember that this calls the HTRC servers for
each volume, so can add considerable overhead. The result is a MARC
file, returns as a `pymarc <https://github.com/edsu/pymarc>`__ record
object. For example, to get the publisher information from field
``260``:

.. code:: python

    for vol in fr.volumes():
        print(vol.metadata['260'].value())


::


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-7-8bc5f5c0f945> in <module>()
          1 for vol in fr.volumes():
    ----> 2     print(vol.metadata['published'][0])
    

    KeyError: 'published'


.. code:: python

    print("METADATA FIELDS: " + ", ".join(vol.metadata.keys()))


.. parsed-literal::

    METADATA FIELDS: _version_, htrc_charCount, title, htrc_volumePageCountBin, publishDate, title_a, mainauthor, author_only, oclc, authorSort, country_of_pub, author, htrc_gender, language, ht_id, publisher, author_top, publishDateRange, htrc_pageCount, title_top, callnosort, publication_place, topic, htsource, htrc_wordCount, title_ab, callnumber, fullrecord, htrc_volumeWordCountBin, format, lccn, genre, htrc_genderMale, topic_subject, topicStr, geographic, published, sdrnum, id


*At large-scales, using ``vol.metadata`` is an impolite and inefficient
amount of server pinging; there are better ways to query the API than
one volume at a time. Read about the `HTRC Solr
Proxy <https://wiki.htrc.illinois.edu/display/COM/Solr+Proxy+API+User+Guide>`__.*

Another source of bibliographic metadata is the HathiTrust Bib API. You
can access this information through the URL returned with
``vol.ht_bib_url``:

.. code:: python

    vol.ht_bib_url




.. parsed-literal::

    'http://catalog.hathitrust.org/api/volumes/full/htid/mdp.39015028036104.json'



Volumes also have direct access to volume-wide info of features stored
in pages. For example, you can get a list of words per page through
`Volume.tokens\_per\_page() <http://htrc.github.io/htrc-feature-reader/htrc_features/feature_reader.m.html#htrc_features.feature_reader.Volume.tokens_per_page>`__.
We'll discuss these features `below <#Volume-stats-collecting>`__, after
looking first at Pages.

Pages
-----

A page contains the meat of the HTRC's extracted features, including
information for:

-  Part of speech tagged token counts, through ``Page.tokenlist()``
-  Counts of the characters occurred at the start and end of physical
   lines, though ``Page.lineCounts()``
-  Sentence counts, line counts (referring to the physical line on the
   page)
-  And more, seen in the docs for
   `Page <http://htrc.github.io/htrc-feature-reader/htrc_features/feature_reader.m.html#htrc_features.feature_reader.Page>`__

.. code:: python

    print("The body has %s lines, %s empty lines, and %s sentences" % (page.line_count(),
                                                                       page.empty_line_count(),
                                                                       page.sentence_count()))


.. parsed-literal::

    The body has 30 lines, 0 empty lines, and 9 sentences


Since the HTRC provides information by header/body/footer, most methods
take a ``section=`` argument. If not specified, this defaults to
``"body"``, or whatever argument is supplied to
``Page.default_section``.

.. code:: python

    print("%s tokens in the default section, %s" % (page.token_count(), page.default_section))
    print("%s tokens in the header" % (page.token_count(section='header')))
    print("%s tokens in the footer" % (page.token_count(section='footer')))


.. parsed-literal::

    294 tokens in the default section, body
    3 tokens in the header
    0 tokens in the footer


There are also two special arguments that can be given to ``section``:
``"all"`` and "``group``". 'all' returns information for each section
separately, when appropriate, while 'group' returns information for all
header, body, and footer combined.

.. code:: python

    print("%s tokens on the full page" % (page.token_count(section='group')))
    assert(page.token_count(section='group') == (page.token_count(section='header') +
                                                 page.token_count(section='body') + 
                                                 page.token_count(section='footer')))


.. parsed-literal::

    297 tokens on the full page


Note that for the most part, the properties of the ``Page`` and
``Volume`` objects aligns with the names in the HTRC Extracted Features
schema, except they are converted to follow `Python naming
conventions <https://google.github.io/styleguide/pyguide.html?showone=Naming#Naming>`__:
converting the ``CamelCase`` of the schema to
``lowercase_with_underscores``. E.g. ``beginLineChars`` from the HTRC
data is accessible as ``Page.begin_line_chars``.

The fun stuff: playing with token counts and character counts
-------------------------------------------------------------

Token counts are returned by ``Page.tokenlist()``. By default,
part-of-speech tagged, case-sensitive counts are returned for the body.

The token count information is returned as a DataFrame with a MultiIndex
(page, section, token, and part of speech) and one column (count).

.. code:: python

    print(page.tokenlist()[:3])


.. parsed-literal::

                               count
    page section token    pos       
    16   body    !        .        1
                 '        ''       1
                 'Flowers NNS      1


``Page.tokenlist()`` can be manipulated in various ways. You can
case-fold, for example:

.. code:: python

    df = page.tokenlist(case=False)
    print(df[15:18])


.. parsed-literal::

                                count
    page section lowercase pos       
    16   body    ancient   JJ       1
                 and       CC      12
                 any       DT       1


Or, you can combine part of speech counts into a single integer.

.. code:: python

    df = page.tokenlist(pos=False)
    print(df[15:18])


.. parsed-literal::

                           count
    page section token          
    16   body    Naples        1
                 November      1
                 October       1


Section arguments are valid here: 'header', 'body', 'footer', 'all', and
'group'

.. code:: python

    df = page.tokenlist(section="header", case=False, pos=False)
    print(df)


.. parsed-literal::

                            count
    page section lowercase       
    16   header  ballet         1
                 dancer         1
                 the            1


The MultiIndex makes it easy to slice the results, and it is althogether
more memory-efficient. If you are new to Pandas DataFrames, you might
find it easier to learn by converting the index to columns.

.. code:: python

    df = page.tokenlist()
    # Slicing on Multiindex: get all Signular or Mass Nouns (NN)
    idx = pd.IndexSlice
    nouns = df.loc[idx[:,:,:,'NN'],]
    print(nouns[:3])
    print("With index reset: ")
    print(nouns.reset_index()[:2])


.. parsed-literal::

                                   count
    page section token        pos       
    16   body    benefactress NN       1
                 bitterness   NN       1
                 case         NN       1
    With index reset: 
       page section         token pos  count
    0    16    body  benefactress  NN      1
    1    16    body    bitterness  NN      1


If you prefer not to use Pandas, you can always convert the object, with
methods like ``to_dict`` and ``to_csv``).

.. code:: python

    df[:3].to_dict()




.. parsed-literal::

    {'count': {(16, 'body', '!', '.'): 1,
      (16, 'body', "'", "''"): 1,
      (16, 'body', "'Flowers", 'NNS'): 1}}



To get just the unique tokens, ``Page.tokens`` provides them as a list.

.. code:: python

    page.tokens()[:7]




.. parsed-literal::

    ['!', "'", "'Flowers", "'s", ',', '.', '6']



In addition to token lists, you can also access
``Page.begin_line_chars`` and ``Section.end_line_chars``, which are
DataFrames of character counts that occur at the start or end of a line.

Volume stats collecting
~~~~~~~~~~~~~~~~~~~~~~~

The Volume object has a number of methods for collecting information
from all its pages.

``Volume.tokenlist()`` works identically the page tokenlist method,
except it returns information for the full volume:

.. code:: python

    # Print case-insensitive occurrances of the word `she`
    all_vol_token_counts = vol.tokenlist(pos=False, case=False)
    print(all_vol_token_counts.loc[idx[:,'body', 'she'],][:3])


.. parsed-literal::

                            count
    page section lowercase       
    38   body    she            1
    39   body    she            1
    42   body    she            1


Note that a Volume-wide tokenlist is not crunched until you need it,
then it will stay cached in case you need it. If you try to access
``Page.tokenlist()`` *after* accessing ``Volume.tokenlist()``, the Page
object will return that page from the Volume's cached representation,
rather than preparing it itself.

``Volume.tokens()``, and ``Volume.tokens_per_page()`` give easy access
to the full vocabulary of the volume, and the token counts per page.

.. code:: python

    vol.tokens()[:10]




.. parsed-literal::

    ['"', '.', ':', 'Fred', 'Newton', 'Scott', 'gift', 'i', 'ii', 'iiiiISI']



If you prefer a DataFrame structured like a term-document matrix (where
pages are the 'documents'), ``vol.term_page_freqs()`` will return it.

By default, this returns a page-frequency rather than term-frequency,
which is to say it counts ``1`` when a term occurs on a page, regardless
of how much it occurs on that page. For a term frequency, pass
``page_freq=False``.

.. code:: python

    a = vol.term_page_freqs()
    print(a.loc[10:11,['the','and','is','he', 'she']])
    a = vol.term_page_freqs(page_freq=False)
    print(a.loc[10:11,['the','and','is', 'he', 'she']])


.. parsed-literal::

    token  the  and   is   he  she
    page                          
    10     0.0  1.0  0.0  0.0  0.0
    11     1.0  1.0  1.0  0.0  0.0
    token   the  and   is   he  she
    page                           
    10      0.0  1.0  0.0  0.0  0.0
    11     22.0  7.0  4.0  0.0  0.0


.. code:: python

    data/da

Volume.term\_page\_freqs provides a wide DataFrame resembling a matrix,
where terms are listed as columns, pages are listed as rows, and the
values correspond to the term frequency (or page page frequency with
``page_freq=true``). Volume.term\_volume\_freqs() simply sums these.

Multiprocessing
~~~~~~~~~~~~~~~

For large jobs, you'll want to use multiprocessing or multithreading to
speed up your process. This is left up to your preferred method, either
within Python or by spawning multiple scripts from the command line.
Here are two approaches that I like.

Dask
^^^^

Dask offers easy multithreading (shared resources) and multiprocessing
(separate processes) in Python, and is particularly convenient because
it includes a subset of Pandas DataFrames.

Here is a minimal example, that lazily loads token frequencies from a
list of volume IDs, and counts them up by part of speech tag.

.. code:: python

    import dask.dataframe as dd
    from dask import delayed

    def get_tokenlist(vol):
        ''' Load a one volume feature reader, get that volume, and return its tokenlist '''
        return FeatureReader(ids=[volid]).first().tokenlist()

    delayed_dfs = [delayed(get_tokenlist)(volid) for volid in volids]

    # Create a dask
    ddf = (dd.from_delayed(delayed_dfs)
             .reset_index()
             .groupby('pos')[['count']]
             .sum()
          )

    # Run processing
    ddf.compute()

Here is an example of 78 volumes being processed in 24 seconds with 31
threads:

.. figure:: data/dask-progress.png
   :alt: Counting POS in 78 books about knitting

   Counting POS in 78 books about knitting

This example used multithreading. Due to the nature of Python, certain
functions won't parallelize well. In our case, the part where the JSON
is read from the file and converted to a DataFrame (the light green
parts of the graphic) won't speed up because Python dicts lock the
Global Interpreter Lock (GIL). However, because Pandas releases the GIL,
nearly everything you do after parsing the JSON will be very quick.

To better understand what happens when ``ddf.compute()``, here is a
graph for 4 volumes:

.. figure:: data/dask-graph.png
   :alt: 

GNU Parallel
^^^^^^^^^^^^

As an alternative to multiprocessing in Python, my preference is to have
simpler Python scripts and to use GNU Parallel on the command line. To
do this, you can set up your Python script to take variable length
arguments of feature file paths, and to print to stdout.

This psuedo-code shows how that you'd use parallel, where the number of
parallel processes is 90% the number of cores, and 50 paths are sent to
the script at a time (if you send too little at a time, the
initialization time of the script can add up).

.. code:: bash

    find feature-files/ -name '*json.bz2' | parallel --eta --jobs 90% -n 50 python your_script.py >output.txt

Additional Notes
----------------

Installing the development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    git clone https://github.com/htrc/htrc-feature-reader.git
    cd htrc-feature-reader
    python setup.py install

Iterating through the JSON files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to do fast, highly customized processing without
instantiating Volumes, FeatureReader has a convenient generator for
getting the raw JSON as a Python dict: ``fr.jsons()``. This simply does
the file reading, optional decompression, and JSON parsing.

Downloading files within the library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``utils`` includes an Rsyncing utility, ``download_file``. This requires
Rsync to be installed on your system.

**Usage:**

Download one file to the current directory:

::

    utils.download_file(htids='nyp.33433042068894')

Download multiple files to the current directory:

::

    ids = ['nyp.33433042068894', 'nyp.33433074943592', 'nyp.33433074943600']
    utils.download_file(htids=ids)

Download file to ``/tmp``:

::

    utils.download_file(htids='nyp.33433042068894', outdir='/tmp')

Download file to current directory, keeping pairtree directory
structure, i.e.
``./nyp/pairtree_root/33/43/30/42/06/88/94/33433042068894/nyp.33433042068894.json.bz2``:

``utils.download_file(htids='nyp.33433042068894', keep_dirs=True)``

Getting the Rsync URL
~~~~~~~~~~~~~~~~~~~~~

If you have a HathiTrust Volume ID and want to be able to download the
features for a specific book, ``hrtc_features.utils`` contains an
`id\_to\_rsync <http://htrc.github.io/htrc-feature-reader/htrc_features/utils.m.html#htrc_features.utils.id_to_rsync>`__
function. This uses the `pairtree <http://pythonhosted.org/Pairtree/>`__
library but has a fallback written with that library is not installed,
since it isn't compatible with Python 3.

.. code:: python

    from htrc_features import utils
    utils.id_to_rsync('miun.adx6300.0001.001')




.. parsed-literal::

    'miun/pairtree_root/ad/x6/30/0,/00/01/,0/01/adx6300,0001,001/miun.adx6300,0001,001.json.bz2'



See the `ID to Rsync notebook <examples/ID_to_Rsync_Link.ipynb>`__ for
more information on this format and on Rsyncing lists of urls.

There is also a command line utility installed with the HTRC Feature
Reader:

.. code:: bash

    $ htid2rsync miun.adx6300.0001.001
    miun/pairtree_root/ad/x6/30/0,/00/01/,0/01/adx6300,0001,001/miun.adx6300,0001,001.json.bz2

Advanced Features
~~~~~~~~~~~~~~~~~

In the beta Extracted Features release, schema 2.0, a few features were
separated out to an advanced files. However, *this designation is no
longer present starting with schema 3.0*, meaning information like
``beginLineChars``, ``endLineChars``, and ``capAlphaSeq`` are always
available:

.. code:: python

    # What is the longest sequence of capital letter on each page?
    vol.cap_alpha_seqs()[:10]




.. parsed-literal::

    [0, 1, 0, 0, 0, 0, 0, 0, 4, 1]



.. code:: python

    end_line_chars = vol.end_line_chars()
    print(end_line_chars.head())


.. parsed-literal::

                             count
    page section place char       
    2    body    end   -         1
                       :         1
                       I         1
                       f         1
                       t         1


.. code:: python

    # Find pages that have lines ending with "!"
    idx = pd.IndexSlice
    print(end_line_chars.loc[idx[:,:,:,'!'],].head())


.. parsed-literal::

                             count
    page section place char       
    45   body    end   !         1
    75   body    end   !         1
    77   body    end   !         1
    91   body    end   !         1
    92   body    end   !         1


Testing
~~~~~~~

This library is meant to be compatible with Python 3.2+ and Python 2.7+.
Tests are written for py.test and can be run with ``setup.py test``, or
directly with ``python -m py.test -v``.

If you find a bug, leave an issue on the issue tracker, or contact Peter
Organisciak at ``organisciak+htrc@gmail.com``.
