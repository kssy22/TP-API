from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('emojis_data.json') as f:
    emojis_data = json.load(f)

#Récupérer un emoji aléatoire
@app.route('/random')
def get_random_emoji():
    import random
    emoji = random.choice(emojis_data)
    return jsonify(emoji)

#Récupérer un emoji grâce à son nom
@app.route('/name/<string:emoji_name>')
def get_emoji_by_name(emoji_name):
    emoji = next((e for e in emojis_data if e['name'] == emoji_name), None)
    if emoji:
        return jsonify(emoji)
    else:
        return jsonify({'Emoji not found'}), 404

#Récupérer un emoji selon sa catégorie
@app.route('/category/<string:category_name>')
def get_emoji_by_category(category_name):
    emojis = [e for e in emojis_data if e['category'] == category_name]
    if emojis:
        return jsonify(emojis)
    else:
        return jsonify({'Category not found'}), 404

#Récupérer un emoji selon son groupe
@app.route('/group/<string:group_name>')
def get_emoji_by_group(group_name):
    emojis = [e for e in emojis_data if e['group'] == group_name]
    if emojis:
        return jsonify(emojis)
    else:
        return jsonify({'Group not found'}), 404
