from flask import render_template, Blueprint
from flask import request
from zipfile import ZipFile
import pandas as pd

backend_blueprint = Blueprint("backend", __name__)
# unzipped_gene_file = ZipFile.extractall(path="/data/variants.tsv.zip", members=None, pwd=None)
gene_file = pd.read_csv("/data/variants.tsv", sep = " ")

