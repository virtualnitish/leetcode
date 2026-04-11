.PHONY: new summary setup help check

help:
	@echo "LeetCode Jadia Workflow Commands:"
	@echo "  make new      - Create a new solution file (interactive)"
	@echo "  make summary  - Update README.md with the latest solved problems table"
	@echo "  make check    - Identify naming or header inconsistencies"
	@echo "  make setup    - Install optional dependencies for robust URL fetching (requires uv)"

new:
	python3 tools/filename_generate.py

summary:
	python3 tools/summary_generate.py

check:
	python3 tools/summary_generate.py --check

setup:
	@if command -v uv > /dev/null; then \
		echo "Installing dependencies with uv..."; \
		uv pip install curl_cffi beautifulsoup4; \
	else \
		echo "uv not found. Please install uv or use pip manually:"; \
		echo "pip install curl_cffi beautifulsoup4"; \
	fi
