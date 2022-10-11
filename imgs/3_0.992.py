d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.short)

d.end()
