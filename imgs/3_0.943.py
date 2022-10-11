d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.W, Length.medium)

d.end()
