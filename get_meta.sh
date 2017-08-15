#!/bin/bash
src=~/Pictures
find $src -name "*.png" -print -exec exiftool {} \; > meta.log
mkdir -p thumbnail
find $src -name "*.png" -exec ./get_thumbnail.sh {} \;
