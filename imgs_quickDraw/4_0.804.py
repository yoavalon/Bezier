d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.long)

d.end()
