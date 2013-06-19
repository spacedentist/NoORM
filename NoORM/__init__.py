"""Convenience helper for running SQL queries.
"""

class Row(dict):

    """Representation of a single row of a query result set."""

    __getattribute__ = dict.__getitem__

    @classmethod
    def select(cls, cursor, query, args=(), column_names=None, fetchall=True):
        """Execute a query on the given cursor and return a list of Row
        instances.

        args: arguments to be passed on to cursor.execute

        column_names: a list of the names of the columns that the query will
        return. Optional, defaults to the column names provided by the
        cursor.

        fetchall: if set to True return a fully populated list. Otherwise
        return a generator object. Defaults to True.
        """
        cursor.execute(query, args)

        if column_names is None:
            column_names = tuple(i[0] for i in cursor.description)

        if fetchall:
            return list(cls(zip(column_names, r)) for r in cursor.fetchall())
        else:
            return (cls(zip(column_names, cursor.fetchone()))
                    for i in range(cursor.rowcount))
