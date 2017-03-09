ls *.png | xargs -I{} basename {} .png | \
xargs -I{} convert {}.png -resize 50% {}.jpg
