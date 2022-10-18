d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)

d.end()
