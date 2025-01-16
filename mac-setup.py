#!/usr/bin/env python3
import os
import subprocess
from typing import Optional

github_username = "ywake"
brewed_path = os.environ["PATH"] + ":/opt/homebrew/bin"

def define_apps() -> list:
	return [
		Installer(
			title="Xcode Command Line Tools",
			commands=["xcode-select --install"],
			check="xcode-select -p",
		),
		Installer(
			title="Homebrew",
			commands=[
				'/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
			],
			check="command -v brew",
			path_override=brewed_path,
		),
		Installer(
			title="chezmoi",
			commands=["brew install chezmoi"],
			check="command -v chezmoi",
			path_override=brewed_path,
		),
		Installer(
			title="Dotfiles",
			commands=[
				f"chezmoi init {github_username}",
				"make -C ~/.local/share/chezmoi copy",
				"chezmoi apply",
			],
			check=None,
			path_override=brewed_path,
		),
		Installer(
			title="Brewfile",
			commands=["brew bundle --global"],
			check=None,
			path_override=brewed_path,
		),
		Installer(
			title="Python",
			commands=["pyenv install 3"],
			check="command -v pyenv",
			path_override=brewed_path,
		),
		Installer(
			title="Node.js",
			commands=["volta install node"],
			check="command -v volta",
			path_override=brewed_path,
		),
	]


class Installer:
	title: str # Display title
	commands: list[str] # Installation commands
	check_command: Optional[str] # Command to check if the app is already installed
	env: dict[str, str] # Environment variables

	def __init__(self, title: str, commands: list[str], check:Optional[str], path_override: Optional[str] = None):
		self.title = title
		self.commands = commands
		self.check_command = check
		self.env = os.environ.copy()
		if path_override is not None:
			self.env["PATH"] = path_override

	def go_nogo_poll(self) -> bool:
		if self.check_command is None:
			return True
		try:
			subprocess.run(self.check_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=self.env)
			return False
		except subprocess.CalledProcessError:
			return True

	def install(self) -> bool:
		for command in self.commands:
			res = subprocess.run(command, shell=True, check=False, env=self.env)
			if res.returncode == 0:
				continue
			else:
				return False
		return True

def installAll(apps: list[Installer]):
	for app in apps:
		go = app.go_nogo_poll()
		if not go:
			myprint(f"{app.title} is already installed. Skip.")
			continue
		myprint(f"Installing {app.title}...")
		success = app.install()
		if success:
			myprint(f"{app.title} is installed.")
		else:
			myprint(f"Failed to install {app.title}.")
			break

def myprint(msg: str):
	STYLE = "\033[1;36m" # CYAN BOLD
	RESET= "\033[0m"
	print(f"[{STYLE}mac-setup{RESET}] {msg}")


if __name__ == "__main__":
	apps: list[Installer] = define_apps()
	installAll(apps)
