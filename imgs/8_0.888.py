d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.short)
d.position_pen(3,3)

d.end()
