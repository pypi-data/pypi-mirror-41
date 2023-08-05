# coding: UTF-8

"""
HappyBase connection module.
"""

import logging

from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport, TFramedTransport, TSaslClientTransport
from TSaslClientTransport2 import TSaslClientTransport as TSaslClientTransport2
from thrift.protocol import TBinaryProtocol, TCompactProtocol
import getpass

from .hbase import Hbase
from .hbase.ttypes import ColumnDescriptor
from .table import Table
from .util import pep8_to_camel_case

logger = logging.getLogger(__name__)

COMPAT_MODES = ('0.90', '0.92', '0.94', '0.96')
THRIFT_TRANSPORTS = dict(
    buffered=TBufferedTransport,
    framed=TFramedTransport,
)
THRIFT_PROTOCOLS = dict(
    binary=TBinaryProtocol.TBinaryProtocolAccelerated,
    compact=TCompactProtocol.TCompactProtocol,
)

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 9090
DEFAULT_TRANSPORT = 'buffered'
DEFAULT_COMPAT = '0.96'
DEFAULT_PROTOCOL = 'binary'


class Connection(object):
    """Connection to an HBase Thrift server.

    The `host` and `port` arguments specify the host name and TCP port
    of the HBase Thrift server to connect to. If omitted or ``None``,
    a connection to the default port on ``localhost`` is made. If
    specifed, the `timeout` argument specifies the socket timeout in
    milliseconds.

    If `autoconnect` is `True` (the default) the connection is made
    directly, otherwise :py:meth:`Connection.open` must be called
    explicitly before first use.

    The optional `table_prefix` and `table_prefix_separator` arguments
    specify a prefix and a separator string to be prepended to all table
    names, e.g. when :py:meth:`Connection.table` is invoked. For
    example, if `table_prefix` is ``myproject``, all tables tables will
    have names like ``myproject_XYZ``.

    The optional `compat` argument sets the compatibility level for
    this connection. Older HBase versions have slightly different Thrift
    interfaces, and using the wrong protocol can lead to crashes caused
    by communication errors, so make sure to use the correct one. This
    value can be either the string ``0.90``, ``0.92``, ``0.94``, or
    ``0.96`` (the default).

    The optional `transport` argument specifies the Thrift transport
    mode to use. Supported values for this argument are ``buffered``
    (the default) and ``framed``. Make sure to choose the right one,
    since otherwise you might see non-obvious connection errors or
    program hangs when making a connection. HBase versions before 0.94
    always use the buffered transport. Starting with HBase 0.94, the
    Thrift server optionally uses a framed transport, depending on the
    argument passed to the ``hbase-daemon.sh start thrift`` command.
    The default ``-threadpool`` mode uses the buffered transport; the
    ``-hsha``, ``-nonblocking``, and ``-threadedselector`` modes use the
    framed transport.

    The optional `protocol` argument specifies the Thrift transport
    protocol to use. Supported values for this argument are ``binary``
    (the default) and ``compact``. Make sure to choose the right one,
    since otherwise you might see non-obvious connection errors or
    program hangs when making a connection. ``TCompactProtocol`` is
    a more compact binary format that is  typically more efficient to
    process as well. ``TBinaryAccelerated`` is the default protocol that
    happybase uses.

    The optional `auth_mechanism` and `kerberos_service_name` arguments specify
    if a SASL connection should be made
    As such, this feature can only be used on Python 2.7 onwards.

    .. versionadded:: 0.10
       `auth_mechanism` and `kerberos_service_name` and `user` arguments and `password` arguments
TSocket.py
    .. versionadded:: 0.9
       `protocol` argument

    .. versionadded:: 0.5
       `timeout` argument

    .. versionadded:: 0.4
       `table_prefix_separator` argument

    .. versionadded:: 0.4
       support for framed Thrift transports

    :param str host: The host to connect to
    :param int port: The port to connect to
    :param int timeout: The socket timeout in milliseconds (optional)
    :param bool autoconnect: Whether the connection should be opened directly
    :param str table_prefix: Prefix used to construct table names (optional)
    :param str table_prefix_separator: Separator used for `table_prefix`
    :param str compat: Compatibility mode (optional)
    :param str transport: Thrift transport mode (optional)
    """
    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT, timeout=None,
                 autoconnect=True, table_prefix=None,
                 table_prefix_separator='_', compat=DEFAULT_COMPAT,
                 transport=DEFAULT_TRANSPORT, protocol=DEFAULT_PROTOCOL,
                 auth_mechanism="NOSASL", kerberos_service_name='hbase',
                 user = None, password = None):

        if transport not in THRIFT_TRANSPORTS:
            raise ValueError("'transport' must be one of %s"
                             % ", ".join(THRIFT_TRANSPORTS.keys()))

        if table_prefix is not None \
                and not isinstance(table_prefix, basestring):
            raise TypeError("'table_prefix' must be a string")

        if not isinstance(table_prefix_separator, basestring):
            raise TypeError("'table_prefix_separator' must be a string")

        if compat not in COMPAT_MODES:
            raise ValueError("'compat' must be one of %s"
                             % ", ".join(COMPAT_MODES))

        if protocol not in THRIFT_PROTOCOLS:
            raise ValueError("'protocol' must be one of %s"
                             % ", ".join(THRIFT_PROTOCOLS))

        # Allow host and port to be None, which may be easier for
        # applications wrapping a Connection instance.
        self.host = host or DEFAULT_HOST
        self.port = port or DEFAULT_PORT
        self.timeout = timeout
        self.table_prefix = table_prefix
        self.table_prefix_separator = table_prefix_separator
        self.compat = compat
        self.auth_mechanism = auth_mechanism
        self.kerberos_service_name = kerberos_service_name
        self.user = user
        self.password = password

        self._transport_class = THRIFT_TRANSPORTS[transport]
        self._protocol_class = THRIFT_PROTOCOLS[protocol]
        self._refresh_thrift_client()

        if autoconnect:
            self.open()

        self._initialized = True

    def _refresh_thrift_client(self):
        """Refresh the Thrift socket, transport, and client."""
        socket = TSocket(self.host, self.port)
        if self.timeout is not None:
            socket.setTimeout(self.timeout)

        if self.auth_mechanism == "NOSASL":
            self.transport = self._transport_class(socket)
        else:
            self.transport = self._get_sasl_transport(socket)

        protocol = self._protocol_class(self.transport)
        self.client = Hbase.Client(protocol)

    def _get_sasl_transport(self, socket):
        user = self.user
        password = self.password
        if self.auth_mechanism in ['LDAP', 'PLAIN']:
            if self.user is None:
                user = getpass.getuser()
                logger.debug('get_transport: user=%s', user)
            if self.password is None:
                if self.auth_mechanism == 'LDAP':
                    password = ''
                else:
                    # PLAIN always requires a password for HS2.
                    password = 'password'
                logger.debug('get_transport: password=%s', password)
        try:
            import sasl

            def sasl_factory():
                sasl_client = sasl.Client()
                sasl_client.setAttr('host', self.host)
                if self.kerberos_service_name:
                    sasl_client.setAttr('service', self.kerberos_service_name)
                if self.auth_mechanism.upper() in ['PLAIN', 'LDAP']:
                    sasl_client.setAttr('username', user)
                    sasl_client.setAttr('password', password)
                sasl_client.init()
                return sasl_client
            return TSaslClientTransport2(sasl_factory, self.auth_mechanism, socket)
        except ImportError:
            logger.warn("Unable to import 'sasl'. Fallback ")
        return TSaslClientTransport(socket, self.host, self.kerberos_service_name)

    def _table_name(self, name):
        """Construct a table name by optionally adding a table name prefix."""
        if self.table_prefix is None:
            return name

        return self.table_prefix + self.table_prefix_separator + name

    def open(self):
        """Open the underlying transport to the HBase instance.

        This method opens the underlying Thrift transport (TCP connection).
        """
        if self.transport.isOpen():
            return

        logger.debug("Opening Thrift transport to %s:%d", self.host, self.port)
        self.transport.open()

    def close(self):
        """Close the underyling transport to the HBase instance.

        This method closes the underlying Thrift transport (TCP connection).
        """
        if not self.transport.isOpen():
            return

        if logger is not None:
            # If called from __del__(), module variables may no longer
            # exist.
            logger.debug(
                "Closing Thrift transport to %s:%d",
                self.host, self.port)

        self.transport.close()

    def __del__(self):
        try:
            self._initialized
        except AttributeError:
            # Failure from constructor
            return
        else:
            self.close()

    def table(self, name, use_prefix=True):
        """Return a table object.

        Returns a :py:class:`happybase.Table` instance for the table
        named `name`. This does not result in a round-trip to the
        server, and the table is not checked for existence.

        The optional `use_prefix` argument specifies whether the table
        prefix (if any) is prepended to the specified `name`. Set this
        to `False` if you want to use a table that resides in another
        ‘prefix namespace’, e.g. a table from a ‘friendly’ application
        co-hosted on the same HBase instance. See the `table_prefix`
        argument to the :py:class:`Connection` constructor for more
        information.

        :param str name: the name of the table
        :param bool use_prefix: whether to use the table prefix (if any)
        :return: Table instance
        :rtype: :py:class:`Table`
        """
        if use_prefix:
            name = self._table_name(name)
        return Table(name, self)

    #
    # Table administration and maintenance
    #

    def tables(self):
        """Return a list of table names available in this HBase instance.

        If a `table_prefix` was set for this :py:class:`Connection`, only
        tables that have the specified prefix will be listed.

        :return: The table names
        :rtype: List of strings
        """
        names = self.client.getTableNames()

        # Filter using prefix, and strip prefix from names
        if self.table_prefix is not None:
            prefix = self._table_name('')
            offset = len(prefix)
            names = [n[offset:] for n in names if n.startswith(prefix)]

        return names

    def create_table(self, name, families):
        """Create a table.

        :param str name: The table name
        :param dict families: The name and options for each column family

        The `families` argument is a dictionary mapping column family
        names to a dictionary containing the options for this column
        family, e.g.

        ::

            families = {
                'cf1': dict(max_versions=10),
                'cf2': dict(max_versions=1, block_cache_enabled=False),
                'cf3': dict(),  # use defaults
            }
            connection.create_table('mytable', families)

        These options correspond to the ColumnDescriptor structure in
        the Thrift API, but note that the names should be provided in
        Python style, not in camel case notation, e.g. `time_to_live`,
        not `timeToLive`. The following options are supported:

        * ``max_versions`` (`int`)
        * ``compression`` (`str`)
        * ``in_memory`` (`bool`)
        * ``bloom_filter_type`` (`str`)
        * ``bloom_filter_vector_size`` (`int`)
        * ``bloom_filter_nb_hashes`` (`int`)
        * ``block_cache_enabled`` (`bool`)
        * ``time_to_live`` (`int`)
        """
        name = self._table_name(name)
        if not isinstance(families, dict):
            raise TypeError("'families' arg must be a dictionary")

        if not families:
            raise ValueError(
                "Cannot create table %r (no column families specified)"
                % name)

        column_descriptors = []
        for cf_name, options in families.iteritems():
            if options is None:
                options = dict()

            kwargs = dict()
            for option_name, value in options.iteritems():
                kwargs[pep8_to_camel_case(option_name)] = value

            if not cf_name.endswith(':'):
                cf_name += ':'
            kwargs['name'] = cf_name

            column_descriptors.append(ColumnDescriptor(**kwargs))

        self.client.createTable(name, column_descriptors)

    def delete_table(self, name, disable=False):
        """Delete the specified table.

        .. versionadded:: 0.5
           `disable` argument

        In HBase, a table always needs to be disabled before it can be
        deleted. If the `disable` argument is `True`, this method first
        disables the table if it wasn't already and then deletes it.

        :param str name: The table name
        :param bool disable: Whether to first disable the table if needed
        """
        if disable and self.is_table_enabled(name):
            self.disable_table(name)

        name = self._table_name(name)
        self.client.deleteTable(name)

    def enable_table(self, name):
        """Enable the specified table.

        :param str name: The table name
        """
        name = self._table_name(name)
        self.client.enableTable(name)

    def disable_table(self, name):
        """Disable the specified table.

        :param str name: The table name
        """
        name = self._table_name(name)
        self.client.disableTable(name)

    def is_table_enabled(self, name):
        """Return whether the specified table is enabled.

        :param str name: The table name

        :return: whether the table is enabled
        :rtype: bool
        """
        name = self._table_name(name)
        return self.client.isTableEnabled(name)

    def compact_table(self, name, major=False):
        """Compact the specified table.

        :param str name: The table name
        :param bool major: Whether to perform a major compaction.
        """
        name = self._table_name(name)
        if major:
            self.client.majorCompact(name)
        else:
            self.client.compact(name)
