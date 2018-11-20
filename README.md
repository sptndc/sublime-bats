# Sublime Text package for Bats.

Bash Automated Testing System ([Bats][]) is a test library running in
Bash/Shell, created by [@sstephenson][].

## Installation

Go to your Sublime Text Packages directory.

Sublime Text 2:
* Linux: `~/.config/sublime-text-2/Packages`
* macOS: `~/Library/Application\ Support/Sublime\ Text\ 2/Packages`
* Windows: `%APPDATA%/Sublime Text 2/Packages`

Sublime Text 3:
* Linux: `~/.config/sublime-text-3/Packages`
* macOS: `~/Library/Application\ Support/Sublime\ Text\ 3/Packages`
* Windows: `%APPDATA%/Sublime Text 3/Packages`

Clone the repository using a command below:

~~~sh
$ git clone https://github.com/sptndc/sublime-bats.git Bats
~~~

## Usage

All `.bats` files should automatically be assigned the `Bash
Automated Testing System (bats)` language/grammar.

The following snippets/commands exist:

* `bats` - use at the top of a file to set the environment to
  `#!/usr/bin/env bats`.
* `test` - inserts a `@test "test something" { … }` test block.
* `lines` - inserts a `[ "${lines[0]}" = "some value" ]` assertion.
* `status` - inserts a `[ "$status" -eq 0 ]` assertion.

## License

This project was released under the [MIT][] License.


[Bats]: https://github.com/sstephenson/bats
[MIT]: https://github.com/sptndc/sublime-bats/blob/master/LICENSE
[@sstephenson]: https://github.com/sstephenson
