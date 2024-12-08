# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots
from pathlib import Path
desktop = Path().home().joinpath("Desktop")
screenshots = desktop.joinpath("screenshots")
screenshots.mkdir(exist_ok=True)
count = 0

for f in desktop.iterdir():
    if f.suffix == ".png":
        print(f.name)
        count += 1
        f.replace(screenshots.joinpath("mac" + str(count) + f.suffix))
