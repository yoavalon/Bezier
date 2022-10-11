d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
