d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.right, Length.short, Radius.high)
d.position_pen(2,1)

d.end()
