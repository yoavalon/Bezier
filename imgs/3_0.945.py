d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)

d.end()
