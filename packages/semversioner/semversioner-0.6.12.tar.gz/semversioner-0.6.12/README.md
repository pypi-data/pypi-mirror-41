#Semversioner
The easiest way to manage [semantic versioning](https://semver.org/) in your project. 

##Install

```shell
$ pip install semversioner
```

## Usage

In your local environment your will use the CLI to create the different changeset files that will be committed with your code. For example:
```shell
$ semversioner add-change --type patch --description "Fix security vulnerability with authentication."
```

Then, in your CI / CD tool you will need to release (generating automatically version number) and creating the the changelog file. 
```shell
$ semversioner release
$ semversioner changelog > CHANGELOG.md
```

---
Made with ♥ by `Raul Gomis <https://twitter.com/rgomis>`.