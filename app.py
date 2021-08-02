from flask import Flask, render_template
import datetime
from time import strftime

app = Flask(__name__)

@app.route("/")
def index():
    
    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Set the current time
    today = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Write the current time
    ##f = open("datetime.txt", "w")
    ##f.write(str(today))
    ##f.close()

    # Render HTML with count variable
    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run()