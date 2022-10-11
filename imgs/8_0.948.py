d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)

d.end()
