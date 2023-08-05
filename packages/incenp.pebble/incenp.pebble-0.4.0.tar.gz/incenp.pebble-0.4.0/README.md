Pebble - Command-line Passman client
====================================

Pebble is a command-line client for the
[Passman](https://github.com/nextcloud/passman) password manager.

It supports read and write access to Passman vaults: it can list,
show, create, modify or delete entries in a vault. It cannot,
however, create or delete the vaults themselves.

Note that write support (creating, modifying, and deleting entries)
should be considered *experimental* at this stage. Use it on your
vaults at your own risks.


Configuration
-------------
Pebble requires a configuration file describing the vault(s) to use. The
configuration file uses the [INI
syntax](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure)
and is expected to be at `$XDG_CONFIG_HOME/pebble/config` by default;
another location may be specified using the `-c` option.

A vault is described in the configuration file by a section like in the
following example:

```
[default]
host: host.example.com
user: alice
password: mypassword
vault: MyVault
```

The file may contain several sections, one for each different vault.
Use the `-s` option to specify the name of the section to use (and thus,
which vault to connect to). By default, a section named `default` will
be used.

Inside a vault section, the `password` field may be omitted, in which
case the password will be asked interactively. Note: This is the
Nextcloud password, *not* the vault’s password! The vault password is
*always* asked interactively.

The `password` field may be replaced by `password_command`, which is a
command to execute to get the password. The command is expected to print
the password on its standard output and to terminate with a return code
of zero; if the return code is non-zero, the output is ignored and the
password will be asked interactively instead.

The `vault` field is the name of the vault, as chosen when creating the
vault in Passman’s web interface.

If several vaults share the same server settings, those settings may be
described in a separate section which may then be referred to with a
`server` field, as in the following example:

```
[myserver]
host: host.example.com
user: alice
password: mypassword

[default]
server: myserver
vault: MyVault

[second]
server: myserver
vault: MyAnotherVault
```


Use
---
With at least one vault configured, Pebble may then be used through the
`pbl` command and its subcommands. Use the `-h` option for a list of
available subcommands.

Pebble fetches the vault’s data and cache them locally in
`$XDG_DATA_HOME/pebble`. All entries are stored encrypted. The local
cache is refreshed from the server if it is more than 1 day old (or any
other value set by the `max_age` option, see below), this behavior may
be changed on the command line with the `--refresh` (force inconditional
refresh) or `--no-refresh` options (forbid refresh even if local cache
is old).

Cache settings may also be changed in the configuration file, within a
vault section:

* The `nocache` option, if set to `true`, forbids writing the contents
  of a vault to disk (the cache is only kept in memory).
* The `max_age` option changes the age after which the local cache is
  refreshed from the server. The value can be expressed as a number of
  seconds, or as a number of minutes, hours, or days by suffixing the
  number with `m`, `h`, or `d` respectively.


Copying
-------
Pebble is distributed under the terms of the GNU General Public License,
version 3 or higher. The full license is included in the [COPYING
file](COPYING) of the source distribution.


Homepage and repository
-----------------------
The project is located at <https://incenp.org/dvlpt/pebble.html>. The
latest source code is available in a Git repository at
<https://git.incenp.org/damien/pebble>.
