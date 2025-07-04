from flask import Flask, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/gists"


@app.route('/<username>', methods=['GET'])
def get_gists(username):
    response = requests.get(GITHUB_API_URL.format(username))

    if response.status_code == 404:
        return jsonify({'error': 'User not found'}), 404
    elif response.status_code != 200:
        return jsonify({'error': f'GitHub API error: {response.status_code}'}), response.status_code

    try:
        gists = response.json()
        print(gists)
    except Exception:
        return jsonify({'error': 'Invalid JSON response from GitHub'}), 502

    gist_list = [{'id': g['id'], 'description': g['description'], 'url': g['html_url']} for g in gists]
    return jsonify(gist_list)


# Only run this if not being imported
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
