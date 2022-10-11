d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
