#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Minimum-possible self-contained example of apistar_session_cookie."""


from apistar import Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar import http
from getpass import getuser
from datetime import datetime
from apistar_session_cookie import init_cookie_session
from apistar import Component
from secrets import token_urlsafe


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
    Route('/',  'GET', login),         # Writes and Reads Session Data.
    Route('/logout', 'GET', logout),   # Deletes Session Data.
)


cookie_sessions = (Component(http.Session, init=init_cookie_session), )


app = App(routes=routes, components=cookie_sessions)


if __name__ in '__main__':
    app.main()
