d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,2)
d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)

d.end()
