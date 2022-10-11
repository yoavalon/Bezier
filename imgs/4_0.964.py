d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.W, Length.short)
d.position_pen(0,3)
d.straight_line(Direction.S, Length.medium)

d.end()
