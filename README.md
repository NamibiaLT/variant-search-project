# Variant Search Coding Assignment

## Assignment

Create a web application that allows a user to search for genomic variants by gene name and display the results in a tabular view.

## Features

1. Allow the user to enter a gene name to search for variants in that gene. Display the results in a table that shows various attributes associated with each genomic variant.

2. Provide an auto-suggest feature for entering the gene name.

3. Provide two RESTful endpoints supporting the functionality listed in steps 1 and 2.

## Datasource

A zipped TSV file of variants is available in /data/variants.tsv.zip. Each row in the TSV file represents a genomic variant and contains a Gene column with the gene name. A variant will belong to one and only one gene, but multiple variants may belong to the same gene.

## Implementation

If you are comfortable with Python and/or React, please use these technologies for your app. You may use any additional frameworks, languages, databases, libraries, etc. that you find appropriate.

Our expectation is you will be writing some server code, client code, and applying some basic styling to create a working web application. The application should include unit tests.

Here’s an example of how you might group and display the information:

![variants table example](./example_table.png)

## Submitting Your Solution

Please clone this repository and upload an archive to Greenhouse, or upload your repository to GitHub and send us a link. Update this README to include instructions on how to install, test, and run your application. Bonus: Deploy it and include the URL here.

As part of the review process, we may comment on or ask questions about specific parts of the code.

Please return your solution within 1 week. This is not an expectation of the time required to complete the assignment. Rather, it’s meant to provide buffer for busy schedules.

## Running the App:
1. OPTIONAL: create and activate a new virtual environment

    With Anaconda:

        conda create -n ve python=3.7
        conda activate ve

2. Install requirements. Some of the dependencies may not be accessible in the condo repo. You may use pip to install all libraries.

```
pip install -r requirements.txt
```

3. Run the FLASK application

    Change directory to `variant_search_project`. For debugging, you can add `export FLASK_DEBUG=1`

```
variant_search_project$ export FLASK_APP=server.py
variant_search_project$ flask run
