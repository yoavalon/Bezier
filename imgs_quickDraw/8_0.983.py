d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.position_pen(3,2)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
