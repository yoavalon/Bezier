d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.N, Length.long)

d.end()
