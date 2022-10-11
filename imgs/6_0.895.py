d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
