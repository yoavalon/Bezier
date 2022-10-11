d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,3)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)

d.end()
