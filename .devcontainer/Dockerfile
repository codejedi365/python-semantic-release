# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.217.4/containers/python-3/.devcontainer/base.Dockerfile
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"

COPY ./library-scripts/*.sh ./library-scripts/*.env /tmp/library-scripts/

RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    # add helpful system packages
    && apt install --no-install-recommends -y bash-completion rpm \
    # Ensure github:22 is a known-host
    && bash /tmp/library-scripts/known-hosts-debian.sh "github.com" \
    # Install global python packages if desired
    && pip3 --disable-pip-version-check --no-cache-dir install pip_search \
    # Install Node.js if desired
    && if [ "${NODE_VERSION}" != "none" ]; then \
        su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; \
    fi \
    # Install any global node packages (optional)
    # && su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1 \
    # Add helpful aliases
    && su vscode -c "umask 0002 && { echo 'alias ls=\"ls -lF --color=auto --group-directories-first\"'; echo 'alias la=\"ls -a\"'; } > ~/.bash_aliases" \
    # Cleanup
    && apt autoremove -y && apt-get clean -y && rm -rf /tmp/library-scripts
