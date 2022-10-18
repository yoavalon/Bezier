d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
