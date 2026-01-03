from flask import Flask, render_template, request

app = Flask(__name__)

def generate_draft(issue, draft_type):
    issue = issue.strip()

    if draft_type == "email":
        return f"""Subject: Clarification required regarding the matter

Dear Sir/Madam,

This is with reference to the following matter:

"{issue}"

Based on our review, the same requires clarification and confirmation from your end. Kindly provide the necessary explanation along with supporting details, if any.

Please feel free to reach out in case of any questions.

Regards,
"""
    elif draft_type == "audit":
        return f"""Audit Note:

Issue Identified:
{issue}

Observation:
During the course of audit, the above matter was noted and requires management clarification.

Action Required:
Management to review the matter and provide reconciliation / justification along with supporting documents.
"""
    else:  # WhatsApp
        return f"""Hello,

Regarding the following issue:

{issue}

Kindly review and confirm at the earliest. Please share clarification and supporting details.

Thanks."""

@app.route("/", methods=["GET", "POST"])
def index():
    draft = ""
    if request.method == "POST":
        issue = request.form["user_text"]
        draft_type = request.form["draft_type"]
        draft = generate_draft(issue, draft_type)

    return render_template("index.html", draft=draft)

if __name__ == "__main__":
    app.run(debug=True)
