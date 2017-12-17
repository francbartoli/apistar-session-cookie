#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Minimum-possible self-contained example of apistar_session_cookie."""


from datetime import datetime
from getpass import getuser
from secrets import token_urlsafe

from apistar import Component, Route, http
from apistar.frameworks.wsgi import WSGIApp as App

from apistar_session_cookie import init_cookie_session


def login(username: str, session: http.Session) -> dict:
    session["username"] = username or getuser()            # Writes FAKE Data.
    session["last_login"] = datetime.utcnow().isoformat()  # Writes FAKE Data.
    session["token"] = token_urlsafe()                     # Writes FAKE Data.
    print(session.data)                                    # Reads Session Data.
    return session.data


def logout(session: http.Session) -> dict:
    if session.data:  # Clean out Session Data.
        del session["username"], session["last_login"], session["token"]
    return session.data


routes = (
    Route('/', 'GET', login),          # Writes and Reads Session Data.
    Route('/logout', 'GET', logout),   # Deletes Session Data.
)


cookie_sessions = (Component(http.Session, init=init_cookie_session), )


app = App(routes=routes, components=cookie_sessions)


if __name__ in '__main__':
    app.main()
