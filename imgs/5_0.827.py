d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
