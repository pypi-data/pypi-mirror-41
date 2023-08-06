# Brief

read/write .properties file in line-oriented format  
`key=value` per line *through function*.

*the code refers to `java.util.Properties` in Java 1.6.*


# Common Usage

* file I/O:
    ```python
    # input
    properties = load(file)
    # or update existing dictionary
    load(file, properties)
    
    # output
    store(file, properties)
    ```

* custom input:  
    `class LineReader` read in one key-value data. It skips all comment lines,  
    blank lines, leading whitespace, and processes multi-line data.  
    `loadSingle(string)` read each piece of data given above to key-value.  
    ```python
    for line in LineReader(file): # each key-value line has no line seperator
        key, value = loadSingle(line)
        # do something
    ```

* custom output:  
    `storeComments(writable, comments, linesep=os.linesep))`  
    write comment (accept multi-line), can specify the line terminator.  
    `storeSingle(writable, key, value, sep='=', linesep=os.linesep)`  
    write one key-value, can specify the seperator and the line terminator.  
    ```python
    storeComments(file, 'this is a comment')
    storeSingle(file, 'key', 'value')
    ```


# File Format

normally each line is comment line or a key-value pair.

main features:
* seperate key and value by one of `=`, `:`, ` `, `\t`
* ignore whitespaces leading in a line or around `=` or `:`
* comment line begin with `#` or `!`
* escape unicode by `\uxxxx`
* escape special characters by adding `\`

others:
* data line ends with `\` discard the line break

differences with Java:
* store method will not write datetime comment


# Changelog

## v0.1.1, 2019-2-9
* change to run with python3

## v0.1.0, 2018-6-7
* set up.  
