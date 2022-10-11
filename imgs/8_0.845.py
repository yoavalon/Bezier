d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.position_pen(3,2)

d.end()
