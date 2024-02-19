from datetime import datetime

def calculate_age(birthdate, today):
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # Adjust for negative months and days
    if months < 0 or (months == 0 and days < 0):
        years -= 1
        if months < 0:
            months += 12
        if days < 0:
            temp_date = today.replace(year=today.year, month=today.month - 1)
            days += (today - temp_date).days
    return years, months, days

# Replace "Uptime" section with current age
def replace_uptime_with_age(readme_content, age):
    lines = readme_content.split('\n')
    new_lines = []

    for line in lines:
        if 'Uptime:' in line:
            new_lines.append(f'  Uptime: {age[0]} years, {age[1]} months, {age[2]} days')
        else:
            new_lines.append(line)

    return '\n'.join(new_lines)

# Read the README.md file
with open('README.md', 'r') as file:
    readme_content = file.read()

# Calculate age
birthdate = datetime(year=2004, month=9, day=21) 
today = datetime.today()
age = calculate_age(birthdate, today)

new_readme_content = replace_uptime_with_age(readme_content, age)

# Write the modified content back to README.md
with open('README.md', 'w') as file:
    file.write(new_readme_content)

print("Age section updated in README.md successfully!")
