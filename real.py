# -*- coding: UTF-8 -*-
class Counter:
  com = 0
  def __init__ (self):
    self.__class__.com += 1
    self.own = self.__class__.com
  def incr (self):
    self.own += 1

  def bla:
    spatOp = "Contains" if overlapMin is not None and overlapMin>=100 else "Intersects" # Currently, DHuS OpenSearch (solr) does not implement "Overlaps"!
    issue="not enough space"; severity=notify("%s: %s, free is %d MiB but estimated need is %d MiB!"%(folder, issue, int(round(free.value/MiB)), int(round(estimated/MiB))), 1)

#ACHTUNG Überdeckungseffekte... wenn man .__class__ weglässt, sprich self.com, wird das TROTZDEM gefunden... weil Suche-Automagie!?