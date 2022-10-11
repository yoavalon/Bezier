d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.N, Length.short)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
