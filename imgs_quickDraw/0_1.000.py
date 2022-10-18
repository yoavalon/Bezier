d = DslBezier()

d.position_pen(2,1)
d.position_pen(1,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.position_pen(2,2)

d.end()
