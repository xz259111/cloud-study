#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask, render_template, redirect, g, request, url_for, jsonify, json
import urllib
import requests  # similar purpose to urllib.request, just more convenience
import os

app = Flask(__name__)
TODO_API_URL = "http://34.83.175.183:5001"


@app.route("/")
def show_list():
    try:
        r = requests.get(TODO_API_URL)
        json_dict = json.loads(json.dumps(r.json()))
        return render_template('index.html', todolist = json_dict)
    except:
        raise ApiError('GET /items/ {}'.format(r.statue_code))
    return render_template('index.html', todolist=resp)

@app.route("/add", methods=['POST'])
def add_entry():
    requests.post(TODO_API_URL+"/api/items", json={
                  "what_to_do": request.form['what_to_do'], "due_date": request.form['due_date'],
                  "location":request.form['location],"invities":request.form['invities']})
    return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
    item = urllib.parse.quote(item)
    requests.delete(TODO_API_URL+"/api/items/"+item)
    return redirect(url_for('show_list'))


@app.route("/mark/<item>")
def mark_as_done(item):
    item = urllib.parse.quote(item)
    requests.put(TODO_API_URL+"/api/items/"+item)
    return redirect(url_for('show_list'))


if __name__ == "__main__":
    app.run("0.0.0.0",port = 5001)


# In[ ]:




