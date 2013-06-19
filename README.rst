=======
 NoORM
=======

About
=====

NoORM is a very simple helper class that makes querying SQL databases more convenient. Objects of the ``NoORM.Row`` class represent one row of a query result. The ``NoORM.Row.select`` class method executes an SQL statement on a given cursor and returns a list of ``NoORM.Row`` objects. Each object stores the column values of a row in attributes that are named corresponding to the columns.