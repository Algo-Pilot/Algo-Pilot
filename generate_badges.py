import os

data = {
    "USER ID": "1153590 ",
    "RANKING": "#233,780 📊",
    "POINTS": "1250 ✨",
    "STREAK": "9 DAYS 🔥",
    "SOLVED": "21"
}

colors = {
    "USER ID": "#2b83f6",
    "RANKING": "#3ba241",
    "POINTS": "#f1b501",
    "STREAK": "#f77f00",
    "SOLVED": "#9145e8"
}

os.makedirs("badges", exist_ok=True)

for label, value in data.items():
    filename = f"badges/{label.replace(' ', '_').lower()}.svg"
    color = colors[label]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="180" height="80">
  <rect rx="12" width="180" height="80" fill="{color}" />
  <text x="50%" y="35%" dominant-baseline="middle" text-anchor="middle" font-size="16" fill="#fff" font-family="Arial" font-weight="bold">{label}</text>
  <rect y="40" rx="12" width="180" height="40" fill="#fff" />
  <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" font-size="22" fill="#000" font-family="Arial" font-weight="bold">{value}</text>
</svg>"""

    with open(filename, "w") as f:
        f.write(svg)

print("✅ Badges updated!")
