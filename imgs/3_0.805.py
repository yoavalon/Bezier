d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)

d.end()
