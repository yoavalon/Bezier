d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
