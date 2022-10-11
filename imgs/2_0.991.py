d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()
