year := $(shell date +%Y )
day := $(shell date +%d )
day_path := $(year)/$(day)

day : 
	mkdir -p $(day_path)
	cp templates/template.py $(day_path)/$(day).py
	aocd > $(day_path)/input.txt