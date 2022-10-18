d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SE, Length.long)

d.end()
