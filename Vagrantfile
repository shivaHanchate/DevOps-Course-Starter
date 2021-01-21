Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    sudo apt-get update

    # TODO: Install pyenv prerequisites

    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

    # TODO: Install pyenv

    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    
    
    # Initilise pyenv
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
    # Refresh shell for PATH changes to take effect
    . ~/.profile
    
    # Install new python version and set as default    
    pyenv install 3.8.3
    pyenv global 3.8.3
    python --version

    # Download and Install poetry
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

    #source $HOME/.poetry/env

  SHELL
end
