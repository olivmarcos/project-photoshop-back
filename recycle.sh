#!/bin/bash

# List of directories to clean up
directories=("uploaded_images" "filtered_images" "images_histograms" "equalized_images")

for directory in "${directories[@]}"; do
    if [ -d "$directory" ]; then
        cd "$directory"

        find . ! -name ".gitkeep" -type f -exec rm -f {} \;

        cd ..
    else
        echo "Directory '$directory' does not exist."
    fi
done
