# Markr

> A library and script for associating marks/labels/key-values with a given
> file. Markr lets you perform operations on the marks for files.

Associating metadata with files/resources can be used to organize, search and
perform other operations on files. Markr provides a library and script to do
this using external attributes.

## Getting Started

Install the python3 package

```shell
pip3 install markr
```

Test setting and getting `marks`.

```shell
$ touch me.txt
$ markr set me.txt foo bar
$ markr set me.txt alice bob
$ markr get me.txt
foo : bar
alice : bob
```

Creating a mark directory

```shell
$ mkdir -p test/dir
$ touch test/dir/me.txt
$ markr set me.txt foo bar
$ markr set me.txt alice bob
$ markr get me.txt
alice : bob
foo : bar
$ markr dir test
$ tree marks
marks/
├── alice
│   └── me.txt -> ../../test/dir/me.txt
└── foo
    └── me.txt -> ../../test/dir/me.txt

2 directories, 2 files
```

## Advanced Features

The `dir` command scans all files underneath a given directory for marks, and
creates a new directory structure where each subdirectory is a given label. This
allows you to view what files have the same marks


## Licensing

MIT License.
