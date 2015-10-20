#!/bin/bash
#git remote add upstream https://github.com/AndreyAkinshin/Russian-Phd-LaTeX-Dissertation-Template
git checkout master
git pull
git fetch upstream
git diff upstream/master
git merge upstream/master
