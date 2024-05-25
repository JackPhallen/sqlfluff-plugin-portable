# SQLFluff Portability Rules

This is a plugin for [SQLFluff](https://github.com/sqlfluff) SQL Linter to identify SQL functions that are not portable 
across multiple SQL dialects. The example configuration provided is the intersect of MSSQL Server and Oracle SQL.

This plugin only checks function names. To test other features for portability, use the `ansi` dialect when running 
SQLFluff. Generally, a query that is compliant with ANSI will run on any database.

This repo includes a Python utility to calculate the intersect of two SQL dialects

## Getting Started
### Install
Install SQLFluff globally
```commandline
pip install sqlfluff
```
Install this plugin
```commandline
pip install -e .
```
The `-e` allows changes made to your local branch to be applied globally without the need to run `pip install` again. 
You can run `git pull` and the changes will be applied automatically.

The plugin is disabled by default. To enable the plugin please read the "Configure" section below.

### Configure
You likely do not want this plugin to run for all queries. That is why it is disabled by default. To enable this plugin,
copy `.sqlfluff` from `example_config/.sqlfluff` and drop it in one of the following locations:
1. Your home directory `~/` to enable the plugin globally
2. Between your cwd and the directory containing the files you want to enable this plugin for when linting. For example,
you can place `.sqlfluff` in your project root. SQLFluff searches all directories between cwd and the target file.
3. In the same directory as the files being linted.

Read more about SQLFluff configuration nesting here: [SQLFluff Configuration Nesting](https://docs.sqlfluff.com/en/stable/configuration.html#nesting)

If you have an existing SQLFluff configuration, you can copy the configuration fields from `example_config/.sqlfluff`
and add it to your existing configuration file.

The example configuration is the intersect of MSSQL Server and Oracle. If you notice a function missing, please add the
function to your configuration and then open an issue on Github so that I can apply the change to the repo.

### Test
There is a test query `testqueries/isnull.sql` which contains a function that is supported by MSSQL Server but not
Oracle. Once you have configured the plugin, test using this query.
```commandline
sqlfluff lint --dialect ansi testqueries/fail.sql
```
You should see a SQLFluff error for two functions that are not portable.

## Dialect Intersection Util

Run `intersect-util/src/main.py` to calculate the intersection between dialects. The intersection will be written to 
`output/intersection`. To add a new dialect, create a directory in `intersect-util/src/dialects`. Add one or more text 
file with a list of functions that are built-into the SQL dialect. In the oracle and tsql directories, I split up the 
functions into multiple files. This is not necessary.

The utility calculates the intersection between all dialects in the dialects directory. There is currently no support
for finding the intersect of a subset of dialects. 
