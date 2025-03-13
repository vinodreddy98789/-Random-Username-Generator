
from flask import Flask, render_template, request
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

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
      include_number = 'include_number' in request.form
      include_special = 'include_special' in request.form
      custom_addition = request.form.get('custom_addition', '')
      num_usernames = int(request.form.get('num_usernames', 1))

      usernames = [generate_username(include_number, include_special, custom_addition) for _ in range(num_usernames)]
  else:
      usernames = []

  return render_template('index.html', usernames=usernames)

if __name__ == '__main__':
  app.run(debug=True)
