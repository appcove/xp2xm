
xp2xm
=====

A simple tool for converting a list of xpath expressions to an xml document.

Copyright (c) 2013 AppCove, Inc.

* Designed to work with Python 3
* Simple one-function interface
* Accepts an iterable of strings as input
* Outputs several formats (xml, formatted xml, nested dicts)

--------

#### Sample Input Data:

```text
/data/customer/name
/data/customer/address
/data/customer/city
/data/customer/state
/data/customer/zip
/data/customer/phone/residential
/data/customer/phone/comercial
/data/file/createdate
/data/file/deleted
/data/file/deletedate
```

#### Sample Output Text:

```xml
<?xml version="1.0" ?>
<document>
  <data>
    <customer>
      <name/>
      <address/>
      <city/>
      <state/>
      <zip/>
      <phone>
        <residential/>
        <comercial/>
      </phone>
    </customer>
    <file>
      <createdate/>
      <deleted/>
      <deletedate/>
    </file>
  </data>
</document>
```



## Example:

```python
import xp2xm

data = open('sample-input.txt', 'r')
result = xp2xm.convert(data)
open('sample-output.txt', 'w').write(result)

```

## function convert(...)

`convert(lines, *, Output, Limit, PartRegex, RootName, IgnoreParts)`

#### lines
An iterable of strings, each in the format `/this/that/other`.  For example:

`open('input.txt', 'r')`   
or 
`data.split('\n')`  

#### Output
One of ('prettyxml', 'xml', 'dict').  Default is 'prettyxml'.

* prettyxml: return a formatted xml string
* xml: return a compact xml string
* dict: return a nested tree of OrderedDict objects

#### Limit
Number of parts to process.  Useful if this were to be used as a web service.  
Default is 100,000.

#### PartRegex
Regular expression used to validate that each xml node name is valid.  
Defaults to `^[a-zA-Z0-9_-]{1,64}$`.

#### RootName
Name of root xml node.  Defaults to `document`.

#### IgnoreParts
Number of leading sections of each line to ignore.  Default is 1.

This can be useful if you have the root node included in the document, for example:

```text
/document/name
/document/name/first
/document/name/last
/document/age
```

If you wish the result to be:

```xml
<person>
  <name>
    <first />
    <last />
  </name>
  <age />
</person>
```

Then you would call `convert(input, RootName='person', IgnoreParts=2)`

Why 2?  Because the empty space before the leading `/` is the first part, and `document` is the second part.
Then `person` is inserted as the root node.  It is as if the following were processed:

```text
name/first
name/last
age
```
And then inserted into `<person>...</person>`.



--
vim:encoding=utf-8:ts=2:sw=2:expandtab

