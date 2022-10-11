d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)
d.position_pen(1,0)

d.end()
