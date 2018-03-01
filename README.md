## dfa-integration

Author: Connor McArthur (connor@fishtownanalytics.com)

This integration extracts reports from DFA to S3 on a recurring schedule, as defined by your config file.

### Quick Start

1. Install

```bash
git clone git@github.com:fishtown-analytics/dfa-integration.git
cd dfa-integration
pip install .
```

2. Get credentials from DFA. You'll need to:

- create a 'Web Application' type app via the Google Developer Console, with the DFA API turned on.
- manually or automatically authenticate via OAuth.
- copy the refresh token, client ID, and client secret into the config file. [see instructions for manually going through the OAuth flow](AUTHENTICATION.md)

3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your credentials.

You'll need to specify a list of reports to run. Each report can optionally have a cron snippet defining how often it will try to run (although it can only run as often as you invoke the integration!)

Run it!

```bash
dfa-integration -c config.json -s state.json
```

---

Copyright &copy; 2018 Fishtown Analytics
