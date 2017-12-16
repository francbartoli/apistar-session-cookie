#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tests for CookieSessionStore."""


import unittest
from random import randint

from apistar import http

from apistar_session_cookie import init_cookie_session


# Random order for tests runs. (Original is: -1 if x<y, 0 if x==y, 1 if x>y).
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: randint(-1, 1)


class TestCookieSessions(unittest.TestCase):

    maxDiff, __slots__ = None, ()

    def setUp(self):
        self.response_headers = http.ResponseHeaders()

    def tearDown(self):
        del self.response_headers

    def test_new_session_is_empty(self):
        with init_cookie_session(http.Header(""), self.response_headers) as session:
            self.assertEqual(session.data, {})

    def test_set_session(self):
        with init_cookie_session(http.Header(""), self.response_headers) as session:
            session["user"] = 1
            session["is_active"] = True
        cookie = http.Header(self.response_headers["Set-Cookie"])
        with init_cookie_session(cookie, self.response_headers) as session:
            self.assertEqual(session["user"], 1)
            self.assertEqual(session.get("is_active"), True)

        cookie = http.Header(self.response_headers["Set-Cookie"])
        with init_cookie_session(cookie, self.response_headers) as session:
            self.assertEqual(session.data, {"user": 1, "is_active": True})

    def test_unset_session(self):
        with init_cookie_session(http.Header(""), self.response_headers) as session:
            session["user"] = 1
            session["is_active"] = True
        cookie = http.Header(self.response_headers["Set-Cookie"])
        with init_cookie_session(cookie, self.response_headers) as session:
            del session["user"]
            self.assertTrue(session.get("is_active"))

        cookie = http.Header(self.response_headers["Set-Cookie"])
        with init_cookie_session(cookie, self.response_headers) as session:
            self.assertTrue("user" not in session)
            self.assertTrue(session.get("is_active"))
            del session["is_active"]

        cookie = http.Header(self.response_headers["Set-Cookie"])
        with init_cookie_session(cookie, self.response_headers) as session:
            self.assertEqual(session.data, {})

    def test_session_modification(self):
        with init_cookie_session(http.Header(""), self.response_headers) as session:
            session["user"] = 1
        modified_session = self.response_headers["Set-Cookie"].replace("a", "e")
        cookie = http.Header(modified_session)
        with init_cookie_session(cookie, self.response_headers) as session:
            self.assertEqual(session.data, {})


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
