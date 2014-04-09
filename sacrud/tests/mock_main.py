#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
main function for functional test module
"""
from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings

from sacrud.tests.test_models import Profile, User


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    session_factory = session_factory_from_settings(settings)
    config = Configurator(settings=settings, session_factory=session_factory)

    # SACRUD
    config.include('sacrud.pyramid_ext', route_prefix='/admin')
    settings = config.registry.settings
    settings['sacrud.models'] = {'': [User],
                                 'Auth models': [User, Profile],
                                 }
    config.scan()
    return config.make_wsgi_app()
