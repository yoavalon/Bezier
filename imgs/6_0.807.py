d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,3)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
