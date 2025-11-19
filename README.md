

🚀 What is Club Assistant?

Finding a club that matches your vibe shouldn’t feel like searching for a needle in a haystack.
Club Assistant is here to fix that.
It’s a smart, interactive web system that recommends clubs based on your interests — and lets you join them with a single click. No confusion. No scrolling for hours. Just perfect matches.

💡 Why We Built This

Students often want to join clubs but struggle to choose the right one. Too many options, too much info, too much confusion.
So we built a system that:

✔ Understands the user
✔ Suggests the best clubs
✔ Simplifies joining
✔ Makes the whole process fun and smooth

🎯 Core Objectives

Build a clean, user-friendly interface

Collect user details & preferences easily

Recommend clubs based on interests

Enable one-click club joining

Increase student participation

🛠️ How We Built It

We divided the system into three simple modules:

🔹 1. Registration Module

Collects basic information like Name, Age, Academic Year, Stream, Interests.

🔹 2. Recommendation Engine

Suggests clubs using:

Keyword matching

Content filtering

Scoring logic

🔹 3. Club Joining Module

A single click → you’re officially part of the club.

The entire frontend is built using HTML + CSS, keeping everything neat, clean, and friendly.

🗂️ Database Design
Users Table

user_id

name

age

year

stream

interest

Clubs Table

club_id

club_name

category

description

User_Club Table

user_id

club_id

joined_date

This simple structure keeps everything organized and easy to manage.

🎨 UI / UX Design

We focused on:

✨ Minimal, modern layout
✨ Red highlight headings
✨ Card-style boxes
✨ Clean background
✨ Easy-to-read input fields
✨ Clear “Submit” & “Join Now” buttons

Figma Prototype:
🔗 https://www.figma.com/design/BPAKT3FfXGP8VoELwtmkqY/Untitled?node-id=0-1&p=f

🧪 Final Output / Result

We successfully built a working prototype where:

Students enter their academic details

Select their interests

Receive personalized club recommendations

Join any club instantly

The interface is simple.
The experience is smooth.
The participation becomes easy.

Our prototype proves how smart design + thoughtful planning can boost student involvement in clubs.

🔁 System Workflow
User Opens Form
        ↓
Enters Personal Information
        ↓
Selects Interests
        ↓
Recommendation Engine Matches Clubs
        ↓
User Views Suggested Clubs
        ↓
User Clicks “Join Now”
        ↓
Membership Stored in Database
