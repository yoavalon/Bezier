d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.SE, Length.short)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,0)

d.end()
