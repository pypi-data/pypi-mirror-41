from sqlalchemy.util import asbool

from . import connector
from ..base import ClickHouseDialect, ClickHouseExecutionContextBase

# Export connector version
VERSION = (0, 0, 2, None)


class ClickHouseExecutionContext(ClickHouseExecutionContextBase):
    def pre_exec(self):
        # Always do executemany on INSERT with VALUES clause.
        if self.isinsert and self.compiled.statement.select is None:
            self.executemany = True


class ClickHouseDialect_native(ClickHouseDialect):
    driver = 'native'
    execution_ctx_cls = ClickHouseExecutionContext

    @classmethod
    def dbapi(cls):
        return connector

    def create_connect_args(self, url):
        kwargs = {}
        port = url.port or 9000
        db_name = url.database or 'default'

        secure = url.query.get('secure')
        if secure is not None:
            url.query['secure'] = asbool(secure)

        verify = url.query.get('verify')
        if verify is not None:
            url.query['verify'] = asbool(verify)

        kwargs.update(url.query)

        return (url.host, port, db_name, url.username, url.password), kwargs

    def _execute(self, connection, sql):
        return connection.execute(sql)


dialect = ClickHouseDialect_native
