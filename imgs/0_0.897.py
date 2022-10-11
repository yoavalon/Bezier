d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.long)

d.end()
