# Scream Monorepo Example
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An example utilization of the [scream](https://github.com/r-kells/scream) monorepo manager to show off some of the features.
All files / folders you see in this repository were automatically generated by [scream](https://github.com/r-kells/scream).

Here are the commands to reproduce this repo.

## Setup

`scream init` sets up an empty repository with all the basic files you need for your python monorepo.

```bash
mkdir monorepo
cd monorepo

scream init
> Initialized empty Git repository in /Users/rk/py/scream-example/.git/
> INFO - Done!
> Create a new package with `scream new <namespace>.<package_name>`

scream new company.common
> INFO - Created project `company.common`

scream new company.project
> INFO - Created project `company.project`

# Remember to have python 3.6 installed (the default, you can change it.)
pyenv local 3.6.7

# Run all tests!
scream test --all

# Commit our initial project structure.
git add .
git commit -m "initial monorepo setup"

# Your repo here... 
git remote add origin git@github.com:r-kells/scream-example.git
git push -u origin master
```

## Dependencies

```bash
# Start working on a new feature.
git checkout -b link-packages
```
Add the following to `project/setup.cfg` `[options]`

This will make the package `project` depend on the package `common`.
By using explicitly defined dependencies `scream` will know how to build and test your repository.

While we are add it, add `flask` as a dependency.

`dependency_links` is not mandatory, but if you want to install `company_project` package
directly using pip you will need to add it. 

```ini
install_requires = 
    company_common 
    flask

dependency_links =
    git+ssh://git@github.com/r-kells/scream-example.git@master#egg=company_common-0#subdirectory=common
```

## Testing

`scream test` will use git to automatically detect which packages need to be tested.

If you change a package that is a dependency for other packages in this repository, 
each package that uses that dependency will be tested to make sure they are compatible with the changes.

The test command uses [tox](https://tox.readthedocs.io/en/latest/) 
to test all python versions specified in your [`setup.cfg`](https://github.com/r-kells/scream#configuration).
 
### Testing a single package

```bash
# Run scream test to make sure we didn't break anything
scream test
> INFO - The following packages have changes compared since branch: `link-packages`:
        company_project

> INFO - Packages that require testing:
        company_project
> ...
> ...
> ...

> py36-company_project: commands succeeded
> congratulations

# Save and push changes
git commit -am "linked"
git push --set-upstream origin link-packages

git checkout master
git pull origin link-packages
git push
```

## Installing your package

#### `pip install` a single package with dependencies

At this point we can `pip install` a package from anywhere.

```bash
pip install 'git+ssh://git@github.com/r-kells/scream-example.git@master#subdirectory=project' --process-dependency-links

> Successfully built company-project
> Installing collected packages: company-project
> Successfully installed company-project-0.0.1
```

#### `scream install`

If you are using CD/CI, you'll probably clone your monorepo into an environment for testing / deploying.
Using `scream install`, local dependencies are resolved automatically without needing `dependency_links`.

```bash
git clone git@github.com:r-kells/scream-example.git

scream install company_project
> INFO - Installing package: `company_project`...
> INFO - Installation complete.
```
