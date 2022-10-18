d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.long)

d.end()
