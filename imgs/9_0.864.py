d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)

d.end()
