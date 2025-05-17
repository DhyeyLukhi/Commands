import webbrowser as web

years = ['S', 'W']

for time in years:
    for year in range(2021, 2025):
        web.open(f"https://gtu.ac.in/uploads/{time}{year}/CS/1310503.pdf")