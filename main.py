from flask import Flask
import json
import datetime
import os

app = Flask(__name__)

@app.route('/news.all.get')
def get_news_all_articles():
    data = []
    try:
        with open('news_data.json', 'r') as file:
            data = json.load(file)
        app.logger.debug('_________________Hello ' + str(data))
    except FileNotFoundError:
        app.logger.error('news_data.json not found')
        return json.dumps({'error': 'News data file not found'}), 404
    except json.JSONDecodeError:
        app.logger.error('Invalid JSON in news_data.json')
        return json.dumps({'error': 'Invalid news data format'}), 500
    
    return json.dumps(data)

@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return json.dumps(data)

@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
