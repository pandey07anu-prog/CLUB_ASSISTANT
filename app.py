from flask import Flask, request, jsonify, render_template
import pandas as pd
import csv

app = Flask(__name__)

# ---------------- HOME ROUTES ----------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sports.html')
def sports():
    return render_template('sports.html')

@app.route('/coding.html')
def coding():
    return render_template('coding.html')

@app.route('/art.html')
def art():
    return render_template('art.html')

@app.route('/music.html')
def music():
    return render_template('music.html')


# ---------------- RECOMMENDATION API ----------------
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json()

        # Save user selection for tracking
        with open('students_data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Category", "Interest", "TournamentInterest"])
            writer.writerow([
                data.get('category'),
                data.get('interest'),
                data.get('tournamentInterest')
            ])

        category = data.get('category', '').strip().upper()
        interest = data.get('interest', '').strip()
        tournament_interest = data.get('tournamentInterest', '').strip().lower()

        df = pd.read_csv('data.csv')
        df.columns = [c.strip().capitalize() for c in df.columns]

        # Filter category
        filtered_df = df[df['Category'].str.upper() == category]

        # Filter interest
        if interest:
            filtered_df = filtered_df[filtered_df['Activity'].str.contains(
                interest, case=False, na=False)]

        # Filter tournament interest
        if tournament_interest in ["yes", "no"]:
            filtered_df = filtered_df[filtered_df['Interested'].str.lower()
                                      == tournament_interest]

        filtered_data = filtered_df.to_dict(orient='records')

        return jsonify({"clubs": filtered_data})

    except Exception as e:
        print("❌ Error in /recommend:", e)
        return jsonify({"error": str(e)}), 500


# ---------------- SAVE FORM DATA ----------------
@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()

        with open('student_form_data.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Name", "Age", "Year", "Stream", "Interest"])
            writer.writerow([
                data.get('name', ''),
                data.get('age', ''),
                data.get('year', ''),
                data.get('stream', ''),
                data.get('interest', '')
            ])

        return jsonify({"message": "Form data saved successfully!"})

    except Exception as e:
        print("❌ Error in /submit_form:", e)
        return jsonify({"error": str(e)}), 500


# ---------------- JOIN CLUB FORM ----------------
@app.route('/join_club', methods=['POST'])
def join_club():
    try:
        data = request.get_json()

        with open('joined_clubs.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Name", "Email", "ClubName", "Category", "Activity"])
            writer.writerow([
                data.get('name', ''),
                data.get('email', ''),
                data.get('clubName', ''),
                data.get('category', ''),
                data.get('activity', '')
            ])

        return jsonify({"message": "Join form data saved successfully!"})

    except Exception as e:
        print("❌ Error in /join_club:", e)
        return jsonify({"error": str(e)}), 500


# ---------------- VIEW JOINED CLUBS ----------------
@app.route('/view_joined_clubs')
def view_joined_clubs():
    try:
        df = pd.read_csv('joined_clubs.csv')
        data = df.to_dict(orient='records')
        return render_template("view_joined.html", data=data)
    except:
        return "<h2>No joined club data found.</h2>"


# ---------------- CHATBOT ----------------
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_msg = request.json.get("message", "").lower().strip()

        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.upper()

        corrections = {
            "cooding": "coding",
            "codding": "coding",
            "spor": "sports",
            "aart": "art",
            "musc": "music"
        }
        for wrong, correct in corrections.items():
            if wrong in user_msg:
                user_msg = user_msg.replace(wrong, correct)

        allowed_categories = ["coding", "sports", "music", "art"]
        detected_category = None

        for cat in allowed_categories:
            if cat in user_msg:
                detected_category = cat.upper()
                break

        if not detected_category:
            return jsonify({"reply": "❌ Please select from: Coding, Sports, Music, Art"})

        matches = df[df["CATEGORY"] == detected_category]

        if matches.empty:
            return jsonify({"reply": "❌ No matching clubs found."})

        # Remove duplicate ACTIVITY rows
        unique_rows = matches.drop_duplicates(subset=["ACTIVITY"])

        reply = f"🟦 Category: {detected_category} \n\n"
        reply += "🟩 Available Clubs: \n\n"
        reply += " ━━━━━━━━━━━━━━━━━━━━━━\n"

        for _, row in unique_rows.iterrows():
            reply += (
                f"📌 Activity: {row['ACTIVITY']}\n"
                f"➡️ Details: {row['DETAILS']}\n"
                f" ━━━━━━━━━━━━━━━━━━━━━━\n"
            )

        return jsonify({"reply": reply})

    except Exception as e:
        print("Chatbot Error:", e)
        return jsonify({"reply": "Server error occurred."}), 500


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
