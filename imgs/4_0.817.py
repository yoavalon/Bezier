d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.position_pen(1,3)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
