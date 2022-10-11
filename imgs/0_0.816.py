d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
