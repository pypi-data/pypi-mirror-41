# Harvest `cropper`

`cropper` is a tool to explore your [Harvest](https://www.getharvest.com/) account and rewrite entries from one project task to another in harvest.

## Installation

You can install `cropper` by cloning this repository or by using [Pip](http://pypi.python.org/pypi/pip):

```sh
$ pip install harvest-cropper
```

If you want to use the development version, you can install directly from github:

```sh
$ pip install -e git+git://github.com/CartoDB/harvest-cropper.git#egg=harvest-cropper
```

If using, the development version, you might want to install dependencies as well:

```
$ pip install -r requirements.txt
```

**NOTE**: Only tested in Python **3.6.7**

## Usage

Just run `cropper` to see the different commands available, you can also run `cropper [command] --help` to check further details and options for every command.

The list of commands available are:

* `check` to confirm your account credentials are up and running
* `clients` to get a list or JSON of your registered clients
* `company` to get your organization details as a JSON object
* `projects` to get a list or JSON of your projects
* `project` gets details of an specific project
* `tasks` gets the list of tasks associated to a project
* `time-entries` return the timesheet entries added to a project
* `time-entry` returns a single timesheet
* `update-all-time-entries` will update a set of time entries
* `update-time-entry` will update an specific time entry
* `users` to get a list of your account users

You can check each command specific options just calling them with the `--help` option.

To authenticate against your Harvest account you need to specify your `token` and `account_id` as parameters on every execution you you can set up the environment variables `HARVEST_TOKEN` and `HARVEST_ID` that will be read automatically.

Finally, most of the commands can output both as text (CSV) or raw JSON formats as returned by the Harvest API, check [their docs](https://help.getharvest.com/api-v2/) for details.