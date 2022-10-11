d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.medium)

d.end()
