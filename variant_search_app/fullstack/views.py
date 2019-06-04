from flask import render_template, Blueprint
from flask import request, send_from_directory
from zipfile import ZipFile
import pandas as pd

fullstack_blueprint = Blueprint("fullstack", __name__)
# unzipped_gene_file = ZipFile.extractall(path="/data/variants.tsv.zip", members=None, pwd=None)
# gene_file = pd.read_csv("variants.tsv", sep = "/t")

# INDEX TEMPLATE -  where search bar will be
@fullstack_blueprint.route("/<path:filename>")
def index(filename):
    print('@@ THIS IS SOMETHING')
    print(filename)
    return send_from_directory("./static", filename)

# SHOW ACTION TEMPLATE- where we send users after they hit submit
@fullstack_blueprint.route("/company_results")
def show():
    company_id = request.args.get("SAMPLE", type=str) # Pass in string as the argument name in get
    data = get_company_data(company_id)
    # ['google', 'amazon', 'facebook', 'netflix', 'apple', 'microsoft']
    return render_template('company_results.html', context=data)
