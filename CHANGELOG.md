# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Drop support for Python3.8, add support for Python3.13, bump PyPy test version to 3.10

## [1.0.3] - 4th of July 2024

### Changed
- Maintenance: adjust for various updates to mypy, cffi, gcc, ...

## [1.0.2] - 8th of November 2022

### Changed
- Exclude tests from the packages
- Fixed a small type error that appeared with the newest version of mypy

## [1.0.1] - 3rd of November 2022

### Added
- Python 3.11 to the list of supported versions

## [1.0.0] - 1st of November 2022

### Added
- Provide bindings to libxeddsa (version 2.0.0+)

### Removed
- Pre-stable (i.e. versions before 1.0.0) changelog omitted.

[Unreleased]: https://github.com/Syndace/python-xeddsa/compare/v1.0.3...HEAD
[1.0.3]: https://github.com/Syndace/python-xeddsa/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/Syndace/python-xeddsa/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/Syndace/python-xeddsa/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/Syndace/python-xeddsa/releases/tag/v1.0.0
