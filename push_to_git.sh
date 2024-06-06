#!/bin/bash

# Staging all changes
git add .

# Commit the changes with a timestamp
git commit -m "Update $(date +"%Y-%m-%d %H:%M:%S")"

# Connect to the GitHub repository
git remote add origin https://github.com/Maxvanaardg/active_campaign.git

# Push the changes to the remote repository
git push origin main

# Show a message when succesfull
echo "Wijzigingen zijn succesvol gepusht naar GitHub."

