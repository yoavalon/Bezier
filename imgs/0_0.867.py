d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(1,3)

d.end()
