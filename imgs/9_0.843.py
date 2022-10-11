d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
