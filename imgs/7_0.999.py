d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(2,3)

d.end()
