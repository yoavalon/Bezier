d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)

d.end()
