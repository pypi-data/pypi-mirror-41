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

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

import sys

import tomlkit
import click
import os
from click_didyoumean import DYMGroup

from isomer.misc.path import set_instance
from isomer.logger import warn, critical
from isomer.tool import _get_system_configuration, ask, run_process, format_result, \
    log, error, debug, get_next_environment, _get_configuration
from isomer.tool.etc import write_instance, valid_configuration, \
    remove_instance, instance_template
from isomer.tool.templates import write_template
from isomer.tool.defaults import service_template, nginx_template, cert_file, key_file, distribution
from isomer.tool.defaults import EXIT_INSTALLATION_FAILED, EXIT_USER_BAILED_OUT, EXIT_INSTANCE_EXISTS, \
    EXIT_INSTANCE_UNKNOWN, EXIT_SERVICE_INVALID, \
    EXIT_INVALID_CONFIGURATION, EXIT_INVALID_PARAMETER
from isomer.tool.environment import install_environment_module, _clear_environment


@click.group(cls=DYMGroup)
@click.pass_context
def instance(ctx):
    """[GROUP] instance various aspects of Isomer"""

    if ctx.invoked_subcommand in ('info', 'list', 'create'):
        return

    _get_configuration(ctx)


@instance.command(name='info', short_help="show system configuration of instance")
@click.pass_context
def info_instance(ctx):
    """Print information about the selected instance"""

    instance_name = ctx.obj['instance']
    instances = ctx.obj['instances']
    instance_config = instances[instance_name]

    environment_name = instance_config['environment']
    environment_config = instance_config['environments'][environment_name]

    if instance_name not in instances:
        log('Instance %s unknown!' % instance_name, lvl=warn)
        sys.exit(EXIT_INSTANCE_UNKNOWN)

    log('Instance configuration:', instance_config, pretty=True)
    log('Active environment (%s):' % environment_name, environment_config, pretty=True)


@instance.command(name='list', short_help='List all instances')
@click.pass_context
def list_instances(ctx):
    """List all known instances"""

    for instance_name in ctx.obj['instances']:
        log(instance_name, pretty=True)


@instance.command(name='set', short_help='Set a parameter of an instance')
@click.argument('parameter')
@click.argument('value')
@click.pass_context
def set_parameter(ctx, parameter, value):
    """Set a configuration parameter of an instance"""

    log('Setting %s to %s' % (parameter, value))
    instance_config = ctx.obj['instance_config']
    defaults = instance_template

    try:
        parameter_type = type(defaults[parameter])
        log(parameter_type, pretty=True, lvl=warn)

        if parameter_type == tomlkit.items.Integer:
            converted_value = int(value)
        elif parameter_type == bool:
            converted_value = value.upper() == 'TRUE'
        else:
            converted_value = value
    except KeyError:
        log('Invalid parameter specified. Available parameters:', sorted(list(defaults.keys())), lvl=warn)
        sys.exit(EXIT_INVALID_PARAMETER)

    instance_config[parameter] = converted_value
    log('New config:', instance_config, pretty=True, lvl=debug)

    ctx.obj['instances'][ctx.obj['instance']] = instance_config

    if valid_configuration(ctx):
        write_instance(instance_config)
    else:
        log('New configuration would not be valid', lvl=critical)
        sys.exit(EXIT_INVALID_CONFIGURATION)


@instance.command(short_help="Create a new instance")
@click.pass_context
def create(ctx):
    """Create a new instance"""
    instance_name = ctx.obj['instance']
    if instance_name in ctx.obj['instances']:
        log('Instance exists!', lvl=warn)
        sys.exit(EXIT_INSTANCE_EXISTS)

    log('Creating instance:', instance_name)
    instance_config = instance_template
    instance_config['name'] = instance_name
    ctx.obj['instances'][instance_name] = instance_config

    write_instance(instance_config)


@instance.command(short_help="Install first environment for instance")
@click.pass_context
def install(ctx):
    """Install a new environment of an instance"""
    # TODO

    log('Would now install a blank instance')


@instance.command(name='clear', short_help="Clear the whole instance (CAUTION)")
@click.option('--force', '-f', is_flag=True, default=False)
@click.option('--no-archive', '-n', is_flag=True, default=False)
@click.pass_context
def clear_instance(ctx, force, no_archive):
    """Clear all environments of an instance"""

    _clear_instance(ctx, force, no_archive)


def _clear_instance(ctx, force, no_archive):
    log('Clearing instance:', ctx.obj['instance'])
    log('Clearing blue environment.', lvl=debug)
    _clear_environment(ctx, force, 'blue', no_archive)
    log('Clearing green environment.', lvl=debug)
    _clear_environment(ctx, force, 'green', no_archive)


@instance.command(short_help="Remove a whole instance (CAUTION)")
@click.option('--clear', '-c', is_flag=True, help='Clear instance before removal', default=False)
@click.pass_context
def remove(ctx, clear):
    """Remove a whole instance"""

    if clear:
        log('Destructively removing instance:', ctx.obj['instance'], lvl=warn)

    if not ask('Are you sure', default=False, data_type='bool'):
        sys.exit(EXIT_USER_BAILED_OUT)

    if clear:
        _clear_instance(ctx, force=True)

    new_config = ctx.obj['config']
    del new_config['instances'][ctx.obj['instance']]

    log(new_config, pretty=True, lvl=debug)
    remove_instance(ctx.obj['instance'])


@instance.command('install-module', short_help="Add (and install) a module to an instance")
@click.option('--source', '-s', default='github')
@click.option('--url', '-u', default=None)
@click.option('--install-env', '--install', '-i', is_flag=True, default=False,
              help='Install module on active environment')
@click.pass_context
def install_instance_module(ctx, source, url, install_env):
    """Add and install a module"""

    instance_name = ctx.obj['instance']
    instance_configuration = ctx.obj['instances'][instance_name]

    descriptor = {'source': source, 'url': url}
    if descriptor not in instance_configuration['modules']:
        instance_configuration['modules'].append(descriptor)

    write_instance(instance_configuration)

    if install_env is True:
        install_environment_module(ctx, source, url)

    log('Done: Install instance module')


@instance.command(short_help="Activates the other environment")
@click.option('--force', '-f', is_flag=True, default=False, help='Force turnover')
@click.pass_context
def turnover(ctx, force):
    """Activates the other environment """

    # if ctx.obj['acting_environment'] is not None:
    #    next_environment = ctx.obj['acting_environment']
    # else:
    next_environment = get_next_environment(ctx)

    log('Activating environment:', next_environment)
    env = ctx.obj['instance_config']['environments'][next_environment]

    log('Inspecting new environment')

    if not force:
        if env.get('database', '') == '':
            log('Database has not been set up correctly.', lvl=critical)
            sys.exit(EXIT_INSTALLATION_FAILED)

        if not env.get('installed', False) or not env.get('tested', False) or \
            not env.get('provisioned', False) or not env.get('migrated', False):
            log('Installation failed, cannot activate!', lvl=critical)
            sys.exit(EXIT_INSTALLATION_FAILED)

    update_service(ctx, next_environment)

    ctx.obj['instance_config']['environment'] = next_environment

    write_instance(ctx.obj['instance_config'])

    # TODO: Effect reload of service
    # * Systemctl reload
    # * (Re)start service
    # * confirm correct operation
    #  - if not, switch back to the other instance, maybe indicate a broken state for next_environment
    #  - if yes, Store instance configuration and terminate, we're done

    log('Done: Turnover to', next_environment)


def update_service(ctx, next_environment):
    """Updates the specified service configuration"""

    validated, message = validate_services(ctx)

    if not validated:
        log('Service configuration validation failed:', message, lvl=error)
        sys.exit(EXIT_SERVICE_INVALID)

    init = ctx.obj['config']['meta']['init']
    environment_config = ctx.obj['instance_config']['environments'][next_environment]

    log('Updating %s configuration of instance %s to %s' % (init, ctx.obj['instance'], next_environment))
    log('New environment:', environment_config, pretty=True)

    # TODO: Add update for systemd
    # * Stop possibly running service (it should not be running, though!)
    # * Actually update service files

    instance_name = ctx.obj['instance']
    config = ctx.obj['instance_config']

    env_path = '/var/lib/isomer/' + instance_name + '/' + next_environment

    log("Updating systemd service for %s (%s)" % (instance_name, next_environment))

    launcher = os.path.join(env_path, 'repository/iso')
    executable = os.path.join(env_path, 'venv/bin/python3') + " " + launcher
    executable += " --do-log --quiet --instance " + instance_name + ' launch'

    definitions = {
        'instance': instance_name,
        'executable': executable,
        'environment': next_environment,
        'user_name': config['user'],
        'user_group': config['group'],
    }
    service_name = 'isomer-' + instance_name + '.service'

    write_template(service_template, os.path.join('/etc/systemd/system/', service_name), definitions)


def _launch_service(ctx):
    """Actually enable and launch newly set up environment"""
    instance_name = ctx.obj['instance']

    service_name = 'isomer-' + instance_name + '.service'

    success, result = run_process('/', ['systemctl', 'enable', service_name], sudo='root')

    if not success:
        log('Error activating service:', format_result(result), pretty=True, lvl=error)
        sys.exit(5000)

    log('Launching service')

    success, result = run_process('/', ['systemctl', 'start', service_name], sudo='root')

    if not success:
        log('Error activating service:', format_result(result), pretty=True, lvl=error)
        sys.exit(5000)

    log("Done: Launch Service")


def validate_services(ctx):
    """Checks init configuration settings so nothing gets mis-configured"""

    # TODO: Service validation
    # * Check through all configurations that we're not messing with port numbers
    # * ???

    return True, "VALIDATION_NOT_IMPLEMENTED"


@instance.command(short_help='instance ssl certificate')
@click.option('--selfsigned', help="Use a self-signed certificate", default=False, is_flag=True, hidden=True)
@click.pass_context
def cert(ctx, selfsigned):
    """instance a local SSL certificate"""

    instance_cert(ctx, selfsigned)


def instance_cert(ctx, selfsigned):
    """instance a local SSL certificate"""

    instance_configuration = ctx.obj['instance_config']
    instance_name = ctx.obj['instance']
    next_environment = get_next_environment(ctx)
    hostnames = instance_configuration.get('web_hostnames', False)
    hostnames = hostnames.replace(' ', '')

    instance_argument = '' if instance_name == 'default' else '-i %s ' % instance_name

    if not hostnames or hostnames == 'localhost':
        log('Please configure the public fully qualified domain names of this instance.\n'
            "Use 'iso %sinstance set web_hostname your.hostname.tld' to do that.\n"
            "You can add multiple names by separating them with commas." % instance_argument, lvl=error)
        sys.exit(50031)

    set_instance(instance_name, next_environment)

    if not selfsigned:
        contact = instance_configuration.get('contact', False)
        if not contact:
            log('You need to specify a contact mail address for this instance to generate certificates.\n'
                "Use 'iso %sinstance set contact your@address.com' to do that." % instance_argument, lvl=error)
            sys.exit(50032)

        success, result = run_process('/', [
            'certbot', '--nginx', 'certonly',
            '-m', contact, '-d', hostnames,
            '--agree-tos', '-n'])
        if not success:
            log('Error getting certificate:', format_result(result), pretty=True, lvl=error)
            sys.exit(50033)
    else:
        log('This has been removed.')
        sys.exit()
        # log('Generating self signed (insecure) certificate/key combination')
        #
        # try:
        #     os.mkdir('/etc/ssl/certs/isomer')
        # except FileExistsError:
        #     pass
        # except PermissionError:
        #     log("Need root (e.g. via sudo) to generate ssl certificate")
        #     sys.exit(1)
        #
        # def create_self_signed_cert():
        #     """Create a simple self signed SSL certificate"""
        #
        #     # create a key pair
        #     k = crypto.PKey()
        #     k.generate_key(crypto.TYPE_RSA, 1024)
        #
        #     if os.path.exists(cert_file):
        #         try:
        #             certificate = open(cert_file, "rb").read()
        #             old_cert = crypto.load_certificate(crypto.FILETYPE_PEM,
        #                                                certificate)
        #             serial = old_cert.get_serial_number() + 1
        #         except (crypto.Error, OSError) as e:
        #             log('Could not read old certificate to increment '
        #                 'serial:', type(e), e, exc=True, lvl=warn)
        #             serial = 1
        #     else:
        #         serial = 1
        #
        #     # create a self-signed certificate
        #     certificate = crypto.X509()
        #     certificate.get_subject().C = "DE"
        #     certificate.get_subject().ST = "Berlin"
        #     certificate.get_subject().L = "Berlin"
        #     # noinspection PyPep8
        #     certificate.get_subject().O = "Hackerfleet"
        #     certificate.get_subject().OU = "Hackerfleet"
        #     certificate.get_subject().CN = gethostname()
        #     certificate.set_serial_number(serial)
        #     certificate.gmtime_adj_notBefore(0)
        #     certificate.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        #     certificate.set_issuer(certificate.get_subject())
        #     certificate.set_pubkey(k)
        #     certificate.sign(k, b'sha512')
        #
        #     open(key_file, "wt").write(str(
        #         crypto.dump_privatekey(crypto.FILETYPE_PEM, k),
        #         encoding="ASCII"))
        #
        #     open(cert_file, "wt").write(str(
        #         crypto.dump_certificate(crypto.FILETYPE_PEM, certificate),
        #         encoding="ASCII"))
        #
        #     open(combined_file, "wt").write(str(
        #         crypto.dump_certificate(crypto.FILETYPE_PEM, certificate),
        #         encoding="ASCII") + str(
        #         crypto.dump_privatekey(crypto.FILETYPE_PEM, k),
        #         encoding="ASCII"))
        #
        # create_self_signed_cert()
        #
        # log('Done: instance Cert')


@instance.command(short_help='install systemd service')
@click.pass_context
def service(ctx):
    """instance systemd service configuration"""

    update_service(ctx, ctx.obj['instance_config']['environment'])
    log('Done: Update init service')


@instance.command(short_help='instance nginx configuration')
@click.option('--hostname', default=None, help='Override public Hostname (FQDN) Default from active system '
                                               'configuration')
@click.pass_context
def update_nginx(ctx, hostname):
    """instance nginx configuration"""

    ctx.obj['hostname'] = hostname

    _create_nginx_config(ctx)
    log("Done: Update nginx config")


def _create_nginx_config(ctx):
    """instance nginx configuration"""

    # TODO: Specify template url very precisely. Currently one needs to be in the repository root

    instance_name = ctx.obj['instance']
    config = ctx.obj['instance_config']

    current_env = config['environment']
    env = config['environments'][current_env]

    dbhost = config['database_host']
    dbname = env['database']

    hostnames = ctx.obj['web_hostnames']
    if hostnames is None:
        hostnames = config['web_hostnames']
    if hostnames is None:
        try:
            configuration = _get_system_configuration(dbhost, dbname)
            hostnames = configuration.hostname
        except Exception as e:
            log('Exception:', e, type(e), exc=True, lvl=error)
            log("""Could not determine public fully qualified hostname!
Check systemconfig (see db view and db modify commands) or specify
manually with --hostname host.domain.tld

Using 'localhost' for now""", lvl=warn)
            hostnames = 'localhost'
    port = config['web_port']
    address = config['web_address']

    log("Creating nginx configuration for %s:%i using %s@%s" % (hostnames, port, dbname, dbhost))

    definitions = {
        'server_public_name': hostnames.replace(',', ' '),
        'ssl_certificate': cert_file,
        'ssl_key': key_file,
        'host_url': 'http://%s:%i/' % (address, port),
        'instance': instance_name,
        'environment': current_env
    }

    if distribution == 'DEBIAN':
        configuration_file = '/etc/nginx/sites-available/isomer.%s.conf' % instance_name
        configuration_link = '/etc/nginx/sites-enabled/isomer.%s.conf' % instance_name
    elif distribution == 'ARCH':
        configuration_file = '/etc/nginx/nginx.conf'
        configuration_link = None
    else:
        log('Unsure how to proceed, you may need to specify your '
            'distribution', lvl=error)
        return

    log('Writing nginx Isomer site definition')
    write_template(nginx_template, configuration_file, definitions)

    if configuration_link is not None:
        log('Enabling nginx Isomer site (symlink)')
        if not os.path.exists(configuration_link):
            os.symlink(configuration_file, configuration_link)

    log('Restarting nginx service')
    run_process('/', ['systemctl', 'restart', 'nginx.service'], sudo='root')

    log("Done: instance nginx configuration")

# TODO: Add instance user
