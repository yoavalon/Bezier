d = DslBezier()

d.position_pen(0,0)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,3)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
