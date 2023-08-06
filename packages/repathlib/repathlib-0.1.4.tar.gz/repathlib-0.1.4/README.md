# `repathlib`

`repathlib` is a package that combines
[`repathlib`](https://docs.python.org/3/library/pathlib.html) and
[`re`](https://docs.python.org/3/library/re.html), enabling you to
search, match, etc., on `Path` objects, and to search directories with
`Path.reiterdir`: 

```python
from repathlib import Path
docs = Path('docs')
docs.search('d[a-z]+')
```
`<re.Match object; span=(0, 4), match='docs'>`

```python
list(docs.reiterdir('\.rst'))
```
`[PosixPath('docs/api.rst'), PosixPath('docs/index.rst')]`

Complete documentation is on [readthedocs](https://repathlib.readthedocs.io/en/latest/).
