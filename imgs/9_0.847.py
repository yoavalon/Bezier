d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)

d.end()
