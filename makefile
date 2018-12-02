problems = $(shell ls ./*.py)
last_problem = $(shell ls ./*.py | tail -n 1)

all:
	for problem in  $(problems) ; do \
		echo $$problem ; \
		python3 $$problem ; \
	done

last:
	echo $(last_problem)
	python3 $(last_problem)
