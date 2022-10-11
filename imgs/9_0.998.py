d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)

d.end()
