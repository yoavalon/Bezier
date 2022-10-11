d = DslBezier()

d.position_pen(3,1)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)

d.end()
