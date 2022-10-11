d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.N, Length.long)
d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)

d.end()
