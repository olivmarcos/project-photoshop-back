#!/bin/bash

directory="uploads"

if [ -d "$directory" ]; then
    cd "$directory"

    find . ! -name ".gitkeep" -type f -exec rm -f {} \;

    cd ..

else
    echo "Directory '$directory' does not exist."
fi