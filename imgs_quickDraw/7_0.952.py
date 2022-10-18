d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.position_pen(3,3)
d.straight_line(Direction.E, Length.short)

d.end()
