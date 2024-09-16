MAIN_FILE = main.py

DEPS = constants.py eos.py tov_solver.py tov_calculations.py utils.py plotting.py

PYTHON = python3

OUTPUT_DIR = outputs

all: run

run: $(MAIN_FILE) $(DEPS) $(OUTPUT_DIR)
	$(PYTHON) $(MAIN_FILE) $(ARGS)

time_test: $(MAIN_FILE) $(DEPS) $(POP_DIR) $(OUTPUT_DIR)
	$(PYTHON) $(MAIN_FILE) --time_test $(ARGS)

use_scipy: $(MAIN_FILE) $(DEPS) $(OUTPUT_DIR)
	$(PYTHON) $(MAIN_FILE) --use_scipy $(ARGS)

time_test_scipy: $(MAIN_FILE) $(DEPS) $(POP_DIR) $(OUTPUT_DIR)
	$(PYTHON) $(MAIN_FILE) --time_test --use_scipy $(ARGS)

clean:
	rm -rf __pycache__ $(OUTPUT_DIR)/*.png

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

help:
	@echo "Commands in the Makefile:"
	@echo "  make           		- Runs the main script"
	@echo "  make run       		- Runs the main script"
	@echo "  make time_test			- Measures the execution time of the program"
	@echo "  make use_scipy 		- Runs the main script using scipy ODE solver"
	@echo "  make time_test_scipy 	- Measures the execution time of the program when using scipy ODE solver"
	@echo "  make clean     		- Removes temporary and cache files"
	
