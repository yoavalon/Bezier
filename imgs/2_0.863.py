d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)

d.end()
