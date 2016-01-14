#!/bin/bash
#git remote add upstream https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template
#git fetch origin --prune  # Delete multiple obsolete tracking branches
git checkout master
git pull
git fetch upstream
git diff upstream/master
git merge upstream/master
git push
