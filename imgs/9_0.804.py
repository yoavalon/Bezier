d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,3)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SW, Length.long)

d.end()
