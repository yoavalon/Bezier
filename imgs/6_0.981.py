d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(3,1)

d.end()
