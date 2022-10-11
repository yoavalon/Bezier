d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
