.PHONY: help copy
help:
	@echo "Usage: make [copy]"

CONF_DIR	:= $(HOME)/.config/chezmoi
REPO_DIR	:= $(HOME)/.local/share/chezmoi
copy:
	mkdir -p $(CONF_DIR) && cp -f $(REPO_DIR)/chezmoi.toml $$_

# Note: `$_`: The last argument of the previous command.
