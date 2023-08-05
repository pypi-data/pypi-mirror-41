# -*- coding: utf-8 -*-

from nose.tools import assert_raises

from geokrety_api_exceptions import GKUnprocessableEntity
from geokrety_api_models import Geokret, Move, User
from geokrety_api_models.utilities.const import (GEOKRET_TYPE_TRADITIONAL,
                                                 MOVE_TYPE_GRABBED)

from . import DatabaseTest


class TestMove(DatabaseTest):
    """Test move"""

    def test_create(self):
        move = Move(moved_on_datetime="2019-01-19T22:46:44")
        self.session.add(move)
        with assert_raises(GKUnprocessableEntity):
            self.session.commit()

    def test_create_ok(self):
        user = User(name="username", password="password", email="user@geokrety.org")
        geokret = Geokret(name="My GeoKret",
                          type=GEOKRET_TYPE_TRADITIONAL,
                          created_on_datetime="2019-01-19T22:46:44")
        move1 = Move(geokret=geokret,
                     moved_on_datetime="2019-01-19T22:46:44",
                     type=MOVE_TYPE_GRABBED,
                     author=user)

        self.session.add(move1)
        self.session.commit()

        move2 = Move(geokret=geokret,
                     moved_on_datetime="2019-01-19T22:46:44",
                     type=MOVE_TYPE_GRABBED,
                     author=user)

        self.session.add(move2)
        with assert_raises(GKUnprocessableEntity):
            self.session.commit()
