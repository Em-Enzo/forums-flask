from flask import Flask, render_template
import models, stores, dummy_data


app = Flask(__name__)


member_store = stores.MemberStore()
post_store = stores.PostStore()
dummy_data.seed_stores(member_store, post_store)
	
