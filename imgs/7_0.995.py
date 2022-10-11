d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,2)

d.end()
