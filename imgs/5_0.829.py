d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.position_pen(1,3)
d.position_pen(3,0)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.short)

d.end()
