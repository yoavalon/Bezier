d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)

d.end()
