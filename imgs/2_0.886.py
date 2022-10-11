d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.N, Length.medium)

d.end()
