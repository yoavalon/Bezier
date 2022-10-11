d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)

d.end()
