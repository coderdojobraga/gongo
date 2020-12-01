# Document Title

## Fork the repository
1. Go to the repository [coderdojobraga/gongo](https://github.com/coderdojobraga/gongo).
2. In the top-right corner of the page, click **Fork**.

   <img src="https://github-images.s3.amazonaws.com/enterprise/2.20/assets/images/help/repository/fork_button.jpg" width="350"/>

## Clone the forked repository
1. Go to **your fork** of the repository
2. Under the repository name, click **Clone or download**. 

   <img src="https://github-images.s3.amazonaws.com/enterprise/2.20/assets/images/help/repository/clone-repo-clone-url-button.png" with="350"/>
   
3. Copy the URL.
4. Open a Terminal.
5. Navigate to the location where you want the cloned directory.
6. Run the command `git clone` with the URL you copied earlier. It will look like this:
   ```sh
   git clone https://github.com/pr0t0typ3-ZeR0/gongo.git
   ```
Now, you have a local copy of your fork of the `gongo` repository.

## Install `python` in the specified version (using `asdf`)
1. Install the `asdf` package (depends on `curl` and `git`)
   
   ```sh
   git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.0
   ```
   
2. Add `asdf` to your shell
   - Bash:

      Add to ``~/.bashrc`:
      
      ```sh
      . $HOME/.asdf/asdf.sh
      ```

      And for completions add:

      ```sh
      . $HOME/.asdf/completions/asdf.bash
      ```
      
   - Fish:
   
      Add to `~/.config/fish/config.fish`:
      
      ```sh
      source ~/.asdf/asdf.fish
      ```
      
      And for completions run the command:
      
      ```sh
      mkdir -p ~/.config/fish/completions; and cp ~/.asdf/completions/asdf.fish ~/.config/fish/completions
      ```
      
   - ZSH:
   
      Add to `~/.zshrc`:
      
      ```sh
      . $HOME/.asdf/asdf.sh
      ```

      And for completions add:
     
      ```sh## Install the dependencies      # append completions to fpath
      fpath=(${ASDF_DIR}/completions $fpath)
      # initialise completions with ZSH's compinit
      autoload -Uz compinit
      compinit
      ```
      
      
      **Note:** you could also use a plugin like [asd for oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/asdf).

   **Note:** Restart your shell so that PATH changes take effect. (Opening a new terminal tab will usually do it.)

3. Install the `asdf-python` plugin for `asdf`

   Run the command:
   ```sh
   asdf plugin-add python
   ```
   
4. Install `python` in the specified version

   On the project root there's a file (`.python-version`) that contains the recomended python version to use, to install it just run the command (replacing `3.9.0` by the desired version):
   ```sh
   asdf install python 3.9.0 
   ```
   
5. Set python version
   
   Run the following command on the project folder (replacing `3.9.0` by the desired version):
   ```sh
   asdf local python 3.9.0
   ```
   
## Install the dependencies
   On the project folder, run:
   ```sh
   bin/setup
   ```
