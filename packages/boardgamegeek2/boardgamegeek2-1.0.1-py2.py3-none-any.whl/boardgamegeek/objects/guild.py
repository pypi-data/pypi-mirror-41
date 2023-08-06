# coding: utf-8
"""
:mod:`boardgamegeek.guild` - Guild information
==============================================

.. module:: boardgamegeek.guild
   :platform: Unix, Windows
   :synopsis: classes for storing guild information

.. moduleauthor:: Cosmin Luță <q4break@gmail.com>

"""
from __future__ import unicode_literals

from copy import copy

from .things import Thing


class Guild(Thing):
    """
    Class containing guild information
    """
    def _format(self, log):
        log.info("id         : {}".format(self.id))
        log.info("name       : {}".format(self.name))
        log.info("category   : {}".format(self.category))
        log.info("manager    : {}".format(self.manager))
        log.info("website    : {}".format(self.website))
        log.info("description: {}".format(self.description))
        log.info("country    : {}".format(self.country))
        log.info("state      : {}".format(self.state))
        log.info("city       : {}".format(self.city))
        log.info("address    : {}".format(self.address))
        log.info("postal code: {}".format(self.postalcode))
        if self.members:
            log.info("{} members".format(len(self.members)))
            for i in self.members:
                log.info(" - {}".format(i))

    def __init__(self, data):

        kw = copy(data)

        if "members" in kw:
            self._members = set(kw.pop("members"))
        else:
            self._members = set()

        super(Guild, self).__init__(kw)

    @property
    def country(self):
        """
        :return: country
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("country")

    @property
    def city(self):
        """
        :return: city
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("city")

    @property
    def address(self):
        """
        :return: address (both fields concatenated)
        :rtype: str
        :return: ``None`` if n/a
        """
        address = ""
        if self._data.get("addr1"):
            address += self._data.get("addr1")

        if self._data.get("addr2"):
            if len(address):
                address += " "  # delimit the two address fields by a space
            address += self._data.get("addr2")

        return address if len(address) else None

    @property
    def addr1(self):
        """
        :return: first field of the address
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("addr1")

    @property
    def addr2(self):
        """
        :return: second field of the address
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("addr2")

    @property
    def postalcode(self):
        """
        :return: postal code
        :rtype: integer
        :return: ``None`` if n/a
        """
        return self._data.get("postalcode")

    @property
    def state(self):
        """
        :return: state or provine
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("stateorprovince")

    @property
    def category(self):
        """
        :return: category
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("category")

    @property
    def members(self):
        """
        :return: members of the guild
        :rtype: set of str
        """
        return self._members

    @property
    def members_count(self):
        """
        :return: number of members, as reported by the server
        :rtype: int
        """
        return self._data.get("member_count", 0)

    @property
    def description(self):
        """
        :return: description
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("description")

    @property
    def manager(self):
        """
        :return: manager
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("manager")

    @property
    def website(self):
        """
        :return: website address
        :rtype: str
        :return: ``None`` if n/a
        """
        return self._data.get("website")

    def add_member(self, member):
        self._members.add(member)

    def __len__(self):
        return len(self._members)

    def __repr__(self):
        return "Guild (id: {})".format(self.id)

    def __iter__(self):
        for member in self._members:
            yield member
