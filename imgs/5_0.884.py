d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,2)
d.position_pen(3,0)
d.curve(Direction.N, Orient.right, Length.short, Radius.low)
d.position_pen(1,1)

d.end()
