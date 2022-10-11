d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,2)

d.end()
