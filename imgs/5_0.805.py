d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)

d.end()
