d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NW, Length.long)
d.position_pen(3,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.long)

d.end()
