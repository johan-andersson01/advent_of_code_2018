problems = $(shell ls ./*.py)

solve:
	for problem in  $(problems) ; do \
		echo $$problem ; \
		python3 $$problem ; \
	done
