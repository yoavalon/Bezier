d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)

d.end()
