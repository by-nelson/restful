#!/bin/bash
sudo apt-get update				# update repos
sudo apt-get install -y python3 python3-pip	# install python3 and pip3
pip3 install ansible				# install ansible
pip3 install ansibleantsibull-docs		# install docs generator

# add path to ansible binaries for bash
if [ -f "$HOME/.bashrc" ] && ! grep -Fq "/.local/bin" $HOME/.bashrc; then
	echo export PATH="$HOME/.local/bin:$PATH" >> $HOME/.bashrc
else
	echo "PATH already added to .bashrc"
fi

# add path to ansible binaries for zsh
if [ -f "$HOME/.zshrc" ] && ! grep -Fq "/.local/bin" $HOME/.zshrc; then
	echo export PATH="$HOME/.local/bin:$PATH" >> $HOME/.zshrc
else
	echo "PATH already added to .zshrc"
fi

