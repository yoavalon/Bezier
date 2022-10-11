d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
