A flake8 plugin that rewrites error codes.

# Usage

Install using `pip`:
```
$ pip install flake8-rewriter
```

## With `format`
To activate the plugin, set the format option to "rewriter". Then pass in `--replace=<code1>:<code2>` for each code you want replaced. In this syntax, `<code1>` will be replaced with `<code2>`.

The following will turn all "line longer than length" errors to warnings.
```
$ flake8 --format=rewriter --replace=E501:W501
```

## With `force-rewriter`

In some cases, you may want to use a custom format string, or are unable to modify the `--format` option (such as within an IDE). Thus, the `--force-rewriter` option was implemented to handle these cases. Simply specify the `--force-rewriter` option **after** any `--format` options. If `--format` specifies a format string, then the plugin will output using that string.

The following does the same as above, but also changes the output formatting.
```
$ flake8 --format='%(row)d,%(col)d,%(code).1s,%(code)s:%(text)s' --force-rewriter --replace=E501:W501
```

# Changelong

```
v1.1.0:
    - Added --force-rewriter option
    - With --force-rewriter specified, flake8-rewriter now respects format strings specified through --format
```