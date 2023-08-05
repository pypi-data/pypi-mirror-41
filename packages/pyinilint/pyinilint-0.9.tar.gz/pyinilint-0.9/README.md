# pyinilint
The `pyinilint` command line utility allows you to lint (check the
syntax) of [INI](https://en.wikipedia.org/wiki/INI_file)-like
configuration files. Here’s an example of the simplest possible
useage.

```console
$ pyinilint myfile.ini
```

Silent output, and a `0` exit status means that `myfile.ini` has been
parsed successfully.

The `pyinilint` utility is a front-end to the Python
[configparser](https://docs.python.org/3/library/configparser.html)
module, which supports interpolation. This means you can have
"variables" in your INI-files which can be optionally replaced with
values, which can be defined within the same, or different,
INI-file. Using different pyinilint command line switches you can
inspect what is happening with variable interpolation in your INI-files.


## Usage

```console
$ pyinilint --help
usage: pyinilint [-h] [-b] [-d] [-e ENCODING] [-m] [-o] [-r] [-s] [-v]
                 paths [paths ...]

pyinilint (version 0.9) is a linter and inspector for INI format files.

positional arguments:
  paths                 paths of the file(s) to check

optional arguments:
  -h, --help            show this help message and exit
  -b, --basic           use basic interpolation, the default is extended
  -d, --debug           show debugging messages
  -e ENCODING, --encoding ENCODING
                        set the encoding to be used, omit to use the default
  -m, --merge           merge files into a single configuration
  -o, --output          output the parsed configuration to stdout
  -r, --raw             output raw, do not interpolate
  -s, --serialize       output the interpolated and serialized configuration
                        to stdout
  -v, --verbose         show verbose messages

See https://github.com/danieljrmay/pyinilint for more information.
```

### Options

#### `-b`, `--basic`
Use basic interpolation when parsing. See the Python configparser
interpolation documentation below for more information.

#### `-d`, `--debug`
Output debugging messages, probably only of interest to those
developing pyinilint.

#### `-e ENCODING`, `--encoding ENCODING`
Specifiy a non-default encoding to use when parsing the files to be
checked.

#### `h`, `--help`
Display help and version information.

#### `-m`, `--merge`
Read all the specified `file`s into a single Python `ConfigParser`
object; this allows interpolation between files. When this option is
not specified each file is read into its own seperate `ConfigParser`
object.

#### `-o`, `--output`
Output the parsed configuration to `STDOUT` without any
interpolation. Use the `--serialize` options to enable interpolation.

#### `-r`, `--raw`
Use raw mode, so there is no interpolation when parsing. See the
Python configparser interpolation documentation below for more
information.

#### `-s`, `--serialize` 
Output the parsed, interpolated and serialized configuration to
`STDOUT`. Use this together with the `--basic`, `--merge` and `--raw`
options to inspect the interpolation of "variables" within you
INI-files.

#### `-v`, `--verbose`
Print verbose messages.


### Exit status
This is the list of exit status codes and their meanings returned to the shell by `pyinilint`.

| Exit Status | Name                   | Meaning                                                             |
| :---------: | ---------------------- | ------------------------------------------------------------------- |
|           0 | EXIT_OK                | Everything went well, all files linted successfully.                |
|           1 | EXIT_NON_EXISTANT_FILE | At least one of the specified files does not exist.                 |
|           2 | EXIT_SYNTAX_ERROR      | There was an error in the command line syntax.                      |
|           3 | EXIT_UNREADABLE_FILE   | At least one of the specified files existed but was not readable.   |
|           4 | EXIT_LINT_FAILED       | At least one of the specified files did not pass the syntax checks. |


### Examples

#### Check a single file
```console
$ pyinilint myfile.ini
```
A silent response (with exit status of 0) means that `myfile.ini` has
passed the lint check.

#### Check multiple individual files
```console
$ pyinilint -v myfile1.ini myfile2.ini
```
Check multiple files treating each one individually and output verbose
messages.

#### Check multiple files in a collection, and output the serialized results
```console
$ pyinilint -m -s myfile1.ini myfile2.ini
```
Check multiple files as part of a single `ConfigParser` object,
and output the parsed and interpolated values.

#### Check a file with a custom encoding
```console
$ pyinilint -e iso8859_15 myfile.ini
```
Check `myfile.ini` using  iso8859_15 encoding.


### Caution 

If your INI-files are ultimatly going to be parsed by an INI-parser
different from `ConfigParser` then you should be aware that there can
be subtle differences in INI-file format between parsers. However, it
should still spot most howling errors!

## References
* Python [configparser interpolation documentation](https://docs.python.org/3/library/configparser.html#interpolation-of-values)
* The [pyinilint project website](https://gitlab.com/danieljrmay/pyinilint)

