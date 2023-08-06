# Semversioner
The easiest way to manage [semantic versioning](https://semver.org/) in your project and generate an automatic Changelog file.

## Semantic Versioning
The [semantic versioning](https://semver.org/) spec involves several possible variations, but to simplify, in _Semversioner_ we are using the three-part version number:

`<major>.<minor>.<patch>`

Constructed with the following guidelines:
- Breaking backward compatibility or major features bumps the major (and resets the minor and patch).
- New additions without breaking backward compatibility bumps the minor (and resets the patch).
- Bug fixes and misc changes bumps the patch.

An example would be 1.0.0

## Install

```shell
$ pip install semversioner
```

## Usage

### Bumping the version

In your local environment your will use the CLI to create the different changeset files that will be committed with your code. For example:
```shell
$ semversioner add-change --type patch --description "Fix security vulnerability with authentication."
```

Then, in your CI/CD tool you will need to release (generating automatically version number) and creating the the changelog file. 
```shell
$ semversioner release
```

### Generating Changelog

As a part of your CI/CD workflow, you will be able to generate the Changelog file with all changes.

```shell
$ semversioner changelog > CHANGELOG.md
```

---
Made with ♥ by `Raul Gomis <https://twitter.com/rgomis>`.