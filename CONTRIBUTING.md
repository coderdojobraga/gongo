# Contributing

## Fork the repository

1. Go to the repository [coderdojobraga/gongo](https://github.com/coderdojobraga/gongo).

2. In the top-right corner of the page, click **Fork**.

   <img src="https://i.imgur.com/XGloZIz.png" width="350"/>

## Clone the forked repository

1. Go to **your fork** of the repository

2. Under the repository name, click **Code**.

   <img src="https://i.imgur.com/v12goA3.png" with="350"/>

3. Copy the URL.

   <img src="https://i.imgur.com/FbjI1Pu.png" with="350"/>

4. Open a Terminal.

5. Navigate to the location where you want the cloned directory.

6. Run the command `git clone` with the URL you copied earlier. It will look
   like this:

   ```sh
   git clone https://github.com/<your-github-username>/gongo.git
   ```

Now, you have a local copy of your fork of the `gongo` repository.

## Install `python` in the specified version

1. We recommend using `asdf` as the version manager

   You can read the installation guide [here](https://asdf-vm.com/#/core-manage-asdf).

   And then install the [asdf-python](https://github.com/danhper/asdf-python) plugin.

   ```sh
   asdf plugin-add python
   ```

   **Note:** You should set `legacy_version_file` to yes on the `asdf` config
   file (read more [here](https://asdf-vm.com/#/core-configuration?id=homeasdfrc))

## Install the dependencies

On the project directory, run:

```sh
bin/setup
```

## Get Discord bot token

1. Go to the [discord developer portal](https://discord.com/developers/applications).

2. In the top-right corner of the page, click **New Application**.

   <img src="https://i.imgur.com/W5TZdBT.png" with="350"/>

3. Type the name for your bot, and click **Create**.

   <img src="https://i.imgur.com/RGqKMaU.png" with="350"/>

4. In the left-hand panel click on **Bot** and then **Add Bot**.

   <img src="https://i.imgur.com/CMd2326.png" with="350"/>

5. Now on the right of the profile picture, click on the option
**Click to Reveal Token** to view the token ID.

   <img src="https://i.imgur.com/WlyAY1M.png" with="350"/>

## Modify the `.env` file to contain your bot token.

This file was created when you ran `bin/setup` and is located on the project
directory.

## Set up a Discord server to test the bot

1. Use [this server template](https://discord.com/template/qpH6udHU84sK) to clone
the existing server.

   <img src="https://i.imgur.com/EFGlMFh.png" with="350"/>

2. Invite the bot using a link like this:

   ```http
   https://discord.com/api/oauth2/authorize?client_id=<id>&permissions=<permissions>&scope=bot
   ```

   Where `<id>` is your bot's client id found in the
   [discord developer portal](https://discord.com/developers/applications)
   and `<permissions>` is the **permissions integer** that can be found on the
   bot's page, for now this value is set to `338757952` with the following
   permissions:

   <img src="https://i.imgur.com/x0Hwrjb.png" with="350"/>

## Create a branch to work on an issue or feature

On the project directory run the following command to create a new branch and
switch to it:

```sh
git checkout -b <branch>
```

Where `<branch>` is the name of the new branch.

## Push changes

1. After working on the branch, commit your changes:

   ```sh
   git commit -m "Commit message"
   ```

   **Recommendation:** [How to write a git commit message](https://chris.beams.io/posts/git-commit/)

2. Push the changes to your git repository:

   ```sh
   git push -u <remote> <branch>
   ```

   Here `<remote>` is the current branch’s remote (typically origin).

## Create pull request

1. Go to your fork of the repository.

2. Pick the branch you wish to have merged.

   <img src="https://i.imgur.com/DkSVWxG.png" with="350"/>

3. Click on **Pull request**

   <img src="https://i.imgur.com/2hwgtkZ.png" with="350"/>

4. Enter a **title** and **description** for your pull request.

   <img src="https://i.imgur.com/XZ9fRp2.png" with="350"/>
