# ShellLnk
Package for parsing Microsoft Shell Link (.lnk) files

This package consists of a parsing class shelllnk.ShellLnk. To use,

```python

from shelllnk import ShellLnk
open(myfile, "rb") as fd:
   shell_link = ShellLnk.parse(fd)
```

You may want to read the Microsoft spec on shell links to understand
the different parts of a shell link file. The file format doc is
at https://msdn.microsoft.com/en-us/library/dd871305.aspx

The stuff that I use is ShellLnk.file_attributes and 
ShellLnk.device_name or ShellLnk.net_name and ShellLnk.common_base_path_suffix.
The device name or net name tell you the drive letter or mount point
and the suffix gives you the path after that.