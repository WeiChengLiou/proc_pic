#!/bin/bash
dst="thumbnail/"$(basename "$1")
convert "$1" -thumbnail 256 "$dst"
