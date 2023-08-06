#!/usr/bin/python
from __future__ import absolute_import
import os
import sys
from .utils import *
from .constants import *
from .finder import Finder
from .auth import Authenticator
from .config import ConfigParser
from .download import Downloader

def _create_authenticator(config):
    auth = Authenticator()
    # check for saved credentials
    username = config.get('logins.username')
    password = config.get('logins.password')
    if username and password:
        print_info("Using saved credentials...")
        auth.ask_for_credentials(username=username, password=password)
    else:
        print_warning("Needs authentication. But you can save your credentials using ./leccap config! ")
        auth.ask_for_credentials()
    return auth

def download(config, url, auth=None):
    # extract dest path
    dest_path = config.get('dest_path')
    if dest_path == '.':
        dest_path = os.getcwd()
    downloader = Downloader(url, dest_path)
    # set concurrency``
    concurrency = config.get('concurrency')
    downloader.set_concurrency(concurrency)
    # check authentication
    if downloader.requires_auth():
        if auth is None:
            auth = _create_authenticator(config)
        downloader.set_auth(auth)
        if not downloader.get_auth().is_authenticated():
            print_info("Authenticating...")
            downloader.get_auth().authenticate()
    # start download
    downloader.start()

def search(config, subject, year=None):
    finder = Finder()
    if finder.requires_auth():
        auth = _create_authenticator(config)
        finder.set_auth(auth)
        if not finder.get_auth().is_authenticated():
            print_info("Authenticating...")
            finder.get_auth().authenticate()
    # start searching
    site_url = finder.search(subject, year)
    if not site_url:
        print_error("Cannot find recording site url for %s! Maybe due to wrong credentials or try enter a year!" % subject)
        return
    download(config, site_url, auth)

def reset_config(config, key):
    if key == 'all':
        # reset all
        config.set('logins', {'username': DEFAULT_MSG, 'password': DEFAULT_MSG, 'preferred': DEFAULT_MSG})
        config.set('concurrency', DEFAULT_CONCURRENCY)
        config.set('dest_path', DEFAULT_DIR)
    else:
        # reset parts
        if key in ['logins.username', 'logins.password', 'logins.preferred']:
            config.set(key, DEFAULT_MSG)
        elif key == 'concurrency':
            config.set(key, DEFAULT_CONCURRENCY)
        elif key == 'dest_path':
            config.set(key, DEFAULT_DIR)
        else:
            print_error("Key does not exist!")
            return
    config.save()
    print_success("Config has been reset!")

def update_config(config, key, value):
    try:
        config.set(key, value)
        config.save()
    except Exception as e:
        print_error(e.message)
    else:
        print_success("Config updated and saved!")
