from PIL import Image

ims = []
for i in range(1,5):
    mask = Image.open(f"./clipinterrogator/sample{i}/mask.png")
    product = Image.open(f"./clipinterrogator/sample{i}/product.png")
    background = Image.open(f"./clipinterrogator/sample{i}/background.png").resize(mask.size)
    ims += [mask,product,background]
    
    background.save(f"./clipinterrogator/sample{i}/background.png")
