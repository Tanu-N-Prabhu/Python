#!/bin/sh

find . -depth -type f -not -path '*/\.git/*' -exec sh -c '
  for f; do
    # Convert to lowercase using tr
    new_name=$(echo "$f" | tr "[:upper:]" "[:lower:]")
    
    # Replace spaces with underscores
    new_name="${new_name// /_}"

    # Rename the file
    mv "$f" "$new_name"
  done' sh {} +

