from flask import render_template, Blueprint
from flask import request
from zipfile import ZipFile
import pandas as pd

backend_blueprint = Blueprint("backend", __name__)
# unzipped_gene_file = ZipFile.extractall(path="/data/variants.tsv.zip", members=None, pwd=None)
gene_file = pd.read_csv("variants.tsv", sep = "/t")

# INDEX TEMPLATE -  where search bar will be
@backend_blueprint.route("/")
def index():
    return render_template('index.html')

# SHOW ACTION TEMPLATE- where we send users after they hit submit
@backend_blueprint.route("/company_results")
def show():
    company_id = request.args.get("SAMPLE", type=str) # Pass in string as the argument name in get
    data = get_company_data(company_id)
    # ['google', 'amazon', 'facebook', 'netflix', 'apple', 'microsoft']
    return render_template('company_results.html', context=data)
