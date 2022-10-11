d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.position_pen(0,0)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.position_pen(1,1)

d.end()
