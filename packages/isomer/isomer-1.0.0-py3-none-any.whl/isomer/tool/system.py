#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import time
import click

from click_didyoumean import DYMGroup

from isomer.logger import error
from isomer.misc.path import locations, get_path, get_log_path
from isomer.tool import platforms, install_isomer, log, run_process

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"


@click.group(cls=DYMGroup)
@click.pass_context
@click.option('--platform', '-p', default=None, help='Platform name, one of %s' % list(platforms.keys()))
@click.option('--use-sudo', '-u', is_flag=True, default=False)
@click.option('--print-actions', '-p', help='Show what would be installed', is_flag=True, default=False)
def system(ctx, platform, use_sudo, print_actions):
    """[GROUP] Various aspects of Isomer system handling"""

    ctx.obj['platform'] = platform
    ctx.obj['use_sudo'] = use_sudo
    ctx.obj['print_actions'] = print_actions


@system.command(name='all', short_help='Perform all system setup tasks')
@click.pass_context
def system_all(ctx):
    """Performs all system setup tasks"""

    use_sudo = ctx.obj['use_sudo']

    install_isomer(ctx.obj['platform'], use_sudo, show=ctx.obj['print_actions'], omit_common=True)
    _add_system_user(use_sudo)
    _create_system_folders(use_sudo)
    log('Done: Setup system - all')


@system.command(short_help='Install system dependencies')
@click.pass_context
def dependencies(ctx):
    """Install Isomer platform dependencies"""

    log('Installing platform dependencies')

    install_isomer(ctx.obj['platform'], ctx.obj['use_sudo'], show=ctx.obj['print_actions'], omit_common=True)

    log('Done: Install dependencies')


@system.command(name='user', short_help='create system user')
@click.pass_context
def system_user(ctx):
    """instance Isomer system user (isomer.isomer)"""

    _add_system_user(ctx.obj['use_sudo'])
    log("Done: Add User")


def _add_system_user(use_sudo=False):
    """instance Isomer system user (isomer.isomer)"""

    command = [
        '/usr/sbin/adduser',
        '--system',
        '--quiet',
        '--home',
        '/var/run/isomer',
        '--group',
        '--disabled-password',
        '--disabled-login',
        'isomer'
    ]

    success, output = run_process('/', command, sudo=use_sudo)
    if success is False:
        log('Error adding system user:',lvl=error)
        log(output, lvl=error)

    time.sleep(2)


@system.command(name='paths', short_help='create system paths')
@click.pass_context
def system_paths(ctx):
    """instance Isomer system paths (/var/[local,lib,cache]/isomer)"""

    _create_system_folders(ctx.obj['use_sudo'])
    log("Done: Create system paths")


def _create_system_folders(use_sudo=False):
    target_paths = [
        '/var/www/challenges',  # For LetsEncrypt acme certificate challenges
        '/var/backups/isomer',
        '/var/log/isomer',
        '/var/run/isomer'
    ]
    for item in locations:
        target_paths.append(get_path(item, ''))

    target_paths.append(get_log_path())

    for item in target_paths:
        run_process('/', ['sudo', 'mkdir', '-p', item], sudo=use_sudo)

    # TODO: The group ownership is defined per instance
    run_process('/', ['sudo', 'chgrp', 'isomer', '/var/log/isomer'], sudo=use_sudo)
    run_process('/', ['sudo', 'chmod', 'g+w', '/var/log/isomer'], sudo=use_sudo)
