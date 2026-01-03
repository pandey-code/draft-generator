from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# 🔐 SET YOUR API KEY HERE
openai.api_key = "PASTE_YOUR_API_KEY_HERE"

def ai_generate_draft(issue, draft_type):
    prompt = f"""
You are a professional chartered accountant and business consultant.

Convert the following issue into a well-written {draft_type}:

Issue:
{issue}

Make it clear, professional, and concise.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You write professional business drafts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    draft = ""
    if request.method == "POST":
        issue = request.form["user_text"]
        draft_type = request.form["draft_type"]

        if draft_type == "email":
            label = "professional email"
        elif draft_type == "audit":
            label = "audit note"
        else:
            label = "WhatsApp message"

        draft = ai_generate_draft(issue, label)

    return render_template("index.html", draft=draft)

if __name__ == "__main__":
    app.run(debug=True)
