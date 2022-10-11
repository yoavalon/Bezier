d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)

d.end()
