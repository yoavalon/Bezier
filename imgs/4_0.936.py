d = DslBezier()

d.position_pen(2,1)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(1,0)

d.end()
