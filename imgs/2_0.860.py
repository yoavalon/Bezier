d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.position_pen(3,0)
d.straight_line(Direction.NE, Length.medium)

d.end()
