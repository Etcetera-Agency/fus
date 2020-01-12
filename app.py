from notion.client import NotionClient
from notion.block import *
from notion.collection import NotionDate
from flask import Flask
from flask import request
import pytz
import datetime

timezone = "Europe/Kiev"

app = Flask(__name__)



def create_recruit(token, collection_url, name, upw_link, title, description, country, rate, pf_items, skills, since):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collection_url)
    row = cv.collection.add_row()
    row.name = name
    row.upwork = upw_link
    row.description = description
    row.title = title
    row.country = country
    row.rate = rate
    row.portfolio_items = pf_items
    row.member_since = NotionDate(since, timezone=timezone).to_notion()
    row.skills = skills
    

@app.route('/recruit', methods=['POST'])
def recruit():
    collection_url = request.form.get("collectionURL")
    name = request.form.get('name')
    token_v2 = os.environ.get("TOKEN")
    upw_link = request.form.get('upw_link')
    title = request.form.get('title')
    country = request.form.get('country')
    rate = request.form.get('rate', type = int)
    pf_items = request.form.get('pf_items', type = int)
    skills = request.form.get('skills')
    since = request.form.get('since')
    description = request.form.get('description')
    create_recruit(token_v2, collection_url, name, upw_link, title, description, country, rate, pf_items, skills, since)
    return f'added {name} recruit to Notion'

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
