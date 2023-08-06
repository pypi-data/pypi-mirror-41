# Muscle
Muscle is a weight lifting tracking app

## Dependencies
Python `>=3.5`

## Installation
```bash
python3 -m pip install --user muscle-xz18
```

## Usage
    muscle [option] [<argument>]

    -h, --help                          Show help message and exit
    --show-history                      Show workout history
    --record                            Record today's workout
    --delete-record [<date>]            Delete the record on a specific date,
                                        delete last record without argument
    --list-routine                      List user created routines
    --add-routine                       Add a new routine
    --delete-routine [<routine name>]   Delete a routine
    --import-db <path>                  Import a database
    --export-db <path>                  Export a database
    --gui                               Start muscle GUI (not implemented yet)
## Files
Muscle uses a sqlite database that is located at `~/.local/share/muscle/user.db`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To run the test:

    python3 setup.py test

alternatively:

    python3 -m unittest discover

## Roadmap
- [ ] gtk GUI
- [ ] show statistics/progress

## License
This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details