# Contributing

When contributing to this repository, please first discuss the change you wish
to make via issue, email, or any other method with the owners of this repository
before making a change.

Please note we have a [Code of Conduct](CODE_OF_CONDUCT.md), please follow it in
all your interactions with the project.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
## **Table of Contents**

- [Fork the repository](#fork-the-repository)
- [Clone the forked repository](#clone-the-forked-repository)
- [Install `python` in the specified version](#install-python-in-the-specified-version)
- [Install the dependencies](#install-the-dependencies)
- [Get Discord bot token](#get-discord-bot-token)
- [Modify the `.env` file to contain your bot token.](#modify-the-env-file-to-contain-your-bot-token)
- [Create a branch to work on an issue or feature](#create-a-branch-to-work-on-an-issue-or-feature)
- [Push changes](#push-changes)
- [Create pull request](#create-pull-request)

<!-- markdown-toc end -->

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
   git clone https://github.com/<your-github-username>/gongo.git
   ```

Now, you have a local copy of your fork of the `gongo` repository.

## Install `python` in the specified version

1. We recommend using `asdf` as the version manager

   You can read the instalation guide [here](https://asdf-vm.com/#/core-manage-asdf).

   And then install the [asdf-python](https://github.com/danhper/asdf-python) plugin.

   ```sh
   asdf plugin-add python
   ```

   **Note:** You should set `legacy_version_file` to yes on the `asdf` config file (read more [here](https://asdf-vm.com/#/core-configuration?id=homeasdfrc))

## Install the dependencies

   On the project directory, run:

   ```sh
   bin/setup
   ```
   
## Get Discord bot token

1. Go to the [discord developer portal](https://discord.com/developers/applications).

2. In the top-right corner of the page, click **New Application**.

   <img src="https://www.discordtips.com/wp-content/uploads/2020/10/Create-Discord-Bot.jpg" with="350"/>
   
3. Type the name for your bot, and click **Create**.

   <img src="https://www.discordtips.com/wp-content/uploads/2020/10/Create-bot-in-Discord-compressed-300x250.jpg" with="350"/>

4. In the left-hand panel click on **Bot** and then **Add Bot**.

   <img src="https://www.discordtips.com/wp-content/uploads/2020/10/Discord-bot-token-compressed-768x233.jpg" with="350"/>

5. Now on the very right of the profile picture, click on the option **Click to Reveal Token** to view the token ID.

   <img src="https://www.discordtips.com/wp-content/uploads/2020/10/create-discord-bot-token-compressed-768x318.jpg" with="350"/>

## Modify the `.env` file to contain your bot token.

  This file was created when you ran `bin/setup` and is located on the project directory.

## Create a branch to work on an issue or feature

   On the project directory run the following command to create a new branch and switch to it:

   ```sh
   git checkout -b <branch>
   ```
   
   Where `<branch>` is the name of the new branch.
   
## Push changes
   
1. After working on the branch, commit your changes:

   ```sh
   git commit -m "Commit message"
   ```

   **Recomendation:** [How to write a git commit message](https://chris.beams.io/posts/git-commit/)

2. Push the changes to your git repository:

   ```sh
   git push -u <remote> <branch>
   ```

   Here `<remote>` is the current branch’s remote (typically origin).
   
## Create pull request

1. Go to your fork of the repository.

2. Pick the branch you wish to have merged.

3. Click on **Pull request**

4. Enter a **title** and **description** for your pull request. 
