presentation.html:
	pandoc \
		--mathml \
		-st html5 \
		--metadata title="State Machines & Regular Languages" \
		-o presentation.html \
		presentation.md
