# The argdirective project

Argdirective is a simple module which takes the first argument passed to your python script as subcommand and tries to find a directive module based on the basename of the script.

Example:
`script.py subcommand --arg1 --arg2`

Consider the following module:

```
site-packages
│   ...
│
└───configmount
│   │   mount
```

as well as the following executable script `/bin/configmount`

```python
#!/bin/python

import argdirective

if __name__ == "__main__":
	argdirective.generator.run()

```

If you run `configmount mount --root /etc /mnt/configmount` in your terminal argdirective will lookup the configmount package and redirect the arguments to the module mount. See the [configmount project](https://gitlab.com/domsonAut/configmount) for more details.
