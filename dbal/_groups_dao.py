"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from dbal.group import Group


class _GroupsDao:

    def __init__(self, ds):
        self.ds = ds

    def create_group(self, p):
        """
        (C)RUD: groups
        Generated values are passed to DTO.
        @type p: Group
        @rtype: None
        @raise: Exception if no rows inserted.
        """
        self.ds.create_one(p)

    def read_group(self, g_id):
        """
        C(R)UD: groups
        @type g_id: int
        @rtype: Group
        @raise: Exception if amount of returned rows != 1.
        """
        return self.ds.read_one(Group, {'g_id': g_id})

    def delete_group(self, g_id):
        """
        CRU(D): groups
        @type g_id: int
        @rtype: int (the number of affected rows)
        """
        return self.ds.delete_one(Group, {'g_id': g_id})