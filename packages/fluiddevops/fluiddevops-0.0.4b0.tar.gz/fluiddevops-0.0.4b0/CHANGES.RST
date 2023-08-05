0.0.4b0
-------
- Handle http error messages which are bytestrings
- New ``bitbucket``/``bb`` command!
- Remove hardcoded bb usage instructions
- Remove more hardcoded help messages
- Remove password decorator from clone, and restrict accidental delete command
- Show help with no subcommand for bb
- Tests pass, skip TestMirrorHgGit in CI
- Pin requests>2.20.0 CVE: 2018-18074
- Pin extras hg to working versions
- SVG logo, ungroup SVG, add logo_template.svg with editable text, CC-BY-SA 4.0
  in metadata
- License CC-BY-SA for logo template
- Raise error if repo is unconfigured for ``fluidmirror``.
- From setup.py to setup.cfg

0.0.3b1
-------
- Fixes a bug related to chdir after push encounters Destination is None
- rm six imports

0.0.3b0
-------
- Fluidmirror new init sub-command, list works when inside subdirectories
- New run sub-command to execute shell commands in repositories
- Resolve a lot of compatibility issues with other Python versions
- Tests and CI!

0.0.2b1
-------

- Improved fluidicat: displays wait time using threads
- Use threading.Event instead of sleep

0.0.2b0
-------

- New command fluidicat: intermittent cat
