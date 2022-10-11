d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
