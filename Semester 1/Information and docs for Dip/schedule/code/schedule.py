import pandas as pd

# Creating the data for the schedule
data = {
    "Time": [
        "6:00-7:00 AM", "7:00-7:30 AM", "7:30-8:30 AM", "8:30-9:30 AM",
        "9:00-10:00 AM", "10:00-11:00 AM", "11:00-12:00 PM", "12:00-1:00 PM",
        "1:00-2:00 PM", "2:00-3:00 PM", "3:00-4:00 PM", "4:00-5:00 PM",
        "5:00-6:00 PM", "6:00-7:00 PM", "7:00-8:00 PM", "8:00-9:00 PM",
        "9:00-10:00 PM", "10:00-11:00 PM", "11:00-12:00 AM"
    ],
    "Monday": [
        "-", "-", "-", "-",
        "Wake up, Breakfast", "Study", "Study", "Study",
        "Lunch/Study Break", "Study", "Study", "Study",
        "Dinner/Leisure", "Study", "Study", "Leisure",
        "Leisure", "Rest/Free Time", "Rest"
    ],
    "Tuesday": [
        "Travel to class", "Travel to class", "Class (8:30 AM-3:30 PM)", "Class",
        "Class", "Class", "Class", "Class",
        "Class", "Travel/Rest", "Study", "Study",
        "Dinner", "Study", "Study", "Leisure",
        "Leisure", "Rest/Free Time", "Rest"
    ],
    "Wednesday": [
        "Travel to class", "Travel to class", "Class (8:30 AM-5:30 PM)", "Class",
        "Class", "Class", "Class", "Class",
        "Class", "Travel/Rest", "Study/Rest", "Study/Rest",
        "Dinner", "Study", "Study", "Leisure",
        "Leisure", "Rest/Free Time", "Rest"
    ],
    "Thursday": [
        "-", "-", "-", "-",
        "Wake up, Breakfast", "Study", "Study", "Study",
        "Lunch/Study Break", "Study", "Study", "Study",
        "Dinner", "Work (2:00 PM-12:00 AM)", "Work", "Work",
        "Work", "Work", "Work"
    ],
    "Friday": [
        "-", "-", "-", "-",
        "Wake up, Breakfast", "Study", "Study", "Study",
        "Lunch/Study Break", "Study", "Study", "Study",
        "Dinner", "Work (2:00 PM-12:00 AM)", "Work", "Work",
        "Work", "Work", "Work"
    ],
    "Saturday": [
        "-", "-", "-", "-",
        "Wake up, Breakfast", "Workout", "Workout", "Workout",
        "Lunch/Leisure", "Study", "Study", "Study",
        "Dinner", "Work (2:00 PM-12:00 AM)", "Work", "Work",
        "Work", "Work", "Work"
    ],
    "Sunday": [
        "-", "-", "-", "-",
        "Wake up, Breakfast", "Leisure", "Leisure", "Leisure",
        "Leisure", "Leisure", "Leisure", "Leisure",
        "Dinner", "Leisure", "Leisure", "Leisure",
        "Leisure", "Rest", "Rest"
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Saving the DataFrame to an Excel file on your Desktop
df.to_excel(r"C:\Users\NickS\Documents\weekly_schedule.xlsx", index=False)
