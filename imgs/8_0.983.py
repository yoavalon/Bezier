d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
