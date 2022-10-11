d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)

d.end()
