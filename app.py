from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

# Predefined lists of adjectives and nouns
adjectives = ["Kartik", "Sachin", "Happy", "Cool", "Brave", "Witty", "Loyal", "Chill", "Fierce", "Jolly", "Mighty", "Swift"]
nouns = ["Gali", "Hiremat", "Tiger", "Dragon", "Phoenix", "Panther", "Falcon", "Shark", "Wolf", "Eagle", "Bear", "Cobra"]

def generate_username(include_number=True, include_special=False, custom_addition=""):
    """Generates a random username with customization options."""
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun

    if include_number:
        username += str(random.randint(10, 999))  # Adds a random number between 10-999

    if include_special:
        username += random.choice(string.punctuation)  # Adds a random special character

    if custom_addition:
        username += custom_addition  # Adds user-defined custom characters

    return username

# HTML template as a string
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Username Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        h1 {
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
            text-align: left;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="number"],
        input[type="text"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="checkbox"] {
            margin-right: 5px;
        }
        .btn {
            background-color: #007bff;
            color: #fff;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 4px;
            width: 100%;
        }
        .btn:hover {
            background-color: #0056b3;
        }
        .username-list {
            margin-top: 20px;
            text-align: left;
        }
        .username-item {
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .copy-btn {
            background-color: #28a745;
            color: #fff;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
            border-radius: 4px;
        }
        .copy-btn:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 Random Username Generator 🎉</h1>
        <form method="post">
            <div class="form-group">
                <label for="num_usernames">Number of Usernames:</label>
                <input type="number" id="num_usernames" name="num_usernames" min="1" value="1" required>
            </div>
            <div class="form-group">
                <input type="checkbox" id="include_number" name="include_number" checked>
                <label for="include_number">Include Numbers</label>
            </div>
            <div class="form-group">
                <input type="checkbox" id="include_special" name="include_special">
                <label for="include_special">Include Special Characters</label>
            </div>
            <div class="form-group">
                <label for="custom_addition">Custom Addition:</label>
                <input type="text" id="custom_addition" name="custom_addition" placeholder="Enter custom text">
            </div>
            <button type="submit" class="btn">Generate Usernames</button>
        </form>
        {% if usernames %}
            <div class="username-list">
                <h3>Generated Usernames:</h3>
                <ul>
                    {% for username in usernames %}
                        <li class="username-item">
                            {{ username }}
                            <button class="copy-btn" onclick="copyToClipboard('{{ username }}')">Copy</button>
                        </li>
                    {% endfor %}
                </ul>
            </div>
        {% endif %}
    </div>

    <script>
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                alert('Copied to clipboard: ' + text);
            }, function(err) {
                console.error('Could not copy text: ', err);
            });
        }
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    usernames = []
    if request.method == 'POST':
        include_number = 'include_number' in request.form
        include_special = 'include_special' in request.form
        custom_addition = request.form.get('custom_addition', '')
        num_usernames = int(request.form.get('num_usernames', 1))

        usernames = [generate_username(include_number, include_special, custom_addition) for _ in range(num_usernames)]

    return render_template_string(html_template, usernames=usernames)

if __name__ == '__main__':
    app.run(debug=True)
