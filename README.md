# tmux-bitahub

[![readthedocs](https://shields.io/readthedocs/tmux-bitahub)](https://tmux-bitahub.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/tmux-bitahub/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/tmux-bitahub/main)
[![github/workflow](https://github.com/Freed-Wu/tmux-bitahub/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/tmux-bitahub/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/tmux-bitahub/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/tmux-bitahub)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FFreed-Wu%2Ftmux-bitahub.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FFreed-Wu%2Ftmux-bitahub?ref=badge_shield)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/tmux-bitahub/total)](https://github.com/Freed-Wu/tmux-bitahub/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/tmux-bitahub/latest/total)](https://github.com/Freed-Wu/tmux-bitahub/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/tmux-bitahub)](https://github.com/Freed-Wu/tmux-bitahub/blob/main/LICENSE)
![github/languages](https://shields.io/github/languages/count/Freed-Wu/tmux-bitahub)
![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/tmux-bitahub)
![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/tmux-bitahub)
![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/tmux-bitahub)
![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/tmux-bitahub)
![github/v](https://shields.io/github/v/release/Freed-Wu/tmux-bitahub)

[![pypi/status](https://shields.io/pypi/status/tmux-bitahub)](https://pypi.org/project/tmux-bitahub/#description)
[![pypi/v](https://shields.io/pypi/v/tmux-bitahub)](https://pypi.org/project/tmux-bitahub/#history)
[![pypi/downloads](https://shields.io/pypi/dd/tmux-bitahub)](https://pypi.org/project/tmux-bitahub/#files)
[![pypi/format](https://shields.io/pypi/format/tmux-bitahub)](https://pypi.org/project/tmux-bitahub/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/tmux-bitahub)](https://pypi.org/project/tmux-bitahub/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/tmux-bitahub)](https://pypi.org/project/tmux-bitahub/#files)

Display [bitahub](https://bitahub.ustc.edu.cn/resources) GPU status in
[tmux](https://github.com/tmux/tmux) status line.

![Screenshot](https://user-images.githubusercontent.com/32936898/195975347-4024f8a9-3f13-4e1a-b84d-0e366d599c7f.png)

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Configure](#configure)
- [Install](#install)
- [tpm](#tpm)
- [PYPI](#pypi)
- [License](#license)

<!-- mdformat-toc end -->

## Configure

See [array `interpolation`](bitahub.tmux). E.g.,

```sh
tmux set -g status-right "1080ti #{bitahub_status_gtx1080ti}"
```

can display

> 1080ti 8:0 7:0 6:0 5:0 4:0 3:0 2:0 1:0

in the right status line of tmux. (Because now no any GTX1080Ti GPU left.)

## Install

## [tpm](https://github.com/tmux-plugins/tpm)

```tmux
set -g @plugin Freed-Wu/tmux-bitahub
run ~/.config/tmux/plugins/tpm/tpm
```

Make sure [requirements.txt](requirements.txt) has been installed.

## [PYPI](https://pypi.org/project/tmux-bitahub)

```sh
pip install tmux-bitahub
```

```tmux
run-shell python -m tmux_bitahub
```

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FFreed-Wu%2Ftmux-bitahub.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FFreed-Wu%2Ftmux-bitahub?ref=badge_large)
