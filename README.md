# Python Devcontainer with Poetry

This repository is set up to run within a development container (devcontainer) using either Visual Studio Code (VSCode) with local Docker or GitHub Codespaces. The Python environment is managed using Poetry for dependency management and virtual environment.

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed (for local VSCode setup).
- [Visual Studio Code](https://code.visualstudio.com/) with the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.
- (Optional) [GitHub Codespaces](https://github.com/features/codespaces) access for cloud-based development.

## Getting Started

### Using VSCode and Local Docker

1. Clone this repository to your local machine.
2. Open the repository folder in VSCode.
3. When prompted, click on "Reopen in Container". If not prompted, press `F1`, type "Remote-Containers: Open Folder in Container..." and select the repository folder.
4. The container will build and start. Once done, you'll be inside the container's environment.

### Using GitHub Codespaces

1. Fork this repository to your GitHub account.
2. Open the repository on GitHub and click on the "Code" button.
3. Select "Open with Codespaces" and create a new codespace.
4. Once the codespace is ready, you'll be inside the container's environment.

## Managing Dependencies with Poetry

1. To install dependencies, run:
   ```bash
   poetry install
   ```

2. To add a new dependency:
   ```bash
   poetry add <package-name>
   ```

3. To remove a dependency:
   ```bash
   poetry remove <package-name>
   ```

## Using the Poetry Shell

To activate the virtual environment managed by Poetry, run:

```bash
poetry shell
```

This will spawn a new shell subprocess, which will be the virtual environment. You can run Python scripts, use pip, etc., within this shell. To exit the virtual environment, simply type `exit`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
