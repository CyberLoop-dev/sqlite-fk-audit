<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=SQLite%20Foreign%20Key%20Audit&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="SQLite Foreign Key Audit banner" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=Find%20orphaned%20rows%20and%20integrity%20problems%20in%20SQLite%20databases" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/sqlite-fk-audit)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/sqlite-fk-audit)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/sqlite-fk-audit?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/sqlite-fk-audit)

<img src="assets/illustration.svg" alt="SQLite Foreign Key Audit illustration" width="92%"/>
</div>

## :compass: Overview

A read-only SQLite database checker that runs foreign_key_check and integrity_check, then presents orphan references and database integrity results as a concise report.

## :sparkles: Features

- :white_check_mark: Opens databases in read-only mode
- :white_check_mark: Finds rows that violate declared foreign keys
- :white_check_mark: Runs SQLite integrity_check
- :white_check_mark: Supports readable and JSON reports

## :clapper: Demo

```bash
python main.py examples/shop.db --json
```

The example runs locally; no hosted service or upload is required.

## :rocket: Quick Start

```bash
python -m pip install -r requirements.txt
python main.py --help
```

## :toolbox: Tech Stack

- Python 3.10+ standard library (sqlite3)
- Automated tests: unittest with temporary in-memory databases
- Local-first processing

## :file_folder: Folder Structure

```text
sqlite-fk-audit/\n├── main.py\n├── requirements.txt\n├── tests/test_core.py\n├── examples/README.md\n└── assets/illustration.svg
```

## :world_map: Roadmap

- [x] Core workflow
- [x] Example input and tests
- [ ] Additional report formats
- [ ] Continuous integration on supported platforms

## :handshake: Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior changes, and add tests for new features.

## :page_facing_up: License

MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>
