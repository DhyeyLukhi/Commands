import webbrowser as web

timeline = ['S', 'W']
for time in timeline:
    for year in range(2021, 2025):
        web.open(f"https://gtu.ac.in/uploads/{time}{year}/BE/3140705.pdf")

