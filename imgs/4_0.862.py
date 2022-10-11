d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.long)
d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
