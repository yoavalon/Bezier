d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)

d.end()
