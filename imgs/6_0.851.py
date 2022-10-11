d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)

d.end()
