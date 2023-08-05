# Meltano CLI

- `meltano init [project name]`: Create an empty meltano project.
- {: #meltano-add}`meltano add [extractor | loader ] [name_of_plugin]`: Adds extractor or loader to your **meltano.yml** file and installs in `.meltano` directory with `venvs` and `pip`.
- `meltano add [transform | transformer]`: Adds transform to your **meltano.yml** and updates the dbt packages and project configuration, so that the transform can run. Also used to install the `dbt` transformer for enabling transformations to run after extracting and loading data. 
- `meltano install`: Installs all the dependencies of your project based on the **meltano.yml** file.
- `meltano discover all`: list available extractors and loaders:
  - `meltano discover extractors`: list only available extractors
  - `meltano discover loaders`: list only available loaders
- `meltano extract [name of extractor] --to [name of loader]`: Extract data to a loader and optionally transform the data
- `meltano transform [name of transformation] --warehouse [name of warehouse]`: \*\*
- `meltano elt <extractor> <loader> [--dry] [--transform run]`: Extract, Load, and Transform the data.
- `meltano invoke <plugin_name> PLUGIN_ARGS...`: Invoke the plugin manually.
- `meltano select [--list] [--all] <tap_name> [ENTITIES_PATTERN] [ATTRIBUTE_PATTERN]`: Manage the selected entities/attribute for a specific tap.

## meltano select

> Note: not all tap support this feature; tap needs to support the --discover switch.
> You can use `meltano invoke tap-... --discover` to see if the tap supports it.

Use this command to add select patterns to a specific extractor in your Meltano project.

### Select Pattern

Meltano select patterns are inspired by the [glob](https://en.wikipedia.org/wiki/Glob_(programming)) syntax you might find in your operating system.

  - `*`: matches any sequence of characters
  - `?`: matches one character
  - `[abc]`: matches either `a`, `b`, or `c`
  - `[!abc]`: matches any character **but** `a`, `b`, or `c`

#### Examples

> Note: Most shells parse glob syntax: you must escape the special characters in the select pattern by quoting the pattern.

```bash
$ meltano select tap-carbon-intensity '*' 'name*'
```

This will select all attributes starting with `name`.

```bash
$ meltano select tap-carbon-intensity 'region'
```

This will select all attributes of the `region` entity.

### --exclude

Use `--exclude` to exclude all attributes that match the filter.

> Note: exclusion has precedence over inclusion. If an attribute is excluded, there
> is no way to include it back without removing the exclusion pattern first.

#### Examples

```bash
$ meltano select --exclude tap-carbon-intensity '*' 'longitude'
$ meltano select --exclude tap-carbon-intensity '*' 'latitude'
```

This will exclude all `longitude` and `latitude` attributes.

### --list

Use `--list` to list the current selected tap attributes.

> Note: `--all` can be used to show all the tap attributes with their selected status.

## How ELT Commands Fetch Dependencies

When you run ELT commands on a tap or target, this is the general process for fetching dependencies:

- First, the CLI looks in the project directory that you initialized
- Then it looks in the global file (`discovery.yml`) for urls of a package or repo
  - Note: This will eventually be moved into its own repository to prevent confusion since you cannot have local references for dependencies
- If this is the first time that the dependencies are requested, it will download to a local directory (if it is a package) or cloned (if it is a repo)
- By doing this, you ensure that packages are version controlled via `discovery.yml` and that it will live in two places:
  - in the project itself for the user to edit
  - in a global repo for meltano employees to edit
