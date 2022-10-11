d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,2)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)

d.end()
