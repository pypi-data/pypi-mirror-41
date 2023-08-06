

pclean
======

pclean identifies and removes duplicate files within a pCloud account.

By using pCloud's API, pclean is able to determine duplicate files
without needing to download any files from the cloud, preserving your
pCloud bandwidth quota and making it pretty quick.


Setup
-----

Python 3.6 is required purely due to the use of the f-strings. All
other requirements can be installed via pip with

    pip install .

The application needs you to configure your pCloud username and
password which it will save in plain text to
`$HOME/.config/pclean.ini`:

    pclean auth <username> <password>


Examples
--------

To report all duplicate files from the directory `/copies` that can be
found in `/orig` you would run:

    pclean -n clean /orig /copies

The **-n** flag is effectively a dry run and will just report the
duplicates. By omitting *-n* the duplicates will also be removed.


About
-----

The software is provided as is and the author accepts no
responsibility for files lost due to bugs or misuse or anything else.

The source can be found here: <https://bitbucket.org/tipmethewink/pclean>

