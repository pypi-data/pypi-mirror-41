A flake8 plugin that rewrites error codes.

# Usage

Install using `pip`:
```
$ pip install flake8-rewriter
```

To activate the plugin, set the format option to "rewriter". Then pass in `--replace=<code1>:<code2>` for each code you want replaced. In this syntax, `<code1>` will be replaced with `<code2>`.

The following will turn all "line longer than length" errors to warnings.
```
$ flake8 --format=rewriter --replace=E501:W501
```