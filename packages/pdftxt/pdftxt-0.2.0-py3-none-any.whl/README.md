### pdftxt

The goal of this project is to provide an api to extract text
from specific regions of a pdf document/page and a cli to assist
identifying the location of text within a document.

### Installation


    ... pip install pdftxt


### Basic Command Line Usage

Let's say we have a PDF file (PDF-DOC.pdf) that looks like this:

![Source File Image](https://bytebucket.org/mgemmill/pdftxt/raw/36ef6c80f953ac5d4eae712d5c7943c23e8914bc/assets/readme_src_doc_.jpg)

The `pdftxt` command:

    ... pdft PDF-DOC.pdf

Will output a visual layout of the pdf document's pages and text elements to an html page:

![Output File Image](https://bytebucket.org/mgemmill/pdftxt/raw/36ef6c80f953ac5d4eae712d5c7943c23e8914bc/assets/readme_output_doc_.jpg)


### Basic API Usage


    from pathlib import Path
    from pdftxt import api

    filepath = 'tests/Word_PDF.pdf'

    with api.PdfTxtContext(filepath) as pdf:

        for page in pdf:

            # To fetch text objects from specific region
            # of the page, first define the region:
            region = api.Region(400, 300, 512, 317)

            # Initialize layout parameters:
            params = api.PdfTxtParams()

            # Then analyze that area of the page for text objects:
            text = page.analyze(region, params)

            # Do whatever it is we need to do with the results:
            for txt in text:
                print(txt.text)
