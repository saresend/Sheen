<h1> Sheen </h1>

<h3> A todo manager (because looking through the code manually was too hard) </h3>


<h2> Installation </h2>
<p> Just run the following command

<code> wget https://raw.githubusercontent.com/saresend/Sheen/master/sheen.py </code>

And then run the script with
<code> python3 sheen.py \<directoryName\> </code>

It will search through the directory (and its subdirectories), or a single file if specified, giving an output that looks something like this:
```
challenge/env/lib/python3.6/site-packages/numpy/lib/_datasource.py

        Line 48: TODO: .zip support, .tar support?
        Line 295: TODO: Doesn't handle compressed files!
        Line 371: TODO:  This should be more robust.  Handles case where path includes
        Line 483: TODO: There is no support for opening a file for writing which
        Line 486: TODO: Add a ``subdir`` parameter for specifying the subdirectory
challenge/env/lib/python3.6/site-packages/numpy/lib/stride_tricks.py
        Line 255: TODO: consider making the results of broadcast_arrays readonly to match
challenge/env/lib/python3.6/site-packages/numpy/lib/tests/test_io.py
        Line 285: TODO: specify exact message
challenge/env/lib/python3.6/site-packages/numpy/ma/tests/test_old_ma.py
        Line 625: TODO FIXME: Find out what the following raises a warning in r8247
```


