d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.long)

d.end()
