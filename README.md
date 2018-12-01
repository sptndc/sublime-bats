# Sublime Bats

[![GitHub release](https://img.shields.io/github/release/sptndc/sublime-bats.svg)](https://github.com/sptndc/sublime-bats/releases) [![Package Control](https://img.shields.io/packagecontrol/dt/Bats.svg)](https://packagecontrol.io/packages/Bats)

A [Bats](https://github.com/sstephenson/bats) test for Sublime Text.

## Installation

### Package Control

The easiest way to install using [Package Control](https://packagecontrol.io/).

1. Open `Command Palette` using menu item `Tools → Command Palette...`

2. Choose `Package Control: Install Package`

3. Find `Bats` and hit `Enter`

### Manually

If you prefer a manual approach, follow the steps below.

1. Goto into Sublime Text Packages directory, which you can find
   using the menu item `Preferences -> Browse Packages...`

2. Clone this repository.

    ```
    git clone https://github.com/sptndc/sublime-bats.git Bats
    ```

3. Enjoy!

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
