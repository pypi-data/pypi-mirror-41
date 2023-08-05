# Droblo

A multi-hosts oriented, PostgreSQL backed, filesystem duplication detection system.

**Identify duplicated files on multiple hosts on the network, and/or ensure all files being watched are saved to 
multiple locations.**


Droblo uses a Postgresql database for storing files fingerprint of multiple hosts under watch.

- droblod is the daemon watching your hosts filesystem events, storing corresponding files fingerprints centrally.
- droblo_reports generates reports accordingly.

## Getting Started

### Prerequisites

* python 3.5 or above and the modules listed in pip_requirements.txt on machines where you intend to watch files from.

* a server running any PostgreSQL version still being maintained. 

### Installation

Please refer to [Droblo database setup](droblo/docs/droblo_database_setup.md) for creating the database.

Please refer to [Hosts installation](droblo/docs/hosts_installation.md) for installation of Droblo on the watched hosts.

### Commands usage

Please refer to [droblod](droblo/docs/droblod.md) for information on droblod usage.

Please refer to [droblo_reports](droblo/docs/droblo_reports.md) for information on reporting.

## License

This project is licensed under the GNU AFFERO GENERAL PUBLIC LICENSE Version 3 
- see [LICENSE.txt](LICENSE.txt) for details

