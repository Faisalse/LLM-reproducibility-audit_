import matplotlib.pyplot as plt
from pathlib import Path


name_ver_para_plat = 14
name_ver_para = 25
name_para = 15
name_plat = 4
name_ver = 3
name = 4

values = [name_ver_para_plat, name_ver_para,  name_para, name_ver, name_plat , name]
categories = ['Name + Ver. + Para. + Plat.', 'Name + Ver. + Para.', 'Name + Para.', 'Name + Ver.', 'Name + Plat.', 'Name']

# Sort data by values descending

sorted_values, sorted_categories = values, categories

# Plot
fig, ax = plt.subplots(figsize=(6, 2))
bars = ax.barh(sorted_categories, sorted_values, color=['#1b5e20', '#2e7d32', '#66bb6a', '#f9a825', '#ef6c00', '#c62828'])

# Flip the y-axis so largest value is at the top
ax.invert_yaxis()
# Add values inside bars
for bar in bars:
    width = bar.get_width()
    ax.text(width / 2,                       # x = middle of the bar
            bar.get_y() + bar.get_height()/2,  # y = middle of the bar
            str(width),                      # label text
            ha='center', va='center',        # horizontal and vertical align center
            color='white')       # adjust font size/color as needed

# Labels and styling
ax.set_xlim(0, max(sorted_values) + 10)
plt.xlabel("Number of models")
path = Path("Python scripts used to create figures")
path.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
plt.savefig("open_source_llms.pdf")
plt.show()