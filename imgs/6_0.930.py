d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)

d.end()
