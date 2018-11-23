# Bats test package for Sublime Text.

Bash Automated Testing System ([Bats](https://github.com/sstephenson/bats))
is a command tool for testing Bash/Shell.

## Installation

### Package Control

The easiest way to install is using Sublime's [Package Control](https://packagecontrol.io/packages/Bats%20(Bash%20Automated%20Testing%20System)). It's
listed as `Bats (Bash Automated Testing System)`.

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `Bats (Bash Automated Testing System)` and hit `Enter`

### Manually

1. [Download the tarball](https://github.com/sptndc/sublime-bats/releases)
2. Extract and rename folder to `Bats`
3. Copy folder into `Packages` directory, which you can find using
   the menu item `Preferences → Browse Packages...`

## Feature

### Syntax Highlight

All `.bats` files should automatically be assigned the
`Bash Automated Testing System (bats)` language/grammar.

### Snippets

The following snippets exist:

* `bats` - use at the top of a file to set the shebang to
  `#!/usr/bin/env bats`.
* `test` - inserts a `@test "test something" { … }` test block.
* `lines` - inserts a `[ "${lines[0]}" = "some value" ]` assertion.
* `status` - inserts a `[ "$status" -eq 0 ]` assertion.

## Development

Please feel free to submit pull requests and report a bugs on the
[issue tracker](https://github.com/sptndc/sublime-bats/issues).

## License

This project was released under the [MIT](LICENSE) License.
