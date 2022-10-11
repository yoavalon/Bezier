d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)

d.end()
