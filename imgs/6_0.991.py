d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(0,0)

d.end()
