d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(3,0)

d.end()
