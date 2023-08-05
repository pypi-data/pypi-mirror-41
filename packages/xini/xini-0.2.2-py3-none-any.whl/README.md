### xini - eXtract pyproject.toml configs to INI

`pyproject.toml` is a fantastic idea. I want all my tool configurations
in my pyproject.toml file. Not all my tools support a `pyproject.toml`
configuration option though, but why wait?

`xini` pulls configurations from a `pyproject.toml` file for:

   * pytest
   * flake8
   * coverage
   * pylint

And generates the appropriate ini-config files.


### Install

    ... pip install xini


#### How Does It Work?

1. Write tool configuration in the `pyproject.toml` under the appropriate "[tool.toolname]"
   section. This becomes the standard location for your configurations.
   Keep `pyproject.toml` in source control as normal.

2. Run `xini` in the root project directory where the `pyproject.toml` file exits.
   (`xini` does not search for `pyproject.toml` files anywhere but the current directory.)

3. `xini` generates standard named ini-config files in the current directory
   (e.g. .flake8, .coveragerc, etc.). Tools that use old-style ini file formats can then
   run using the generated config file. **No need to maintain these ini-config files in source
   control.**

4. Make config changes in `pyproject.toml` and run `xini` to regnerate ini-config files.


#### The Future

It is my sincere hope that there is no future for this project. I wish
all tool developers to build support for `pyproject.toml` as a configuration
option so a tool like `xini` is unnecessary.
