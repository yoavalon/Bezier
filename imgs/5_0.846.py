d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,3)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)

d.end()
