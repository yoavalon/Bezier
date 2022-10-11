d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)

d.end()
