# apistar-session-cookie

[Cookie](https://en.wikipedia.org/wiki/HTTP_cookie) based Sessions for [Apistar](https://github.com/encode/apistar). [![Build Status](https://travis-ci.org/juancarlospaco/apistar-session-cookie.svg?branch=master)](https://travis-ci.org/juancarlospaco/apistar-session-cookie)

![screenshot](https://source.unsplash.com/V4MBq8kue3U/800x400 "Photo by https://unsplash.com/@brookelark")

[![GPL License](http://img.shields.io/badge/license-GPL-blue.svg)](http://opensource.org/licenses/GPL-3.0)
[![LGPL License](http://img.shields.io/badge/license-LGPL-blue.svg)](http://opensource.org/licenses/LGPL-3.0)
[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](http://python.org)


# Documentation

##### init_cookie_session
<details>

`apistar_session_cookie.init_cookie_session(cookie: http.Header, response_headers: http.ResponseHeaders) -> Generator[http.Session, None, None]`

**Description:** [Apistar](https://github.com/encode/apistar#http-sessions) Component, initializes a SessionStore that works with Cookies
(This Code was Donated by the original Author Vlad Zolotoy to Juan Carlos the maintainer and packager).

**Arguments:**
- `cookie` An standard web browser cookie to work with, required, defaults to `apistar.http.Header`.
- `response_headers` Apistar HTTP Headers, required, defaults to `apistar.http.ResponseHeaders`.

**Keyword Arguments:** None.

**Returns:** `apistar.interfaces.SessionStore`.

**Source Code file:** https://github.com/juancarlospaco/apistar-session-cookie/blob/master/apistar_session_cookie.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:** See `example.py`

</details>


##### CookieSessionStore
<details>

`apistar_session_cookie.CookieSessionStore()`

**Description:** [`SessionStore`](https://github.com/encode/apistar#http-sessions) subclass extended and adapted to work with Cookies to provide a SessionStore for Apistar
(This Code was Donated by the original Author Vlad Zolotoy to Juan Carlos the maintainer and packager).

**Arguments:** None.

**Keyword Arguments:** None.

**Returns:** `apistar.http.Session`.

**Base Class:** `apistar.interfaces.SessionStore`.

**Source Code file:** https://github.com/juancarlospaco/apistar-session-cookie/blob/master/apistar_session_cookie.py

| State              | OS          | Description |
| ------------------ |:-----------:| -----------:|
| :white_check_mark: | **Linux**   | Works Ok    |
| :white_check_mark: | **Os X**    | Works Ok    |
| :white_check_mark: | **Windows** | Works Ok    |

**Usage Example:** N/A, should normally be used via `apistar_session_cookie.init_cookie_session()`, not directly.

</details>


#### Example

- [Check an actual working Example copied from official docs.](example/app.py)

Run it executing on the terminal command line: `apistar run`.

[http://127.0.0.1:8080/](http://127.0.0.1:8080/) Writes and Reads Session data.

[http://127.0.0.1:8080/logout/](http://127.0.0.1:8080/logout/) Deletes Session data.


# Install:

```
pip install apistar_session_cookie
```


# Requisites:

- [Apistar](https://github.com/encode/apistar)


# Tests

- Pull requests to improve tests are welcome!!!.

```bash
python -m unittest --verbose --locals tests.TestCookieSessions
# OR
python -m unittest
# OR
pytest
```

- [Test Templates.](https://gist.github.com/juancarlospaco/040fbe326631e638f2a540fe8c1f2092)


### Contributors:

- **Please Star this Repo on Github !**, it helps to show up faster on searchs.
- [Help](https://help.github.com/articles/using-pull-requests) and more [Help](https://help.github.com/articles/fork-a-repo) and Interactive Quick [Git Tutorial](https://try.github.io).
- English is the primary default spoken language, unless explicitly stated otherwise *(eg. Dont send Translation Pull Request)*
- Pull Requests for working passing unittests welcomed.


### Licence:

- GNU GPL Latest Version and GNU LGPL Latest Version and any Licence YOU Request via Bug Report.


### Ethics and Humanism Policy:

- Religions is not allowed. Contributing means you agree with the COC.


### Challenge

<details>
  
**Contributor:**

- Contributor must be 1 individual person (+18) that self-identify as Girl/Woman.
- Contributor must be living on Argentina, Antartida(AR) or Malvinas Argentinas.
- Contributor must agree with COC, Licences and general project philosophies.
- Contributor must Star, Fork and Pull Request the project on GitHub as usual.
- Contributor must provide 1 complete active valid written C.B.U. number.
- Payment delays 1 week (working days, not include bank delay), for peer reviews.
- Impersonations, fakes, bots, trolls, companies, organizations, Not allowed.

**Contribution:**

- Contribution must pass Ok all Unittests, CI, QA, Prospector, PreCommit, etc.
- Contribution must be 100% Python 3.6+ code, not C/C++/Go/Rust compiled module.
- Contribution must be 100% English language, correct grammar and punctuation.
- Contribution are manually evaluated 1 at a time, else it enters a queue.
- If someone already submitted the same Contribution dont submit the duplicated.
- Obfuscation, autogenerated-code, Code-Golf, overcomplicated, kludge, Not allowed.

**Target:**

Submit 1 of the following items (pick one):

- 1 Pull Request per 1 Contributor with 1 new relevant Feature with 1 Unittest (New Feature with at least 1 Unittest).

**Prize:**

- 1000 ARS.

We are investigating changing to Bitcoin prize eventually. If you dont understand the Challenge contact me before proceeding.

</details>
