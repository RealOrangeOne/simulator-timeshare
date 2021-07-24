# simulator-timeshare

[![CI](https://github.com/RealOrangeOne/simulator-timeshare/actions/workflows/ci.yml/badge.svg)](https://github.com/RealOrangeOne/simulator-timeshare/actions/workflows/ci.yml)

Schedule simulator

## Design

A key design goal of this is for the simulation running to happen separately to the web server (likely from a non internet-accessible device).

The web server runs a database, and stores its files "externally" (ie not in its filesystem). Teams have a single shared login to do the tasks they need. Admins have their own, and have access to the Django admin.

The "runner" connects directly to the servers' database (yes, I know). It can then also read from the "external" file storage to download / upload artefacts. The runner needs an internet connection, but doesn't need to be internet accessible.
