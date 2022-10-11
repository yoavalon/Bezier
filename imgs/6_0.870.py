d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
