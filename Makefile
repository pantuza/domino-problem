
#
# Makefile to rule domino-problem solution build, execution and analysis
#


# Binaries path
PYTHON := $(shell which python3.5)
GNUPLOT := $(shell which gnuplot)
EOG := $(shell which eog)
NOSETESTS := $(shell which nosetests)


help:
	@echo "Dominó problem"
	@echo
	@echo "Target rules:"
	@echo "    compute - Computes execution times for implemented algorithms"
	@echo "    plot    - Run GnuPlot to generate the computation analysis"
	@echo "    show    - Open resulted image using eog"
	@echo "    test    - Run tests using nose"
	@echo "    clean   - Removes log and image files"


compute: compute.py
	$(PYTHON) $^


plot: analysis.plt
	$(GNUPLOT) $^


show: time-complexity-analysis.png
	$(EOG) $^


test:
	$(NOSETESTS) --verbose


clean:
	@rm -rvf *.log *.png
