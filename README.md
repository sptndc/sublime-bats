# Sublime Text package for Bats.

Bash Automated Testing System ([Bats][]) is a test library running in
Bash/Shell, created by [@sstephenson][].

## Usage

All `.bats` files should automatically be assigned the `Bash
Automated Testing System (bats)` language/grammar.

The following snippets/commands exist:

* `bats` - use at the top of a file to set the environment to
  `#!/usr/bin/env bats`.
* `test` - inserts a `@test "test something" { … }` test block.
* `lines` - inserts a `[ "${lines[0]}" = "some value" ]` assertion.
* `status` - inserts a `[ "$status" -eq 0 ]` assertion.


[Bats]: https://github.com/sstephenson/bats
[@sstephenson]: https://github.com/sstephenson
