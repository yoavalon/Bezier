d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
