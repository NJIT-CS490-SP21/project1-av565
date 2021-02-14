import os
from flask import Flask, render_template
import project1

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route('/')
def main():
    song = project1.project1_main()
    return render_template(
        "index.html",
        song=song
    )


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 8080)), debug=True)
