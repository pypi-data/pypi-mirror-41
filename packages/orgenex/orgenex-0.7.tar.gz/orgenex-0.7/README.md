

orgenex
=======

orgenex converts an Evernote export into an emacs org-mode document.


Installation
------------

[pandoc](https://pandoc.org/) is used to tranlate the note content
to the org-mode document. On Ubuntu, installing it is straightforward:

    apt-get install pandoc

and installing orgenex 

    pip install orgenex


Features
--------

A short list of features that it's capable of 

-   Tags are imported
-   All attachments are imported as attachments in the org document
-   Fast and memory efficient
    A 4GB export consisting of 3000 notes took less than three minutes
    to convert and used no more than 0.2% of memory.


Usage
-----

Assuming your export is named Evernote.enex the following command will
create the org-mode file `out.org`. Attachments are stored in the
`data/` directory relative to where you run the command.

    orgenex Evernote.enex > out.org

