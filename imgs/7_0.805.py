d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,3)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)

d.end()
