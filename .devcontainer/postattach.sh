#!/bin/sh
# FILE: postattach.sh
# -----------------------------------

[ -z "$LOG_PREFIX" ] && LOG_PREFIX="[post-attach]"

# as opposed to echo, interpret C escape sequences properly in all envs
replay() {
    printf '%b\n' "$*"
}

# Print to stdout as messages with a prefix of $LOG_PREFIX
log() {
    replay "$@" | awk -v "PREFIX=$LOG_PREFIX" -F '\\\\n' '{print PREFIX " " $1}'
}

# Print to stderr as messages with a prefix of $LOG_PREFIX
error() {
    replay "$@" | awk >&2 -v "PREFIX=$LOG_PREFIX" -F '\\\\n' '{print PREFIX " " $1}'
}

# Prints and runs command
explicit_run_cmd() {
    cmd="$*"
    log "$> $cmd"
    eval "$cmd"
}

# Function to configure git repository to include project `.gitconfig`
config_git_project_gitconfig() {
  output="$(git config --local --get include.path || true)"
  if [ "$output" = "../.gitconfig" ]; then
    unset -v output
    return 0 # As desired, return silently
  fi
  unset -v output
  if [ -f "../.gitconfig" ] && ! git config --local include.path "../.gitconfig"; then
    error "ERROR: failed to add project .gitconfig to local git configuration."
    return 1
  fi
}

# Function to configure git repository to enforce GPG signed commits
config_git_commit_signing() {
  # check if configured properly
  if ! output="$(git config --get commit.gpgsign 2>/dev/null)"; then
    error "ERROR: missing commit.gpgsign setting in git config."
    return 1
  elif ! [ "$output" = "true" ]; then
    error "ERROR: commit.gpgsign must be set to true for project."
    return 1
  fi
  if ! git config --get user.signingkey 1>/dev/null 2>&1; then
    log "==============================================================="
    log "                   USER ACTION REQUIRED!"
    log "---------------------------------------------------------------"
    log "GPG commit signing is required for this repository! Please"
    log "configure your repository with the following command:"
    log "" # prefixed-newline
    log "    git config --local user.signingkey <GPG_KEY_ID>"
    log "" # prefixed-newline
    log "==============================================================="
  else
    log "Signature exists: user.signingkey=$(git config --get user.signingkey)"
  fi
}

# for devcontainers, its best to use ssh to contact origin since HTTPS requires user auth
# which is not easy to setup from within a container
config_git_ssh_origin() {
    output=""
    if ! output="$(git config --local --get remote.origin.url)"; then
        error "FATAL ERROR: Cannot find remote origin url."
        unset -v output
        return 1
    elif replay "$output" | grep -q "git@github.com:"; then
        unset -v output
        return 0
    fi
    ORIGIN_ORIGINAL_URL="$output"
    unset -v output

    # check ssh to github.com is configured, github throws exit 1 so just check message for desired message
    if ! ssh -Tq git@github.com 2>&1 1>/dev/null | grep -q "successfully authenticated"; then
        error "**** WARNING: SSH NOT CONFIGURED FOR GITHUB ****"
        error "**** FAILED COMMAND: ssh -T git@github.com ****"
        error "remote.origin.url='$ORIGIN_ORIGINAL_URL'"
        unset -v ORIGIN_ORIGINAL_URL
        return 0
    fi

    # make new url
    ORIGIN_SSH_URL="git@github.com:${ORIGIN_ORIGINAL_URL#*github.com/}"

    if ! git config --local remote.origin.url "$ORIGIN_SSH_URL"; then
        error "Failed to swap origin url to the ssh equivalent."
        unset -v ORIGIN_ORIGINAL_URL ORIGIN_SSH_URL
        return 1
    fi
    if ! git fetch origin >/dev/null 2>&1; then
        error "Failed to fetch from origin using an ssh url"
        error "Reseting origin url to original path."
        if ! git config --local remote.origin.url "$ORIGIN_ORIGINAL_URL"; then
            error "ERROR: Failed to reset origin to original url."
            return 1
        fi
    fi
    log "SUCCESS: Swapped origin to point at $ORIGIN_SSH_URL"
    unset -v ORIGIN_ORIGINAL_URL ORIGIN_SSH_URL
}

config_git_commit_able() {
  HAS_USERNAME=true
  HAS_EMAIL=true
  # check if configured properly
  if ! GIT_USERNAME="$(git config --get user.name 2>/dev/null)"; then
    error "ERROR: missing user.name setting in git config."
    HAS_USERNAME=false
  fi
  if ! GIT_EMAIL="$(git config --get user.email 2>/dev/null)"; then
    error "ERROR: missing user.email setting in git config."
    HAS_EMAIL=false
  fi
  if [ "$HAS_USERNAME" = "true" ] && [ "$HAS_EMAIL" = "true" ]; then
    log "Username found: user.name=$GIT_USERNAME"
    log "Email found: user.email=$GIT_EMAIL"
    return 0 # success
  fi
  error "Author identity unknown"
  log "==============================================================="
  log "                   USER ACTION REQUIRED!"
  log "---------------------------------------------------------------"
  log "Your git configuration is missing some settings which prevent  "
  log "you from being able to commit. To fix these settings, you can  "
  log "configure your repository with the following command(s):"
  log "" # prefixed-newline
  if [ "$HAS_USERNAME" = "false" ]; then
    log "    git config --local user.name <NAME>                        "
  fi
  if [ "$HAS_EMAIL" = "false" ]; then
    log "    git config --local user.email <EMAIL>                      "
  fi
  log "" # prefixed-newline
  log "Note: using '--local' is a matter of preference. It will define"
  log "only this repository's settings but it can be replaced with    "
  log "with --global if the change applies to all projects."
  log "==============================================================="
  return 1
}

# Unset all functions/vars this file creates
cleanup() {
  unset -v LOG_PREFIX VALID_GIT_CONFIG
  unset -f cleanup replay log error explicit_run_cmd \
           config_git_project_gitconfig config_git_commit_signing \
           config_git_ssh_origin config_git_commit_able
}


# ------------------
# MAIN
# ------------------

VALID_GIT_CONFIG="true"

# [1] Validate git configuration is intact
if ! config_git_project_gitconfig; then
    VALID_GIT_CONFIG="false"
fi
if ! config_git_commit_able; then
    VALID_GIT_CONFIG="false"
fi
if ! config_git_commit_signing; then
    VALID_GIT_CONFIG="false"
fi
if ! config_git_ssh_origin; then
    VALID_GIT_CONFIG="false"
fi
if [ "$VALID_GIT_CONFIG" = "true" ]; then
    log "SUCCESS: verified git config"
fi

cleanup
