d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)
d.position_pen(2,1)
d.position_pen(0,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)

d.end()
