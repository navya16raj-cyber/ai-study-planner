print("Enter Student Details")

name = input("Name: ")
college = input("College: ")
branch = input("Branch: ")
year = input("Graduation Year: ")
email = input("Email: ")

n = int(input("\nEnter number of subjects: "))
subjects = []

for i in range(n):
    sub = input(f"Subject {i+1} name: ")
    credits = int(input("Credits: "))
    subjects.append({"name": sub, "credits": credits})

weekday_hours = int(input("\nWeekday study hours: "))
weekend_hours = int(input("Weekend study hours: "))
preferred_time = input("Preferred study time: ")

for sub in subjects:
    print(f"\nFor {sub['name']}:")
    sub["strong"] = input("Strong areas: ")
    sub["weak"] = input("Weak areas: ")
    sub["confidence"] = int(input("Confidence (1-5): "))

total_weight = 0
for sub in subjects:
    sub["weight"] = sub["credits"] + (5 - sub["confidence"])
    total_weight += sub["weight"]

print("\n--- PERSONALIZED STUDY PLAN ---")
for sub in subjects:
    time = (sub["weight"] / total_weight) * weekday_hours
    print(f"{sub['name']} → {round(time,2)} hrs/day")

print("\n--- NEXT 7 DAYS FOCUS ---")
for sub in subjects:
    print(f"Work on {sub['weak']} in {sub['name']}")

print("\n--- SUMMARY ---")
print("Completion: On track")
print("Confidence will improve")
print("Stress before exam will reduce")
